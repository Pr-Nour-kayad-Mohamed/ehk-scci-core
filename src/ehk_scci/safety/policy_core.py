"""
policy_core.py - EHK-SCCI Policy and Decision Core Module.
"""

def review_condition(p, c, c_fn=1.0, c_fp=1.0):
    threshold_low = c / c_fn
    threshold_high = 1.0 - (c / c_fp)
    return threshold_low < p < threshold_high

def optimal_budget_allocation(dossiers, budget):
    sorted_dossiers = sorted(dossiers.items(), key=lambda x: x[1], reverse=True)
    selected = [d[0] for d in sorted_dossiers[:budget] if d[1] > 0]
    return selected

