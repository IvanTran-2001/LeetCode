class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if len(path) == 1:
            return "/"
        
        new_path = ['/', []]
        for i in range(1, len(path)):
            if path[i] == '/':
                if new_path[-1]:
                    new_path[-1] = "".join(new_path[-1])
                    
                    if new_path[-1] == '.':
                        new_path[-1] = []
                        continue
                    elif new_path[-1] == '..':
                        if len(new_path) - 2 != 0:
                            for _ in range(4):
                                del new_path[-1]
                        else:
                            new_path[-1] = []
                            continue
                            
                    new_path.append('/')
                    new_path.append([]) 
                
            else:
                new_path[-1].append(path[i])
        
        if not(new_path[-1]) and new_path[-2] == '/':
            if len(new_path) != 2:
                del new_path[-1]
                del new_path[-1]
                new_path[-1] = "".join(new_path[-1])
            else:
                del new_path[-1]
        else:
            
            new_path[-1] = "".join(new_path[-1])
            
        if new_path[-1] == '.':
            del new_path[-1]
            del new_path[-1]
            if not new_path:
                return '/'
        elif new_path[-1] == '..':
            if len(new_path) <= 4:
                return '/'
            else: 
                del new_path[-1]
                del new_path[-1]
                del new_path[-1]
                del new_path[-1]
            
        return "".join(new_path)
        

if __name__ == "__main__":
    yes = Solution()
    string = "/.."
    print(yes.simplifyPath(string))