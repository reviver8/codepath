class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_symmetric(root):
    if not root:
        return True
    
    def sym_helper(left, right):
        if not left and not right:
            return True
        elif not left or not right:
            return False
        return (left.value == right.value) and sym_helper(left.left, right.right) and sym_helper(left.right, right.left)
    return sym_helper(root.left, root.right)

root1 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
#print(is_symmetric(root1))


def binary_tree_paths(root):
    '''
    IOCE
        input: root, a TreeNode
        output: list of all the possibile root to leaf paths
        constraints:
            make a traversal path for EACH leaf node
            how to account for traversing to all the different leaves
            limit the amount of traversals that we conduct
        example:
                1
               / \ 
              2   3      => [1->3, 1->2->5]
              \
               5
    Plan
        traverse thru all the nodes in the binary tree
        make a list of size(total_leaves)
        once we reach a leaf node add it to the path_list

        if leaf_node:
            curr_path = "..->..->..->.."
            return bst_paths_helper(curr, path_list.append(curr_path), curr_path)
        else:
            curr_path += "curr_node.value->"
            return bst_paths_helper(curr, path_list, curr_path)
    '''
    if (root == None):
        return None
    
    def path_helper(curr, path_list, curr_path):
        #if a leaf node
        if (curr.left == None and curr.right == None):
            curr_path += "{curr.value}->"
            #return path_helper(curr, path_list.append(curr_path), curr_path)
            print(curr_path)
            return path_list.append(curr_path)
        curr_path += "{curr.value}->"
        return path_helper(curr.left, path_list, curr_path) and path_helper(curr.right, path_list, curr_path)

    return path_helper(root, [], "")
    
    bst_path_root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
    print(binary_tree_paths(bst_path_root))