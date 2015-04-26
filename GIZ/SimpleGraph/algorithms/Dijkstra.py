__author__ = 'Marcin'
from model import *

def dijkstra(graph, start):
    import sys
    S = set()
    Q = dict((v, v) for v in graph.get_vertices())
    d = {}
    p = {}
    for v in graph.get_vertices():
        d[v] = sys.maxint
        p[v] = None
    d[start] = 0
    p[start] = start

    while Q:
        d_tmp = dict((key, d[key]) for key in d.keys() if key not in S)
        (u, u_cost) = min(d_tmp.items(), key=lambda x: x[1])
        S.add(u)
        del(Q[u])
        for edge in u.get_edges():
            if edge in graph.get_edges(): #and edge.get_direction() == EdgeDirection.forward:
                w = edge.get_vertex()[1]
                if w not in Q:
                    continue
                if d[w] > d[u] + edge.get_weight():
                    d[w] = d[u] + edge.get_weight()
                    p[w] = u
    return d, p


def dijkstra_shortest_path(graph, start, end):
    d, p = dijkstra(graph, start)
    path = [end]

    while path[-1] is not start:
        edge = p[end]
        path.append(edge)
        end = edge
    path.reverse()
    return path