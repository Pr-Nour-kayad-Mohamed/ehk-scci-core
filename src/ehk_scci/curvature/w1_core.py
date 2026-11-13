"""
w1_core.py - Noyau geometrique exact, zero dependance externe.
Transport optimal (Wasserstein-1) resolu par flot a cout minimal exact
(chemins augmentants de Bellman-Ford sur graphe residuel), masses mises
a l'echelle entiere pour supprimer toute erreur d'arrondi.
"""
from fractions import Fraction
from collections import deque
from math import gcd
from typing import Dict, List, Tuple

INF = Fraction(10**18, 1)


def _lcm(a: int, b: int) -> int:
    return a // gcd(a, b) * b


class GraphMetricCore:

    @staticmethod
    def spfa_shortest_paths(nodes: List[str],
                            edges: Dict[str, List[Tuple[str, Fraction]]],
                            source: str) -> Dict[str, Fraction]:
        """Distances exactes depuis source. INF si non atteignable."""
        dist = {n: INF for n in nodes}
        dist[source] = Fraction(0, 1)
        in_q = {n: False for n in nodes}
        q = deque([source])
        in_q[source] = True
        while q:
            u = q.popleft()
            in_q[u] = False
            for v, w in edges.get(u, []):
                if dist[u] >= INF:
                    continue
                nd = dist[u] + w
                if nd < dist[v]:
                    dist[v] = nd
                    if not in_q[v]:
                        q.append(v)
                        in_q[v] = True
        return dist

    @classmethod
    def compute_all_pairs_shortest_paths(cls, nodes, edges):
        return {n: cls.spfa_shortest_paths(nodes, edges, n) for n in nodes}

    @staticmethod
    def neighborhood_measure(x: str, edges, alpha: Fraction) -> Dict[str, Fraction]:
        """m_x = alpha * delta_x + (1-alpha) * uniforme sur les voisins ouverts."""
        nb = [n for n, _ in edges.get(x, [])]
        m = {x: alpha}
        if nb:
            share = (Fraction(1, 1) - alpha) / len(nb)
            for n in nb:
                m[n] = m.get(n, Fraction(0, 1)) + share
        else:
            m[x] = Fraction(1, 1)
        return m

    @staticmethod
    def exact_wasserstein_1(supp_u, supp_v, mu, nu, dist_matrix) -> Fraction:
        """
        W1 exact entre deux mesures rationnelles de meme masse totale.
        Flot a cout minimal : chemins augmentants de Bellman-Ford sur le
        graphe residuel, capacites entieres apres mise a l'echelle.
        """
        su = [x for x in supp_u if mu.get(x, Fraction(0, 1)) > 0]
        sv = [y for y in supp_v if nu.get(y, Fraction(0, 1)) > 0]

        base = 1
        for x in su:
            base = _lcm(base, mu[x].denominator)
        for y in sv:
            base = _lcm(base, nu[y].denominator)

        supply = {x: int(mu[x] * base) for x in su}
        demand = {y: int(nu[y] * base) for y in sv}
        if sum(supply.values()) != sum(demand.values()):
            raise ValueError("Masses totales inegales : transport impossible.")

        S, T = "__S__", "__T__"
        nodes = [S, T] + su + sv
        graph = {n: [] for n in nodes}

        def add_edge(a, b, cap, cost):
            graph[a].append([b, cap, cost, len(graph[b])])
            graph[b].append([a, 0, -cost, len(graph[a]) - 1])

        for x in su:
            add_edge(S, x, supply[x], Fraction(0, 1))
        for y in sv:
            add_edge(y, T, demand[y], Fraction(0, 1))
        for x in su:
            for y in sv:
                d = dist_matrix[x][y]
                if d < INF:
                    add_edge(x, y, min(supply[x], demand[y]), d)

        total_cost = Fraction(0, 1)
        sent = 0
        target = sum(supply.values())

        while sent < target:
            dist = {n: INF for n in nodes}
            prev = {}
            dist[S] = Fraction(0, 1)
            for _ in range(len(nodes) - 1):
                changed = False
                for a in nodes:
                    if dist[a] >= INF:
                        continue
                    for idx, (b, cap, cost, _rev) in enumerate(graph[a]):
                        if cap > 0 and dist[a] + cost < dist[b]:
                            dist[b] = dist[a] + cost
                            prev[b] = (a, idx)
                            changed = True
                if not changed:
                    break

            if T not in prev:
                raise ValueError("Flot impossible : graphe de transport deconnecte.")

            bottleneck = target - sent
            node = T
            while node != S:
                a, idx = prev[node]
                bottleneck = min(bottleneck, graph[a][idx][1])
                node = a

            node = T
            while node != S:
                a, idx = prev[node]
                arc = graph[a][idx]
                arc[1] -= bottleneck
                graph[node][arc[3]][1] += bottleneck
                total_cost += bottleneck * arc[2]
                node = a
            sent += bottleneck

        return total_cost / base

    @classmethod
    def ollivier_ricci_curvature(cls, u: str, v: str, edges, nodes, apsp,
                                 alpha: Fraction = Fraction(1, 2)) -> Fraction:
        """kappa(u,v) = 1 - W1(m_u, m_v) / d(u,v)."""
        if u == v:
            return Fraction(1, 1)
        d_uv = apsp[u].get(v, INF)
        if d_uv == 0 or d_uv >= INF:
            raise ValueError("Noeuds non adjacents ou non connectes : distance nulle ou infinie.")

        mu = cls.neighborhood_measure(u, edges, alpha)
        nu = cls.neighborhood_measure(v, edges, alpha)
        w1 = cls.exact_wasserstein_1(list(mu), list(nu), mu, nu, apsp)
        return Fraction(1, 1) - w1 / d_uv

    @classmethod
    def curvature_all_edges(cls, nodes, edges, alpha=Fraction(1, 2)):
        """Courbure sur chaque arete non orientee, une seule passe APSP."""
        apsp = cls.compute_all_pairs_shortest_paths(nodes, edges)
        seen, out = set(), {}
        for u in nodes:
            for v, _w in edges.get(u, []):
                key = tuple(sorted((u, v)))
                if key in seen:
                    continue
                seen.add(key)
                out[(u, v)] = cls.ollivier_ricci_curvature(u, v, edges, nodes, apsp, alpha)
        return out
