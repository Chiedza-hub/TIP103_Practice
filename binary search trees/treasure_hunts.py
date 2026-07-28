from collections import deque 
'''
The mermaid princess Ariel and her pal Flounder visited a new shipwreck and found an exciting new human artifact to add to her collection. Ariel's collection of human treasures is stored in a binary search tree (BST) where each node represents a different item in her collection. Items are organized according to their names (vals) in alphabetical order in the BST.

Given the root of the binary search tree grotto and a string new_item, write a function add_treasure() that adds a new node with value new_item to the collection and returns the root of the modified tree. If a node with value new_item already exists within the tree, return the original tree unmodified. You do not need to maintain balance in the tree.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.

'''
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
    
# buinding the BST
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
         
def add_treasure(grotto, new_item):
    curr = grotto
    to_add = TreeNode(new_item)
    while curr:
        prev = curr
        if new_item < curr.val:
            curr = curr.left
        elif new_item > curr.val:
            curr = curr.right
        else: # we have a match
            return grotto
    if new_item < prev.val:
        prev.left = to_add
    else:
        prev.right = to_add
    return grotto
        

# Using build_tree() function at the top of page
values = ["Snarfblat", "Gadget", "Whatzit", "Dinglehopper", "Gizmo", None, "Whozit"]
grotto = build_tree(values)

# Using print_tree() function included at top of page
print_tree(add_treasure(grotto, "Thingamabob")) 