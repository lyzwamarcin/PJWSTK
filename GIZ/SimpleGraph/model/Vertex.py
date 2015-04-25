__author__ = 'Marcin'
from Edge import EdgeDirection


class Vertex:

    def __init__(self, label):
        self._label = label
        self._edges = []

        self._visited = False
        self._visit_count = 0

    def add_edge(self, edge):
        if not self._edges.__contains__(edge):
            self._edges.append(edge)

    def __str__(self):
        return "Vertex: '" + self._label + "' has Edges: \n\t" + ",\n\t".join(str(e) for e in self._edges) + "\n"

    def __repr__(self):
        return self.__str__()

    def _count_edges_(self, edge_direction=EdgeDirection.none):
        if edge_direction == EdgeDirection.none or edge_direction == EdgeDirection.both:
            return self._edges.__len__()
        else:
            deg = 0
            for edge in self._edges:
                if edge.get_direction() == edge_direction:
                    deg += 1

            return deg

    def get_label(self):
        return self._label

    def in_degree(self):
        return self._count_edges_(EdgeDirection.backward)

    def out_degree(self):
        return self._count_edges_(EdgeDirection.forward)

    def degree(self):
        return self._edges.__len__()

    def del_edge(self, edge):
        if self._edges.__contains__(edge):
            self._edges.remove(edge)

    def get_edges(self):
        return self._edges