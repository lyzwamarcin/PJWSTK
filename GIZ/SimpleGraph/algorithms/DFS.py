__author__ = 'Marcin'
from model import *


def dfs(graph, start):
    """
    Wynikiem jest lista kolejno odwiedzanych Vertex w zaleznosci czy graph jest skierowany
    :param graph:
    :param start:
    :return: list
    """
    if graph.is_digraph():
        return dfs_d(graph, start)
    else:
        return dfs_m(graph, start)


def dfs_m(graph, start):
    visited, stack = [], [start]
    visit_order = []
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            visit_order.append(vertex.get_label())
            for edge in vertex.get_edges():
                if edge in graph.get_edges():
                    stack.extend(edge.get_vertex()) #[1]

    return visit_order


def dfs_d(graph, start):
    visited, stack = [], [start]
    visit_order = []
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            visit_order.append(vertex.get_label())
            for edge in vertex.get_edges():
                if edge in graph.get_edges() and edge.get_direction() == EdgeDirection.forward:
                    stack.append(edge.get_vertex()[1])

    return visit_order


def dfs_paths(graph, start, goal):
    """
    paths from Start to Goal using DFS
    :param graph:
    :param start:
    :param goal:
    """
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for edge in vertex.get_edges():
            if edge in graph.get_edges():
                if edge.get_vertex()[1] == goal:
                    yield path + [edge.get_vertex()[1]]
                else:
                    stack.append((edge.get_vertex()[1], path + [edge.get_vertex()[1]]))
