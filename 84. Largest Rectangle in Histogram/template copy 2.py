from bintrees import RBTree

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        rb_Tree = RBTree()
        max_area = 0
        before = None
        
        for i, n in enumerate(heights):
            if n != before:
                key = nearest_larger(rb_Tree, n)
                
                if key:
                    max_values = remove_greater_or_equal(rb_Tree, key, i, max_area)
                    max_area = max(max_values[0], max_area)
                    if n != 0:
                        rb_Tree.insert(n, max_values[1])
                else:
                    if n != 0:
                        rb_Tree.insert(n, i)
            
            before = n
        
        for key, index in rb_Tree.items():
            max_area = max(max_area, (i + 1 - index) * key)
        
        return max_area
                
        
def remove_greater_or_equal(rb_tree, x, length, max_area):
    items_to_remove = [(key, rb_tree[key]) for key in rb_tree if key >= x]
    min_index = length
    max_area
    for key, index in items_to_remove:
        min_index = min(min_index, index)
        max_area = max((length - index) * key, max_area)
        rb_tree.discard(key)
    
    return [max_area, min_index]

def nearest_larger(rb_tree, x):
    try:
        # Get the smallest key greater than x
        successor_key = rb_tree.ceiling_key(x)
        return successor_key
    except KeyError:
        return None  # Key not found, return None





if __name__ == "__main__":
    yes = Solution()
    node = [2,2,5,6,2,3]
    print(yes.largestRectangleArea(node))

