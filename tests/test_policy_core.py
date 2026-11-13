import pytest
from ehk_scci.safety.policy_core import review_condition, optimal_budget_allocation

def test_p1(): assert review_condition(0.5, 0.1) is True
def test_p2(): assert review_condition(0.01, 0.1) is False
def test_p3(): assert review_condition(0.99, 0.1) is False
def test_p4(): assert review_condition(0.5, 0.5) is False
def test_p5(): res = optimal_budget_allocation({"a": 0.5, "b": 0.8, "c": -0.1}, 2); assert res == ["b", "a"]
def test_p6(): res = optimal_budget_allocation({"a": 0.1}, 5); assert res == ["a"]
def test_p7(): res = optimal_budget_allocation({"a": -1.0, "b": -2.0}, 2); assert res == []
def test_p8(): assert review_condition(0.2, 0.1, c_fn=1.0, c_fp=1.0) is True
def test_p9(): assert review_condition(0.1, 0.1) is False
def test_p10(): assert review_condition(0.9, 0.1) is False
def test_p11(): res = optimal_budget_allocation({"x": 1.0, "y": 2.0, "z": 3.0}, 1); assert res == ["z"]
def test_p12(): assert review_condition(0.5, 0.45) is True
def test_p13(): assert review_condition(0.5, 0.55) is False
def test_p14(): res = optimal_budget_allocation({}, 2); assert res == []
def test_p15(): assert review_condition(0.3, 0.2) is True
def test_p16(): res = optimal_budget_allocation({"a": 0.2, "b": 0.2}, 1); len(res) == 1
def test_p17(): assert review_condition(0.5, 0.1, c_fn=2.0, c_fp=2.0) is True
def test_p18(): res = optimal_budget_allocation({"doc1": 0.5, "doc2": 0.3}, 0); assert res == []

