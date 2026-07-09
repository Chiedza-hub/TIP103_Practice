'''
You are analyzing the stability of protein chains, which are represented by a singly linked list where each node contains an integer stability value. The chain has an even number of nodes, and for each node i (0-indexed), its "twin" is defined as node (n-1-i), where n is the length of the linked list.

Write a function max_protein_pair_stability() that accepts the head of a linked list, and determines the maximum "twin stability sum," which is the sum of the stability values of a node and its twin.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next
        
def reversed(curr):
    prev = None
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

def max_protein_pair_stability(head):
    max_sum = float('-inf')
    tail = reversed(head)
   
    while head:
        curr_sum = tail.value + head.value
        if curr_sum > max_sum:
            max_sum = curr_sum
        tail = tail.next
        head = head.next 
    return max_sum

head1 = Node(5, Node(4, Node(2, Node(1))))
head2 = Node(4, Node(2, Node(2, Node(3))))

print(max_protein_pair_stability(head1))
print(max_protein_pair_stability(head2))