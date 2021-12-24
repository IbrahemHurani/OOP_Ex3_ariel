import math
import unittest
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
def graph_creator():
    g = DiGraph()
    for i in range(10):
        g.add_node(i)
    g.add_edge(0, 1, 2.0)
    g.add_edge(0, 4, 1.0)
    g.add_edge(1, 0, 2.0)
    g.add_edge(1, 4, 6.0)
    g.add_edge(1, 2, 5.0)
    g.add_edge(2, 3, 3.0)
    g.add_edge(3, 1, 1.0)
    g.add_edge(4, 3,1.0)
    return g
class TestGraphAlgo(unittest.TestCase):
    def test_get_graph(self):
        g = graph_creator()
        graph=GraphAlgo(g)
        self.assertEqual(g,graph.get_graph())
    def test_shortest_path(self):
        g=graph_creator()
        graph=GraphAlgo(g)
        path=[]
        path.append(0)
        path.append(4)
        path.append(3)
        self.assertEqual((2.0,path),graph.shortest_path(0,3))
        path.remove(4)
        path.remove(3)
        path.append(1)
        path.append(2)
        self.assertEqual((7.0,path),graph.shortest_path(0,2))
        self.assertEqual((math.inf,[]),graph.shortest_path(10,15))
    def test_TSP(self):#not work
        g = graph_creator()
        graph=GraphAlgo(g)
        cities=[]
        cities.append(3)
        cities.append(0)
        cities.append(4)
        cities.append(1)
        cities.append(2)
        path=[]
        self.assertEqual(path,graph.TSP(cities))

    def test_centerPoint(self):
        g=graph_creator()
        graph=GraphAlgo(g)
        self.assertEqual((-1,0),graph.centerPoint())
if __name__ == '__main__':
    unittest.main()
