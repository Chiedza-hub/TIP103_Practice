from collections import deque

'''
In your bakery, each cookie order is represented by a binary tree where each node contains the number of cookies of a particular type. The cookie combo for any node is defined as the total number of cookies in the entire subtree rooted at that node (including that node itself).

Given the root of a cookie order tree, return an array of the most frequent cookie combo in your bakery's orders. If there is a tie, return all the most frequent combos in any order.
'''
class TreeNode:
    def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

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

def get_combos_rec(root, combos):
        if not root:
            return
        if not root.left and not root.right:
            combos[root.val] = combos.get(root.val, 0) + 1
            return root.val
        total = root.val + get_combos_rec(root.left, combos) + get_combos_rec(root.right, combos)
        combos[total] = combos.get(total, 0) + 1
        return total
    
def most_popular_cookie_combo(root):
    combos = {}
    get_combos_rec(root, combos)
    result = []
    max_freq = max(combos.values())
    for total, freq in combos.items():
        if freq == max_freq:
            result.append(total)
    return result
        

"""
       5
      / \
     2  -3
"""
cookies1 = TreeNode(5, TreeNode(2), TreeNode(-3))

"""
       5
      / \
     2  -5
"""
cookies2 = TreeNode(5, TreeNode(2), TreeNode(-5))

print(most_popular_cookie_combo(cookies1))  
print(most_popular_cookie_combo(cookies2))  
        
       