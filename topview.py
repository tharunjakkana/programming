class node:
    def __init__(self,d):
        self.l=None
        self.r=None
        self.hd=0
def constructtree(nodelist):
    root=node(nodelist[0])
    root.l=node(nodelist[1])
    root.r=node(nodelist[2])
    root.l.l=node(nodelist[3])
    root.l.r=node(nodelist[4])
    root.r.l=node(nodelist[5])
    root.r.r=node(nodelist[6])
    return root
def topview(root):
    m={}
    q=[]
    q=[root]
    while len(q)>0:
        curr_node=q.pop(0)
        if curr_node.hd not in m:
            m[curr_node.hd]=curr_node.hd
        if curr_node.l:
            curr_node.l.hd=curr_node.hd-1
            q.append(curr_node.l)
        if curr_node.r:
            curr_node.l.hd=curr_node.hd+1 
            q.append(curr_node.r)
    m=sorted(m)
    print("Topview")
    for k,v in m.item():
        print(v,end=",")
nodelist=['A','B','C','D','E','F','G']
root=constructtree(nodelist)
topview(root)
    
