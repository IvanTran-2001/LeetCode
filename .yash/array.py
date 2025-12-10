class Solution(object):

    def max_sum_subarray(self, arr, k):
        """
        Finds the maximum sum of any subarray of size k.
        """
        n = len(arr)
        
        # Handle edge case: array is smaller than k
        if n < k:
            return "Invalid input: Array size is smaller than k."
        
        # Calculate the sum of the first window
        current_sum = sum(arr[:k])
        max_sum = current_sum
        
        # Slide the window from the kth element to the end
        for i in range(k, n):
            # Subtract the element leaving the window and add the new element
            current_sum = current_sum - arr[i - k] + arr[i]
            
            # Update the maximum sum if the current window sum is larger
            max_sum = max(max_sum, current_sum)
            
        return max_sum

    # Example usage:
    
    
        
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 6]
    target = 6
    left, right = 0, len(arr)-1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            print(f"Pair found: ({arr[left]}, {arr[right]})")
            break
        elif current_sum < target:
            left += 1   # move left train forward
        else:
            right -= 1  # move right train backward
    
    [1,2,3,4,5]
    
    [1,3,6,10,15]
    
    def range_sum(prefix, l, r):
        if l == 0:
            return prefix[r]
        return prefix[r] - prefix[l-1]
    
    def range_sum(house_value, l, r):
        diff = r - l
        sum = 0
        
        for i in range(l + diff, r + diff + 1):
            sum += house_value[i]
            
        return sum
    
    def middleNode(head):
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow  # slow ends up at the middle
            
arr = [2, 3, 2, 4, 3, 2]
arr = [2, 3, 2, 4, 3, 2]