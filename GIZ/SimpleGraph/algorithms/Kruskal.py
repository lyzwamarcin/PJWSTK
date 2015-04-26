__author__ = 'Marcin'
from model import *

parent = dict()
rank = dict()


def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0


def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]


def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1


def kruskal(graph):
    for vertice in graph.get_vertices():
        make_set(vertice)

    minimum_spanning_tree = []
    edges = list(graph.get_edges())
    edges.sort(key=lambda e: e.get_weight())
    for edge in edges:
        weight, vertice1, vertice2 = edge.get_weight(), edge.get_vertex()[0], edge.get_vertex()[1]
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.append(edge)
    return minimum_spanning_tree