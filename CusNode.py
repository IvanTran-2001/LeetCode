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


# ── Binary Tree ──────────────────────────────────────────────────────────────

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


def list_to_binary_tree(arr):
    """Convert a LeetCode-style level-order list into a binary tree.

    None values in the list represent missing nodes, matching LeetCode's
    serialisation format exactly.

    Example:
        [3, 9, 20, None, None, 15, 7]  →
              3
             / \\
            9  20
               / \\
              15   7
    """
    if not arr or arr[0] is None:
        return None

    from collections import deque

    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1

    while queue and i < len(arr):
        node = queue.popleft()

        # left child
        if i < len(arr):
            if arr[i] is not None:
                node.left = TreeNode(arr[i])
                queue.append(node.left)
            i += 1

        # right child
        if i < len(arr):
            if arr[i] is not None:
                node.right = TreeNode(arr[i])
                queue.append(node.right)
            i += 1

    return root


def binary_tree_to_list(root):
    """Serialize a binary tree back to a LeetCode-style level-order list."""
    if not root:
        return []

    from collections import deque

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

    # Strip trailing None values
    while result and result[-1] is None:
        result.pop()

    return result


def print_binary_tree(root, prefix="", is_left=True):
    """Pretty-print a binary tree to the console."""
    if root is None:
        return
    if root.right:
        print_binary_tree(root.right, prefix + ("│   " if is_left else "    "), False)
    print(prefix + ("└── " if is_left else "┌── ") + str(root.val))
    if root.left:
        print_binary_tree(root.left, prefix + ("    " if is_left else "│   "), True)