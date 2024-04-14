from collections import deque
class treenode:
    def __init__(self,value):
        self.val=value
        self.left=None
        self.right=None
    def reverse_level_order(root):
        if not root:
            return []
        result=[]
        
        

        while queue:
            level_size=len(queue)
            current_level=[]

            for i in range(level_size):
                node=queue.popleft()
                current_level.append(node.val)
               
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.insert(0,current_level)
        return result
    
root=treenode(1)
root.left=treenode(2)
root.right=treenode(3)
root.left.left=treenode(4)
root.left.right=treenode(5)
root.right.left=treenode(6)
root.right.right=treenode(7)

reverse_order=reverse_level_order(root)
print("Reverse level order traversal:")
for i in reverse_order:
    print(level)

                    
