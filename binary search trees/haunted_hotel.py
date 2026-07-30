'''
You have been working the night shift at a haunted hotel and guests have been coming to check out of rooms that you're pretty sure don't exist in the hotel... or are you imagining things? To make sure, you want to explore the entire hotel and make your own map.

Given the root of a binary tree hotel where each node represents a room in the hotel, write a function map_hotel() that returns a dictionary mapping each level of the hotel to a list with the level's room values in the order they appear on that level from left to right.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time complexity.

'''

from collections import deque

class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
        
Room = TreeNode

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

def map_hotel(hotel):
    
    level = 0
    my_map = {}
    queue = deque([[hotel]])
    
    while queue:
        rooms = queue.popleft()
        level_list = []
        level_children = []
        for i in range(len(rooms)):
            node = rooms[i]
            level_list.append(node.val)
            if node.left:
                level_children.append(node.left)
            if node.right:
                level_children.append(node.right)
        # update map and queue
        my_map[level] = level_list
        if level_children:
            queue.append(level_children)
        level += 1
    return my_map
        
        

"""
         Lobby
        /     \
       /       \
      101      102
     /   \    /   \
   201  202  203  204
   /                \ 
 301                302
"""

hotel = hotel = Room("Lobby", 
                Room(101, Room(201, Room(301)), Room(202)),
                Room(102, Room(203), Room(204, None, Room(302))))

print(map_hotel(hotel))