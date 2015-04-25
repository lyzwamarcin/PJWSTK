__author__ = 'Marcin'
from enum import Enum


class EdgeDirection(Enum):
    none = 1
    forward = 2
    backward = 3
    both = 4

    def reverse(self):
        if self == EdgeDirection.forward:
            return EdgeDirection.backward
        elif self == EdgeDirection.backward:
            return EdgeDirection.forward

        return self


class Edge:
    def __init__(self, label, vertex_1, vertex_2, direction=EdgeDirection.none, weight=0):
        self._label = label
        self._vertex_1 = vertex_1
        self._vertex_2 = vertex_2
        self._weight = weight
        self._edge_direction = direction

    def __str__(self):
        return "Edge " + self._vertex_1.get_label() + " - " + self._vertex_2.get_label() + " is " + str(
            self._edge_direction)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self._vertex_1 == other._vertex_1 \
                    and self._vertex_2 == other._vertex_2 \
                    and self._edge_direction == other._edge_direction \
                    and self._weight == other._weight \
                    and self._label == other._label:
                return True
            else:
                return False
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def get_vertex(self):
        return self._vertex_1, self._vertex_2

    def get_direction(self):
        return self._edge_direction

    def get_label(self):
        return self._label

    def get_weight(self):
        return self._weight