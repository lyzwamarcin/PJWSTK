__author__ = 'Marcin'
import graphviz as gv
from model import *


def render_graph(graph, filename="s8557", preview=False):

    g1 = gv.Graph(format='jpg')
    if graph.is_digraph() is True:
        g1 = gv.Digraph(format='jpg')

    for node in graph.get_vertices():
        g1.node(node.get_label())

    for edge in graph.get_edges():
        g1.edge(edge.get_vertex()[0].get_label(), edge.get_vertex()[1].get_label())
        if edge.get_direction() == EdgeDirection.both:
            g1.edge(edge.get_vertex()[1].get_label(), edge.get_vertex()[0].get_label())

    file_path = "./img/" + filename + ".gv"
    g1.render(file_path, view=preview)