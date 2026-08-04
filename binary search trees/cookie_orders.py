'''
In your bakery, customer cookie orders are organized in a binary tree, 
where each node represents a different flavor of cookie ordered by the customers. 
You are given a 2D integer array descriptions where descriptions[i] = [parent_i, child_i, is_left_i] indicates that parent_i is the parent of child_i in a binary tree of unique flavors.
If is_left_i == 1, then child_i is the left child of parent_i.
If is_left_i == 0, then child_i is the right child of parent_i.
Construct the binary tree described by descriptions and return its root.
'''

from collections import deque 
class TreeNode:
    def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def build_cookie_tree(descriptions):
    nodes = {}
    children = set()
    
    for parent, child, is_left in descriptions:
        if parent not in nodes:
            nodes[parent] = TreeNode(parent)
        if child not in nodes:
            nodes[child] = TreeNode(child) 
        if is_left == 1:
            nodes[parent].left = nodes[child]
        else:
            nodes[parent].right = nodes[child]
        children.add(child)
        
        # root is the only node that never appears as a child
        for flavor in nodes:
            if flavor not in children:
                return nodes[flavor]
            
    return None

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)
    
    
descriptions1 = [
    ["Chocolate Chip", "Peanut Butter", 1],
    ["Chocolate Chip", "Oatmeal Raisin", 0],
    ["Peanut Butter", "Sugar", 1]
]

descriptions2 = [
    ["Ginger Snap", "Snickerdoodle", 0],
    ["Ginger Snap", "Shortbread", 1]
]

# Using print_tree() function included at top of page
print_tree(build_cookie_tree(descriptions1))
print_tree(build_cookie_tree(descriptions2))
        
        
       