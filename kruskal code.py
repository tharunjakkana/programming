def find(parent,i):
    if parent[i] == i:
        return i
    return find(parent,parent[i])

def union(parent,rank,x,y):
    x_root=find(parent,x)
    y_root=find(parent,y)
    if rank[x_root]<rank[y_root]:
        parent[x_root]=y_root

    elif rank[x_root]>rank[y_root]:
        parent[y_root]=x_root
    else:
        parent[y_root]=x_root
        rank[x_root] += 1
    
def kruskal(graph):
    sorted_edges=sorted(graph['edges'])
    minimum_spanning_tree=[]
    parent={v:v for v in graph['vertices']}
    rank={v:0 for v in graph['vertices']}
   

    for weight,u,v in sorted_edges:
        u_parent=find(parent,u)
        v_parent=find(parent,v)
        if u_parent != v_parent:
            print("accepted...")
            minimum_spanning_tree.append((weight,u,v))
            union(parent,rank,u_parent,v_parent)
        else:
            print("Rejected...")
    return minimum_spanning_tree
            
    

graph={
    'vertices':['A','B','C','D','E','F']
    'edges':[
        (7,'A','B'),(5,'A','D'),
        (8,'B','C'),(9,'B','D'),(7,'B','E'),
        (5,'C','E')
        (6,'D','F'),
        (8,'E','F')
        ]}
mst=kruskal(graph)
print("Minimum spanning tree")
min_spanning_tree_cost=0
for edge in mst:
    print(edge)
    min_spanning_tree_cost += edge[0]
print("min_spanning_tree_cost=",min_spanning_tree_cost)
    
