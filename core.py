from typing import List, Tuple

def compute(impairments: List[float], weights: List[float]) -> Tuple[list, float]:
    if len(impairments) != len(weights):
        raise ValueError("impairments and weights must have same length (27).")
    imp = [max(0.0, min(5.0, float(x))) for x in impairments]
    dsav = [imp[i] * float(weights[i]) for i in range(len(imp))]
    ghi = round(sum(dsav) / 27.0, 4)
    return dsav, ghi
