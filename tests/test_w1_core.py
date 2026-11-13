"""
test_w1_core.py - Vecteurs de reference derives INDEPENDAMMENT de l'implementation
(transport lineaire resolu par programmation lineaire, valeurs rationnelles exactes).

Convention : m_x = alpha * delta_x + (1-alpha) * uniforme(voisins ouverts), alpha = 1/2.
"""
import unittest
from fractions import Fraction
from ehk_scci.curvature.w1_core import GraphMetricCore as G

def build(pairs, weights=None):
    w = weights or {}
    adj = {}
    for a, b in pairs:
        wt = Fraction(*w.get((a, b), (1, 1)))
        adj.setdefault(a, []).append((b, wt))
        adj.setdefault(b, []).append((a, wt))
    return sorted(adj), adj


class TestReferenceValues(unittest.TestCase):
    """Chaque valeur est connue a l'avance. Aucun test ne lit le resultat du code."""

    def kappa(self, pairs, u, v, alpha=Fraction(1, 2), weights=None):
        nodes, adj = build(pairs, weights)
        apsp = G.compute_all_pairs_shortest_paths(nodes, adj)
        return G.ollivier_ricci_curvature(u, v, adj, nodes, apsp, alpha)

    def test_triangle(self):
        self.assertEqual(self.kappa([("A", "B"), ("B", "C"), ("C", "A")], "A", "B"), Fraction(3, 4))

    def test_cycle4_bipartite(self):
        # C4 est biparti et pourtant de courbure POSITIVE : refute le mythe "biparti => kappa <= 0"
        self.assertEqual(self.kappa([("1", "2"), ("2", "3"), ("3", "4"), ("4", "1")], "1", "2"),
                         Fraction(1, 2))

    def test_cycle6(self):
        self.assertEqual(self.kappa([("1", "2"), ("2", "3"), ("3", "4"), ("4", "5"), ("5", "6"), ("6", "1")],
                                    "1", "2"), Fraction(0))

    def test_complete_bipartite_k22(self):
        self.assertEqual(self.kappa([("a", "x"), ("a", "y"), ("b", "x"), ("b", "y")], "a", "x"),
                         Fraction(1, 2))

    def test_complete_bipartite_k23(self):
        self.assertEqual(self.kappa([("a", "x"), ("a", "y"), ("a", "z"),
                                     ("b", "x"), ("b", "y"), ("b", "z")], "a", "x"), Fraction(1, 3))

    def test_path_boundary_and_interior(self):
        pairs = [("A", "B"), ("B", "C"), ("C", "D")]
        self.assertEqual(self.kappa(pairs, "A", "B"), Fraction(1, 2))
        self.assertEqual(self.kappa(pairs, "B", "C"), Fraction(0))

    def test_star(self):
        self.assertEqual(self.kappa([("c", "1"), ("c", "2"), ("c", "3")], "c", "1"), Fraction(1, 3))

    def test_grid3x3(self):
        pairs = [("a1", "a2"), ("a2", "a3"), ("b1", "b2"), ("b2", "b3"), ("c1", "c2"), ("c2", "c3"),
                 ("a1", "b1"), ("b1", "c1"), ("a2", "b2"), ("b2", "c2"), ("a3", "b3"), ("b3", "c3")]
        self.assertEqual(self.kappa(pairs, "a1", "a2"), Fraction(1, 6))

    def test_alpha_sensitivity(self):
        # alpha -> 1 : mesures concentrees sur u et v, d(u,v)=1 => kappa -> 0
        pairs = [("1", "2"), ("2", "3"), ("3", "4"), ("4", "1")]
        self.assertEqual(self.kappa(pairs, "1", "2", alpha=Fraction(1, 2)), Fraction(1, 2))
        self.assertEqual(self.kappa(pairs, "1", "2", alpha=Fraction(9, 10)), Fraction(1, 10))


class TestInvariants(unittest.TestCase):

    def test_w1_zero_for_identical_measures(self):
        nodes, adj = build([("A", "B"), ("B", "C"), ("C", "A")])
        apsp = G.compute_all_pairs_shortest_paths(nodes, adj)
        m = G.neighborhood_measure("A", adj, Fraction(1, 2))
        self.assertEqual(G.exact_wasserstein_1(list(m), list(m), m, m, apsp), Fraction(0))

    def test_w1_symmetry(self):
        nodes, adj = build([("a", "x"), ("a", "y"), ("a", "z"),
                            ("b", "x"), ("b", "y"), ("b", "z")])
        apsp = G.compute_all_pairs_shortest_paths(nodes, adj)
        mu = G.neighborhood_measure("a", adj, Fraction(3, 10))
        nu = G.neighborhood_measure("x", adj, Fraction(3, 10))
        self.assertEqual(G.exact_wasserstein_1(list(mu), list(nu), mu, nu, apsp),
                         G.exact_wasserstein_1(list(nu), list(mu), nu, mu, apsp))

    def test_mu_is_probability(self):
        nodes, adj = build([("c", "1"), ("c", "2"), ("c", "3")])
        for x in nodes:
            m = G.neighborhood_measure(x, adj, Fraction(1, 2))
            self.assertEqual(sum(m.values()), Fraction(1))

    def test_weighted_path_scales(self):
        # chemin pondere 2-2-2 : kappa identique au chemin unitaire (invariance d'echelle)
        pairs = [("A", "B"), ("B", "C"), ("C", "D")]
        w = {("A", "B"): (2, 1), ("B", "C"): (2, 1), ("C", "D"): (2, 1)}
        nodes, adj = build(pairs, w)
        apsp = G.compute_all_pairs_shortest_paths(nodes, adj)
        self.assertEqual(G.ollivier_ricci_curvature("A", "B", adj, nodes, apsp), Fraction(1, 2))

    def test_unweighted_equals_weighted_one(self):
        pairs = [("A", "B"), ("B", "C"), ("C", "A")]
        a = self._k(pairs, None)
        b = self._k(pairs, {(u, v): (1, 1) for u, v in pairs})
        self.assertEqual(a, b)

    def _k(self, pairs, weights):
        nodes, adj = build(pairs, weights)
        apsp = G.compute_all_pairs_shortest_paths(nodes, adj)
        return G.ollivier_ricci_curvature(pairs[0][0], pairs[0][1], adj, nodes, apsp)


if __name__ == "__main__":
    unittest.main()
