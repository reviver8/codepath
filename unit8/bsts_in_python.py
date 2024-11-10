class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# def print_tree(TreeNode root):
#     sol"
#     while 
def check_tree(root):
    '''
    ioce:
        input: root of tree
        output: boolean indicating whether the root.value
                is equal to the value of sum(left.value, right.value)
        constraints:
            we are using a BST
            the tree has exactly 3 nodes, 1 root and 2 children from the root
        examples:
              10
             / \        => True
            4   6
    Plan
        return root.value == root.left.value + root.right.value
                             sum(root.left.value, root.right.value)
        '''
    #sol = root.right.value + root.left.value
    return root.val == root.left.val + root.right.val

def check_tree_3(root):
    '''
    IOCE
        input:root of tree
        output: bool indicating whether root.val == sum(children.val)
        constraints:
            it is not guaranteed whether the root will have 1 child or 2 children
            if there are 2 children, it will be root.left and root.right
        examples:
             5                        5
            / \\   => True          /    => False
           3   2                   3

    Plan
       iterate throughout the tree recursively and save the current children sum
        return root.val == sum(children.val) 
    '''
    children_sum = 0
    #check if left child exists
    if root.left:
        children_sum += root.left.val
    #check if right child exists
    if root.right:
        children_sum += root.right.val
    return root.val == children_sum

def left_most(root):
    if root is None:
        return None
    
    curr = root
    while curr.left:
        curr = curr.left
    return curr.val

def left_most_recur(root):
    if root is None:
        return None
    if root.left is None:
        return root.val
    return left_most_recur(root.left)

def inorder_traversal(root):
    return inorder_helper(root, [])
        
def inorder_helper(curr, lst):
    if curr:
        inorder_helper(curr.left, lst)
        lst.append(curr.val)
        inorder_helper(curr.right, lst)
    return lst

def bt_size(root):
    return len(inorder_traversal(root))
# def children_sum(curr):
#     if curr is None:
#         return 0
#     left_sum, right_sum = 0, 0
#     if curr.left:
#         left_sum = children_sum(curr)
#     if curr.right:
#         right_sum = children_sum(curr)
#     return curr.value + children_sum(curr)


root1 = TreeNode(10, TreeNode(4), TreeNode(6))
#root = Constructor(value, Constructor(value), Constructor(value))
#root = TreeNode(val, root.left(val), root.right(val))
#node1 = TreeNode(10)
#node2 = TreeNode(4)
#node1.left = node2
root2 = TreeNode(5, TreeNode(3), TreeNode(1))
root3 = TreeNode(5, TreeNode(2))
root4 = TreeNode(6, None, TreeNode(6))
root5 = TreeNode(10, TreeNode(10), None)
root6 = TreeNode(4, root2, root3)
root_ultimate = TreeNode(32, root3, root6)

# check first check_tree method
# print(check_tree(root1))

# check 2nd check_tree method
# print(check_tree_3(root2), check_tree_3(root3))
# print(check_tree_3(root4), check_tree_3(root5))

# check left_most method
# print(left_most(root2), left_most(root6))
# print(left_most_recur(root_ultimate))

# check inorder_traversal method
# print(inorder_traversal(root6))

# check size() method
# print(bt_size(root6))
# print(bt_size(root4))

