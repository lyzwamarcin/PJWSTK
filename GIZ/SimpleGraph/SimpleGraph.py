__author__ = 'Marcin'

from model import *
from utils import *


# a = Vertex('A')
# b = Vertex('B')
# c = Vertex('C')
# d = Vertex('D')
# e = Vertex('E')
#
# ab = Edge('A-B', a, b, EdgeDirection.forward)
# ac = Edge('A-C', a, c, EdgeDirection.forward)
# bd = Edge('B-D', b, d, EdgeDirection.forward)
# dc = Edge('D-C', d, c, EdgeDirection.both)
# ee = Edge('E-E', e, e, EdgeDirection.forward)
# ea = Edge('E-A', e, a, EdgeDirection.forward)

# ab = Edge('A-B', a, b)
# ac = Edge('A-C', a, c)
# bd = Edge('B-D', b, d)
# dc = Edge('D-C', d, c)
# ee = Edge('E-E', e, e)
# ea = Edge('E-A', e, a)

# g = Graph(digraph=True)
#
# g.add_vertex(a)
# g.add_vertex(b)
# g.add_vertex(c)
# g.add_vertex(d)
# g.add_vertex(e)

# ab = Edge('A->B', a, b, EdgeDirection.forward)
# ba = Edge('B->A', b, a, EdgeDirection.forward)
# g.add_edge(ab)
# g.add_edge(ba)

# g.add_edge(ab)
# g.add_edge(ac)
# g.add_edge(bd)
# g.add_edge(dc)
# g.add_edge(ee)
# g.add_edge(ea)

# v = [a, b, c, d]
# e = [ab, ac, bd, dc]

# g.print_graph()
#
# render_graph(g, preview=True, filename='g1')

# print '----------------------------------------------------------------------------------------------------'
# print 'REM EDGE: ', ba
# g.del_edge(dc)
# g.print_graph()
#
# render_graph(g, preview=True, filename='g2')

# print 'Is DiGrapth: ', g.is_digraph()
# print 'Is tree: ', g.is_tree()
# print 'Vertex A degree: ', a.degree()
# print 'Vertex A out degree: ', a.out_degree()
# print 'Vertex A in degree: ', a.in_degree()

# print '1. A-B direction: ', ab.get_direction()
# ab._edge_direction = EdgeDirection.backward
# print '2. A-B direction: ', ab.get_direction()

file = './data/input.txt'
reader = GraphReader(file, False)
graph = reader.create_graph()
graph.set_digraph(True)

graph.print_graph()
render_graph(graph, preview=True, filename='g1')

# graph.del_edge(graph.get_edges()[6])
# graph.add_edge(Edge('B-E', graph.get_vertex_by_label('B'), graph.get_vertex_by_label('E'), EdgeDirection.forward))
graph.del_vertex(graph.get_vertex_by_label('C'))
graph.print_graph()
render_graph(graph, preview=True, filename='g2')
