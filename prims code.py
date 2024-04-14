import heapq
def prim(graph,start):
    minimum_spanning_tree=[]
    visited=set()
    heap=[(0,start)]
    while heap:
        weight,vertex=heapq.heappop(heap)
        if vertex not in visited:
            visited.add(vertex)
            minimum_spanning_tree.append((weight,vertex))
            for neighbour,neighbour_weight in graph[vertex]:
                if neighbour not in visited:
                    heapq.heappush(heap,(neighbour_weight,neighbour))
    return minimum_spanning_tree

no_nodes=int(input("Enter no of nodes: "))
graph={chr(i+65):[]for i in range(no_nodes)}

for key in graph.keys():
    no_neighbours=int(input("No of neighbours of {key} "))
    while no_neighbours>0:
        neighbour_tuple=input("Enter w and neighbour").split()
        neighbour_tuple[0]=int(neighbour_tuple[0])
        graph[key].append((neighbour_tuple[0],neighbour_tuple[1]))
        no_neighbours -= 1
start_vertex='A'
print(graph)
mst=prim(graph,start_vertex)
print("MST:",mst)
print("Minimum Spanning Tree :")
min_spanning_tree_cost=0
for weight,vertex in mst:
    min_spanning_tree_cost += weight
print("min_spanning_tree_cost=",min_spanning_tree_cost) 
    

