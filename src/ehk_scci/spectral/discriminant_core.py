"""
discriminant_core.py - EHK-SCCI Spectral and Discriminant Core Module.
Implements weight computation, discriminant scores, and robust calibration.
"""
import numpy as np

def compute_weights(W, m0=1.0):
    """Computes edge weights based on adjacency matrix and reference mass m0."""
    M = W + W.T
    return np.log1p(M / m0)

def discriminant_score(kappa_arr, phi, cfg):
    """Computes the geometric and spectral discriminant score."""
    kappa_nom = cfg.get("kappa_nom", 0.10)
    phi_nom = cfg.get("phi_nom", 0.40)
    mu = cfg.get("mu", 0.5)
    
    term_c = np.mean(np.maximum(0.0, kappa_nom - kappa_arr) ** 2) if len(kappa_arr) > 0 else 0.0
    term_p = mu * max(0.0, phi_nom - phi) ** 2
    return float(term_c + term_p)

def calibrate_sigma_beta(scores, quantile=0.95):
    """Performs robust quantile-based calibration and IQR scaling."""
    arr = np.array(scores)
    sigma_c = float(np.percentile(arr, quantile * 100))
    q75, q25 = np.percentile(arr, [75, 25])
    iqr = q75 - q25
    beta = float(1.349 / max(iqr, 1e-5)) if iqr > 0 else 8.0
    return sigma_c, beta
