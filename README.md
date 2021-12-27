assignment for weighted directed graph:
![image](https://user-images.githubusercontent.com/86603326/147368829-54ef74ed-bdd5-452e-95d1-e2efc3327bfd.png)

an introduction for my algorthim:

my algorthim implements the weighted directed graph in python the important important classes in my algorthim:
* class Node:in the class implement the information for node the id and location in the graph and weight.
* class DiGraph: this class implements GraphInterface the function implements in this class 
```python
1.def v_size(self) -> int:#this function return the size of nodes in the graph
2.def e_size(self) -> int:#this function return the size of edge in the graph
3.def get_all_v(self) -> dict:#this function return all the nodes in the graph
4.def all_in_edges_of_node(self, id1: int) -> dict:#this funtion return all the in edges for signal node
5.def all_out_edges_of_node(self, id1: int) -> dict:#this function return all the out edge for signal node
6.def get_mc(self) -> int:#this function  Returns the current version of this graph,on every change in the graph state 
7.def add_edge(self, id1: int, id2: int, weight: float) -> bool:#this fucntion to add edge form node to another node in the garph
8.def add_node(self, node_id: int, pos: tuple = None) -> bool:#this function to add node in the graph
9.def remove_node(self, node_id: int) -> bool:#this funtion to reomve node in the graph
10.def remove_edge(self, node_id1: int, node_id2: int) -> bool:#this function to remove edge in the graph
``` 

* class GraphAlgo:this class implements GraphAlgoInterface the function implements in this class
```python
1.def get_graph(self) -> GraphInterface:#this function return the graph
2.def load_from_json(self, file_name: str) -> bool:#this function for read the file json and input in the graph
3.def save_to_json(self, file_name: str) -> bool:#this function to save the file json
4.def shortest_path(self, id1: int, id2: int) -> (float, list):#this function return the short path form node to another node in the graph for another information can visit https://en.wikipedia.org/wiki/Shortest_path_problem
5.def centerPoint(self) -> (int, float):#this function return the center of the graph for another information for graph center can visit:https://en.wikipedia.org/wiki/Graph_center 
6.def plot_graph(self) -> None:#this function to draw all the graph and this function working with matplotlib.pyplot library in python
7.def TSP(self, node_lst: List[int]) -> (List[int], float):#this functio Finds the shortest path that visits all the nodes in the list for another information can visti:https://en.wikipedia.org/wiki/Travelling_salesman_problem
``` 
* class main:this class for compile the code and this class have four function to check if all the classes work perfect.

# compare time between java and python:
|Name Function|Node numbers with averge edge for node in/out|       Java   |   python  |
|-------------|---------------------------------------------|--------------|-----------|
|shortestpath |  100 Nodes and averges 20 edges for one node|    100 ms    |    110 ms |
|center       |  100 Nodes and averges 20 edges for one node|    47 ms     |7 sec 88ms | 
|Tsp          |  100 Nodes and averges 20 edges for one node|    31 ms     | 80 ms     |


|Name Function|Node numbers with averge edge for node in/out |    Java     |    python          |
|-------------|----------------------------------------------|-------------|--------------------|
|shortestpath |  1000 Nodes and averges 20 edges for one node|    256 ms   |        270 ms      |   
|center       |  1000 Nodes and averges 20 edges for one node|    890 ms   | bigger than 1 min  |
|Tsp          |  1000 Nodes and averges 20 edges for one node|    250 ms   |         320 ms     |

|Name Function|Node numbers with averge edge for node in/out  |     java          |     python          |
|-------------|-----------------------------------------------|-------------------|---------------------|
|shortestpath |  10000 Nodes and averges 20 edges for one node|    3 sec 343ms    | 4 sec 109ms         |
|center       |  10000 Nodes and averges 20 edges for one node|    1 min          | bigger than 3 min   |
|Tsp          |  10000 Nodes and averges 20 edges for one node|    14 sec 420 ms  | 16 sec 990 ms       |

for function load and save i take test on A3,A4,A5 it's take time for 15-30 ms in python 
in java take save take 100-250 ms and load take 30-60 ms

# UML diagram algorithm:
![image](https://user-images.githubusercontent.com/86603326/147405112-f47c5377-ad53-4986-b5a5-c13a4f9c5aea.png)




