class Solution(object):

    def intersect(self, n_list):
        new_list = [0]  * len(n_list)
        
        for i, n in enumerate(n_list):
            new_list[i] = (i - n, i + n)
        
        sum = 0
        
        for i, n in enumerate(new_list):
            for j in range(i + 1, len(new_list)):
                    
                if ((new_list[j][0] >= n[0] and new_list[j][0] <= n[1])):
                    sum += 1
                    
                elif ((new_list[j][1] >= n[0] and new_list[j][1] <= n[1])):
                    sum += 1
                    
                elif new_list[j][0] <= n[0] and new_list[j][1] >= n[0]:
                    sum += 1
                    
                elif new_list[j][0] >= n[1] and new_list[j][1] <= n[1]:
                    sum += 1
        
        return sum
            

if __name__ == "__main__":
    yes = Solution()

    print(yes.intersect([1,5,2,1,4,0]))