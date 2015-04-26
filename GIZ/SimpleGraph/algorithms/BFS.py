__author__ = 'Marcin'


def bfs(graph, start):
    visited, queue = set(), [start]
    visit_order = []
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            visit_order.append(vertex.get_label())
            for edge in vertex.get_edges():
                if edge in graph.get_edges():
                    queue.extend(edge.get_vertex())

    return visit_order
