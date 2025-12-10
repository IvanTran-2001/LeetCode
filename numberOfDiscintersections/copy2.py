class Solution(object):
    def binary(self, index, arr, x):
        
        left, right = index, len(arr)

        while left < right:
            mid = (left + right) // 2
            if arr[mid][0] == x:
                return mid
            elif arr[mid][0] < x:
                left = mid + 1
            else:
                right = mid

        return left

    def solution(self, n_list):
        new_list = []
        track = {}
        
        for i, n in enumerate(n_list):
            new_list.append((i - n, i + n))
            
        new_list = sorted(new_list, key=lambda x: x[0])
        
        for i, n in enumerate(new_list):
            if not(n[0] in track):
                track[n[0]] = [i, i]
            else:
                if i > track[n[0]][1]:
                    track[n[0]][1] = i
            
        summary = 0
        for i in range(len(new_list) - 1):

            left = self.binary(i + 1, new_list, new_list[i][0]) 
            right = self.binary(i + 1, new_list, new_list[i][1])
            
            track[new_list[i][0]][0] += 1
                
            if new_list[left][0] in track:
                left = track[new_list[left][0]][0]

            if right < len(new_list) and new_list[right][0] <= new_list[i][1] and new_list[right][0] in track:
                right = track[new_list[right][0]][1] + 1
                
                
            summary += right - left
        
        return summary
    
if __name__ == "__main__":
    yes = Solution()
    print(yes.solution([1,5,2,1,4,0]) == 11)
    print(yes.solution([1,1,1]) == 3)
    print(yes.solution([1,1,1,2]) == 6)
    print(yes.solution([1,2,2,2]) == 6)
    print(yes.solution([1,2,3,4,5]) == 10)
    print(yes.solution([5,4,3,2,1]) == 10)