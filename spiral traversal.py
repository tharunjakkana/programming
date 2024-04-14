class treenode:
    def __init__(self,value):
        self.val=value
        self.left=None
        self.right=None
    def spiral_level_order(root):
        if not root:
            return []
        result=[]
        queue=deque([root])
        left_to_right=True

        while queue:
            level_size=len(queue)
            current_level=deque()

            for i in range(level_size):
                node=queue.popleft()
                if left_to_right:
                    current_level.append(node.val)
                else:
                    current_level.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(list(current_level))
            left_to_right=not left_to_right
root=treenode(1)
root.left=treenode(2)
root.right=treenode(3)
root.left.left=treenode(4)
root.left.right=treenode(5)
root.right.left=treenode(6)
root.right.right=treenode(7)

spiral_order=spiral_level_order(root)

                    
