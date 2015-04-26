__author__ = 'Marcin'
from Vertex import *
from Edge import *


class Graph:
    def __init__(self, digraph=False, root=None):
        self._vertices = []
        self._vertices_dict = {}
        self._edges = []
        self._edges_dict = {}
        self._root = root
        self._digraph = digraph

    def add_vertex(self, vertex):
        if not self._vertices.__contains__(vertex):
            self._vertices.append(vertex)
            self._vertices_dict[vertex.get_label()] = vertex

    def add_edge(self, edge):
        if not self._edges.__contains__(edge):
            self._edges.append(edge)
            self._edges_dict[edge.get_label()] = edge

            if edge.get_direction() == EdgeDirection.forward:
                edge.get_vertex()[0].add_edge(edge)
                edge = Edge(edge._label, edge._vertex_1, edge._vertex_2, EdgeDirection.backward)
                edge.get_vertex()[1].add_edge(edge)
            elif edge.get_direction() == EdgeDirection.backward:
                edge.get_vertex()[0].add_edge(edge)
                edge = Edge(edge._label, edge._vertex_1, edge._vertex_2, EdgeDirection.forward)
                edge.get_vertex()[1].add_edge(edge)
            elif edge.get_direction() == EdgeDirection.both or edge.get_direction() == EdgeDirection.none:
                edge.get_vertex()[0].add_edge(edge)
                edge.get_vertex()[1].add_edge(edge)

    def del_vertex(self, vertex):
        pass
        # if self._vertices.__contains__(vertex):
        #     self._vertices.remove(vertex)
        #     for edge in vertex.get_edges():
        #         print 'EDGE: ', edge
        #         if self._edges.__contains__(edge):
        #             print 'TO DELETE FROM EDGES: ', edge
        #             self._edges.remove(edge)
        #             print 'edge.get_vertex()[0]', edge.get_vertex()[0].get_label()
        #             # edge.get_vertex()[0].del_edge(edge)

    def del_edge(self, edge):
        # if self.is_digraph():
        if self._edges.__contains__(edge):
            self._edges.remove(edge)
            edge.get_vertex()[0].del_edge(edge)
            edge_tmp = Edge(edge.get_label(), edge.get_vertex()[0], edge.get_vertex()[1],
                            edge.get_direction().reverse())
            if not self._edges.__contains__(edge_tmp):
                edge.get_vertex()[1].del_edge(edge_tmp)
                # else:
                # pass

    def is_digraph(self):
        for edge in self._edges:
            if edge.get_direction() == EdgeDirection.none:
                return False

        return True and self._digraph

    def set_digraph(self, digraph):
        self._digraph = digraph

    def is_tree(self):
        return self._root is not None and self.is_digraph()

    def get_root(self):
        return self._root

    def set_root(self, root):
        self._root = root

    def get_vertices(self):
        return self._vertices

    def get_vertex_by_label(self, label):
        return self._vertices_dict[label]

    def get_edge_by_label(self, label):
        return self._edges_dict[label]

    def get_edges(self):
        return self._edges

    def print_graph(self):
        for v in self._vertices:
            print v