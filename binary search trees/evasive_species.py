'''
As a marine ecologist, you are worried about invasive species wreaking havoc on the local ecosystem. Given the root of a BST ecosystem where each node represents a species in a marine ecosystem, and an invasive species name, remove the species with value name from the ecosystem. Return the root of the modified ecosystem. Species are organized alphabetically in the tree by name (val).

If the node with name has two children in the tree, replace it with its inorder successor (leftmost node in its right subtree). You do not need to maintain a balanced tree.
'''

from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
        
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
    
def build_tree(values):
    if not values:
        return None
    def get_key_value(item):
        if isinstance(item, tuple):
            return item[0], item[1]
        else:
            return None, item
    key, value = get_key_value(values[0])
    root = TreeNode(value, key)
    queue = deque([root])
    index = 1
    while queue:
        node = queue.popleft()
        if index < len(values) and values[index] is not None:
            left_key, left_value = get_key_value(values[index])
            node.left = TreeNode(left_value, left_key)
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            right_key, right_value = get_key_value(values[index])
            node.right = TreeNode(right_value, right_key)
            queue.append(node.right)
        index += 1
    return root
         
def remove_species(ecosystem, name):
    curr = ecosystem
    prev = None
    while curr:
        if name < curr.val:
            prev = curr
            curr = curr.left
        elif name > curr.val:
            prev = curr
            curr = curr.right
        else:
            break # we have the node to remove

    # if the name is not part of the tree
    if not curr:
        return ecosystem
    
    # find replacement
    replacement = None
    if curr.left and curr.right:
        # we need the leftmost node in the right subtree
        replacement = curr.right
        rep_prev = curr
        while replacement.left:
            rep_prev = replacement
            replacement = replacement.left
        if replacement is not curr.right:
            rep_prev.left = replacement.right
            replacement.right = curr.right
        replacement.left = curr.left
    elif not curr.right:
        replacement = curr.left
    elif not curr.left:
        replacement = curr.right
    #else no children
        
    #Adjust tree
    if prev is None:
        return replacement
    if prev.left == curr:
            prev.left = replacement
    elif prev.right == curr:
            prev.right = replacement
    return ecosystem
    
    
# Use build_tree() function at top of page
values = ["Dugong", "Brain Coral", "Lionfish", None, "Clownfish", "Giant Clam", "Seagrass"]
ecosystem = build_tree(values)
# Using print_tree() function at top of page
print_tree(remove_species(ecosystem, "Lionfish"))