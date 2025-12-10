from AVLTreeMod import AVLTree

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        avl = AVLTree()
        max_area = 0
        before = None

            
        for i, n in enumerate(heights):
            if n != before:
                items = avl.keys_values_greater_than(n)
                
                if items:
                    max_values = remove_greater(avl, items, i, max_area)
                    max_area = max(max_values[0], max_area)
                    if n != 0:
                        avl.insert(n, max_values[1])
                else:
                    if n != 0:
                        avl.insert(n, i)
            
            before = n
        
        items = avl.keys_values_greater_than(0)
        if items:
            max_area = max(remove_greater(avl, items, i + 1, max_area)[0], max_area)
        
        return max_area

def remove_greater(avl, items, length, max_area):
        min_index = length
        for key, index in items:
            min_index = min(min_index, index)
            max_area = max((length - index) * key, max_area)
            avl.delete(key)
    
        return [max_area, min_index]

class AVLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def _height(self, node):
        if node is None:
            return 0
        return node.height

    def _balance_factor(self, node):
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        self._update_height(z)
        self._update_height(y)

        return y

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        self._update_height(z)
        self._update_height(y)

        return y

    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if node is None:
            return AVLNode(key, value)
        
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        else:
            node.right = self._insert(node.right, key, value)

        self._update_height(node)

        balance = self._balance_factor(node)

        # Left Heavy
        if balance > 1:
            # Left-Left Case
            if key < node.left.key:
                return self._rotate_right(node)
            # Left-Right Case
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

        # Right Heavy
        if balance < -1:
            # Right-Right Case
            if key > node.right.key:
                return self._rotate_left(node)
            # Right-Left Case
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.value = temp.value
            node.right = self._delete(node.right, temp.key)

        if node is None:
            return node

        self._update_height(node)

        balance = self._balance_factor(node)

        # Left Heavy
        if balance > 1:
            # Left-Left Case
            if self._balance_factor(node.left) >= 0:
                return self._rotate_right(node)
            # Left-Right Case
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

        # Right Heavy
        if balance < -1:
            # Right-Right Case
            if self._balance_factor(node.right) <= 0:
                return self._rotate_left(node)
            # Right-Left Case
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def next_larger_integer(self, x):
        return self._next_larger_integer_helper(self.root, x)

    def _next_larger_integer_helper(self, node, x):
        if node is None:
            return None

        if node.key <= x:
            return self._next_larger_integer_helper(node.right, x)
        else:
            left_result = self._next_larger_integer_helper(node.left, x)
            return left_result if left_result is not None else node.key

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        if node is not None:
            self._inorder_traversal(node.left, result)
            result.append((node.key, node.value))
            self._inorder_traversal(node.right, result)
    
    def keys_values_greater_than(self, x):
        key_value_list = []
        self._collect_keys_values_greater_than(self.root, x, key_value_list)
        return key_value_list

    def _collect_keys_values_greater_than(self, node, x, key_value_list):
        if node is not None:
            if node.key > x:
                self._collect_keys_values_greater_than(node.left, x, key_value_list)
                key_value_list.append((node.key, node.value))
                self._collect_keys_values_greater_than(node.right, x, key_value_list)
            elif node.key <= x:
                self._collect_keys_values_greater_than(node.right, x, key_value_list)
    
if __name__ == "__main__":
    yes = Solution()
    node = [2,2,5,6,2,3]
    
    
    print(yes.largestRectangleArea(node))

