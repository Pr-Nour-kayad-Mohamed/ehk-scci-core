import pytest
import numpy as np
from ehk_scci.spectral.discriminant_core import compute_weights, discriminant_score, calibrate_sigma_beta

def test_d1(): assert compute_weights(np.zeros((2,2))).shape == (2,2)
def test_d2(): cfg = {"kappa_nom":0.1, "phi_nom":0.4, "mu":0.5}; assert discriminant_score(np.array([0.2]), 0.5, cfg) == 0.0
def test_d3(): cfg = {"kappa_nom":0.5, "phi_nom":0.4, "mu":0.0}; assert discriminant_score(np.array([0.0]), 0.5, cfg) == pytest.approx(0.25)
def test_d4(): cfg = {"kappa_nom":0.0, "phi_nom":1.0, "mu":1.0}; assert discriminant_score(np.array([]), 0.0, cfg) == pytest.approx(1.0)
def test_d5(): s, b = calibrate_sigma_beta([1,2,3,4,5]); s > 0 and b > 0
def test_d6(): s, b = calibrate_sigma_beta([10,20,30,40,50]); assert s == pytest.approx(48.0)
def test_d7(): w = compute_weights(np.array([[0,10],[0,0]]), m0=1.0); assert w[0,1] == np.log1p(10.0)
def test_d8(): cfg = {"kappa_nom":0.2, "phi_nom":0.5, "mu":2.0}; assert discriminant_score(np.array([0.1, 0.1]), 0.3, cfg) > 0
def test_d9(): _, b = calibrate_sigma_beta([1,1,1,1,1]); assert b > 0
def test_d10(): assert isinstance(compute_weights(np.ones((3,3))), np.ndarray)
def test_d11(): cfg = {"kappa_nom":0.1, "phi_nom":0.4, "mu":0.5}; assert discriminant_score(np.array([0.15]), 0.4, cfg) == 0.0
def test_d12(): s, _ = calibrate_sigma_beta([1, 2, 3, 100], quantile=0.5); assert s == 2.5
def test_d13(): assert discriminant_score(np.array([0.0]), 0.4, {"kappa_nom":0.5, "phi_nom":0.4, "mu":1.0}) == pytest.approx(0.25)
def test_d14(): w = compute_weights(np.array([[0,0],[0,0]]), m0=1.0); assert np.all(w == 0)
def test_d15(): s, b = calibrate_sigma_beta([5, 10, 15, 20]); assert s > 0 and b > 0
def test_d16(): cfg = {"kappa_nom":0.1, "phi_nom":0.4, "mu":0.5}; assert discriminant_score(np.array([0.5]), 0.5, cfg) == 0.0
def test_d17(): assert compute_weights(np.array([[1,1],[1,1]])).shape == (2,2)

