__author__ = 'Marcin'
from model import *
import re


class GraphReader:
    def __init__(self, filename=None, stdin=True):
        self._filename = filename
        self._stdin = stdin
        self._graph = None
        self._vertex_mode = True

    def create_graph(self):
        if self._stdin is False and self._filename is not None:
            self.__build_from_file__()
        else:
            return None

        return self._graph

    def __build_from_file__(self):
        self._graph = Graph()
        # firstline = True

        with open(self._filename) as file:
            for line in file:
                # if firstline is True:
                #     if self.__parse_first_line__(line) is not None:
                #         self._graph.set_digraph(self.__parse_first_line__(line))
                #     else:
                #         self.__readline__(line)
                #     firstline = False
                #     continue
                self.__readline__(line)
            file.close()

    def __readline__(self, line):
        if bool(re.search('#', line)) is True:
            self._vertex_mode = False
            return

        values = line.split(' ')
        if self._vertex_mode is True:
            label = values[0].rstrip()
            #desc = values[1]
            vertex = Vertex(label)
            self._graph.add_vertex(vertex)
        else:
            tail = self._graph.get_vertex_by_label(values[0].rstrip())
            head = self._graph.get_vertex_by_label(values[1].rstrip())
            label = values[2].rstrip()
            weight = 0
            if len(values) == 4:
                weight = int(values[3].rstrip())

            edge = Edge(label, tail, head, EdgeDirection.forward, weight)
            self._graph.add_edge(edge)

    @staticmethod
    def __parse_first_line__(line):
        line = line.rstrip()
        m = re.match("True", line)
        if m is None:
            return None
        if m is not None and bool(m.group()) is True:
            return True
        return False