class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        my_coords = []
        my_dic = {}
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                my_dic[i,j] = 0
                if board[i][j] == word[0]:
                    my_coords.append([i,j])
        
        if not my_coords:
            return False
        
        for coord in my_coords:
            my_dic[coord[0],coord[1]] = 1
            if self.recurse(0, coord, board, word, my_dic):
                return True
            my_dic[coord[0],coord[1]] = 1
        
        return False    
    
    def recurse(self, i, coord, board, word, my_dic):
        truth_statement = False
        if board[coord[0]][coord[1]] != word[i]:
            return False
        elif i + 1 == len(word):
            return True
        else:
            if coord[0] - 1 >= 0:
                coord[0] -= 1
                if my_dic[coord[0], coord[1]] == 0:
                    my_dic[coord[0], coord[1]] = 1
                    truth_statement = self.recurse(i + 1, coord, board, word, my_dic)
                    my_dic[coord[0], coord[1]] = 0
                
                coord[0] += 1
            if coord[0] + 1 < len(board) and not truth_statement:
                coord[0] += 1
                if my_dic[coord[0], coord[1]] == 0:
                    my_dic[coord[0], coord[1]] = 1
                    truth_statement = self.recurse(i + 1, coord, board, word, my_dic)
                    my_dic[coord[0], coord[1]] = 0
                
                coord[0] -= 1
            if coord[1] - 1 >= 0 and not truth_statement:
                coord[1] -= 1
                if my_dic[coord[0], coord[1]] == 0:
                    my_dic[coord[0], coord[1]] = 1
                    truth_statement = self.recurse(i + 1, coord, board, word, my_dic)
                    my_dic[coord[0], coord[1]] = 0
                
                coord[1] += 1
            if coord[1] + 1 <= len(board[0]) and not truth_statement:
                coord[1] += 1
                if my_dic[coord[0], coord[1]] == 0:
                    my_dic[coord[0], coord[1]] = 1
                    truth_statement = self.recurse(i + 1, coord, board, word, my_dic)
                    my_dic[coord[0], coord[1]] = 0
                
                coord[1] -= 1
            
            return truth_statement
        

if __name__ == "__main__":
    yes = Solution()
    board, word = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"

    print(yes.exist(board, word))

