import getopt
import sys

__author__ = 'Marcin'

from model import *
from utils import *
from algorithms import *


def main(argv):
    file_name = './data/dijkstra/d_1.in'
    opts, args = getopt.getopt(argv, "hi:", ["infile="])
    for opt, arg in opts:
        if opt == '-h':
            print 'SimpleGraph.py -i <inputfile> '
            sys.exit()
        elif opt in ("-i", "--ifile"):
            file_name = arg


    graph = Graph(True)
    reader = GraphReader(file_name, False, graph)
    graph = reader.create_graph()

    graph.print_graph()
    render_graph(graph, preview=True, filename='g1')

    mst = kruskal(graph)
    print str(mst)

if __name__ == "__main__":
    main(sys.argv[1:])

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

# file = './data/dfs/dfs_3.in'
# graph = Graph(True)
# reader = GraphReader(file, False, graph)
# graph = reader.create_graph()
#
# graph.print_graph()
# render_graph(graph, preview=True, filename='g1')

# kruskal(graph)

# d = dijkstra(graph, graph.get_vertex_by_label('0'))
# p = dijkstra_shortest_path(graph, graph.get_vertex_by_label('0'), graph.get_vertex_by_label('3'))
# print str(p)
# dfs_m = dfs(graph, graph.get_vertex_by_label('A'))
# print 'DFS', dfs_m
#
# bfs = bfs(graph, graph.get_vertex_by_label('A'))
# print 'BFS', bfs
# path = dfs_paths(graph, graph.get_vertex_by_label('A'), graph.get_vertex_by_label('F'))
# print list(path)
#
# dfr_r = dfs_r(graph, graph.get_vertex_by_label('A'))
# print dfs_r

# print '----------------------------------------------------------------------------------------------------'
# graph.del_edge(graph.get_edges()[0])
# graph.del_edge(graph.get_edges()[0])
# graph.del_edge(graph.get_edges()[3])
# graph.add_edge(Edge('B-E', graph.get_vertex_by_label('B'), graph.get_vertex_by_label('E'), EdgeDirection.forward))
# graph.del_vertex(graph.get_vertex_by_label('A'))
# graph.print_graph()
# render_graph(graph, preview=True, filename='g2')

# print dfs_paths(graph, graph.get_vertex_by_label('A'), graph.get_vertex_by_label('F'))
