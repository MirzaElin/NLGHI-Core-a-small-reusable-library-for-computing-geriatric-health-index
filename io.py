import json, os
from typing import List

class Store:
    def __init__(self, path: str):
        self.path = path; self.data = {}
        if os.path.exists(path):
            try:
                with open(path,"r") as f: self.data = json.load(f)
            except Exception: self.data = {}
    def upsert(self, mcp: str, date: str, impairments: List[float], dsav: List[float], ghi: float):
        self.data.setdefault(mcp, {}); self.data[mcp][date] = {"impairments":impairments,"dsav":dsav,"ghi":ghi}; self._save()
    def timeseries(self, mcp: str):
        if mcp not in self.data: return []
        kv = sorted(self.data[mcp].items(), key=lambda kv: kv[0])
        return [{"date":d, "ghi": r.get("ghi",0.0)} for d,r in kv]
    def _save(self):
        with open(self.path,"w") as f: json.dump(self.data, f, indent=2)
