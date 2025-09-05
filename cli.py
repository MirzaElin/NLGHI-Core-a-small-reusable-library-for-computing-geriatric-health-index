import argparse, json, csv
from . import core, domains
from .io import Store

def _read_csv_row(path):
    with open(path, "r", encoding="utf-8") as f:
        r = csv.DictReader(f); row = next(r)
    cols = [c.strip() for c in row.keys()]; imp = []
    if set(domains.DOMAINS).issubset(set(cols)):
        for d in domains.DOMAINS: imp.append(float(row.get(d,0)))
    else:
        for c in cols:
            try: imp.append(float(row[c]))
            except: imp.append(0.0)
        if len(imp) != 27: raise SystemExit("CSV must have all 27 domain columns or exactly 27 numeric columns.")
    return imp

def main(argv=None):
    p = argparse.ArgumentParser(prog="nlghi", description="NLGHI Core CLI")
    sub = p.add_subparsers(dest="cmd", required=True)
    sp = sub.add_parser("compute"); sp.add_argument("--impairments", required=True)
    sp = sub.add_parser("compute-csv"); sp.add_argument("csv_path")
    sp = sub.add_parser("add-visit"); sp.add_argument("--mcp", required=True); sp.add_argument("--date", required=True); sp.add_argument("csv_path"); sp.add_argument("store_path")
    sp = sub.add_parser("summarize"); sp.add_argument("--mcp", required=True); sp.add_argument("store_path")
    args = p.parse_args(argv)
    if args.cmd == "compute":
        vals = [float(x.strip()) for x in args.impairments.split(",")]
        dsav, ghi = core.compute(vals, domains.WEIGHTS); print(json.dumps({"dsav":dsav,"ghi":ghi}, indent=2))
    elif args.cmd == "compute-csv":
        vals = _read_csv_row(args.csv_path); dsav, ghi = core.compute(vals, domains.WEIGHTS); print(json.dumps({"dsav":dsav,"ghi":ghi}, indent=2))
    elif args.cmd == "add-visit":
        vals = _read_csv_row(args.csv_path); dsav, ghi = core.compute(vals, domains.WEIGHTS); store = Store(args.store_path); store.upsert(args.mcp, args.date, vals, dsav, ghi); print(json.dumps({"status":"ok","mcp":args.mcp,"date":args.date,"ghi":ghi}, indent=2))
    elif args.cmd == "summarize":
        store = Store(args.store_path); out = store.timeseries(args.mcp); print(json.dumps(out, indent=2))
    else:
        p.print_help()

if __name__ == "__main__":
    main()
