import json, csv
from nlghi import domains
from nlghi.cli import main

def run_cli(args):
    import sys, io
    buf = io.StringIO(); old = sys.stdout
    try:
        sys.stdout = buf; main(args)
    finally:
        sys.stdout = old
    return buf.getvalue()

def test_compute_and_store(tmp_path):
    csv_path = tmp_path / "visit.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=domains.DOMAINS); w.writeheader()
        row = {d: (i % 6) for i, d in enumerate(domains.DOMAINS)}; w.writerow(row)
    out = json.loads(run_cli(["compute-csv", str(csv_path)]))
    assert "ghi" in out and "dsav" in out and len(out["dsav"]) == 27
    store_path = tmp_path / "store.json"
    out2 = json.loads(run_cli(["add-visit", "--mcp", "123", "--date", "2025-09-01", str(csv_path), str(store_path)]))
    assert out2["status"] == "ok"
    out3 = json.loads(run_cli(["summarize", "--mcp", "123", str(store_path)]))
    assert len(out3) == 1 and out3[0]["date"] == "2025-09-01"
