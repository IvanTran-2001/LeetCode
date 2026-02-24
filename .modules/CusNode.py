class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def list_to_singly_linked_list(arr):
    head = Node(arr[0])
    temp = head
    for i in range(1, len(arr)):
        head.next = Node(arr[i])
        head = head.next
        
    return temp

def print_el(head):
    while head:
        print(head.data, end='->')
        head = head.next