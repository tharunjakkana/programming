class treenode:
    def __init__(self,value):
        self.val=value
        self.left=None
        self.right=None
def print_leaves(root,result):
    if root:
        print_leaves(root.left,result)
        if not root.left and not root.right:
            result.append(root.val)
        print_leaves(root.right,result)
def print_left_boundary(root,result):
    if root:
        if root.left:
            result.append(root.val)
            print_left_boundary(root.left,result)
        elif root.right:
             result.append(root.val)
             print_left_boundary(root.right,result)
def print_right_boundary(root,result):
    if root:
        if root.right:
            
            print_right_boundary(root.right,result)
            result.append(root.val)
        elif root.right:
            
            print_right_boundary(root.left,result)
            result.append(root.val)
def boundary_traversal(root):
    if not root:
        return[]
    result=[root.val]
    print_left_boundary(root.left,result)
    print_leaves(root,result)
    print_right_boundary(root.right,result)
    return result


root=treenode(20)
root.left=treenode(8)
root.right=treenode(22)
root.left.left=treenode(4)
root.left.right=treenode(12)
root.right.right=treenode(25)
root.left.right.left=treenode(10)
root.left.right.right=treenode(14)

boundary_order= boundary_traversal(root)
print("Boundary traversal of binary tree:",boundary_order)


        
                                    
