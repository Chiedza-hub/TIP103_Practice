from collections import deque 
'''
Given the root of a binary tree where each node's value represents a certain number of cookies, 
return the number of unique paths from the root to a leaf node where the total number of cookies equals a given target_sum.
'''
class TreeNode:
    def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def count_cookie_paths(root, target_sum):
    
    return count_cookie_paths_rec(root, target_sum, 0)

def count_cookie_paths_rec(root, target_sum, curr_sum):
    
    if not root:
        return 0
    curr_sum += root.val
    if not root.left and not root.right:
        return 1 if curr_sum == target_sum else 0
    
    return count_cookie_paths_rec(root.left, target_sum, curr_sum) + count_cookie_paths_rec(root.right, target_sum, curr_sum)
   
    


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

"""
    10
   /  \
  5     8
 / \   / \
3   7 12  4
"""
# Using build_tree() function included at the top of the page
cookie_nums = [10, 5, 8, 3, 7, 12, 4]
cookies1 = build_tree(cookie_nums)

"""
    8
   / \
  4   12
 / \    \
2   6    10
"""
cookie_nums = [8, 4, 12, 2, 6, None, 10]
cookies2 = build_tree(cookie_nums)

print(count_cookie_paths(cookies1, 22)) 
print(count_cookie_paths(cookies2, 14)) 
