from collections import deque
class treenode:
    def __init__(self,value):
        self.val=value
        self.left=None
        self.right=None
    def diagonal_traversal(root):
        if not root:
            return []
        result=[]
        queue=deque([(root,0)])
        

        while queue:
            node,level=queue.popleft
            if level == len(result):
                result.append([])
            result[level].append(node.val)
            if node.left:
                queue.append((node.left,level+1))
            if node.right:
                queue.append((node.right,level))
        return result
    
root=treenode(1)
root.left=treenode(2)
root.right=treenode(3)
root.left.left=treenode(4)
root.left.right=treenode(5)
root.right.left=treenode(6)
root.right.right=treenode(7)

diagonal_order=diagonal_traversal(root)
print("diagonal traversal of the binary tree:")
for i in diagonal_order:
    print(level)

                    
