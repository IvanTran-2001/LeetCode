class Solution(object):
    
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        answer_array = []
        line_array = []
        i = 0
        length_counter = 0
        
        while i < len(words):
            length_counter += len(words[i])
            
            if length_counter > maxWidth:
                length_counter -= len(words[i]) + 1
                
                if len(line_array) == 2:
                    line_array[1] = [""]
                    for _ in range(maxWidth - length_counter):
                        line_array[1].append(" ")
                        
                    line_array[1] = "".join(line_array[1])
                    answer_array.append("".join(line_array))
                    line_array = []
                    length_counter = 0
                    continue
                
                left_over = maxWidth - length_counter
                add_space = left_over//(len(line_array)//2 - 1)
                left_over = left_over%(len(line_array)//2 - 1)
                j = 1
                while j < len(line_array) - 1:
                    
                    for _ in range(add_space):
                        line_array[j].append(" ")
                    
                    if left_over > 0:
                        line_array[j].append(" ")
                        left_over -= 1
                    
                    line_array[j] = "".join(line_array[j])
                    
                    j += 2
                
                del line_array[-1]
                
                answer_array.append("".join(line_array))
                
                
                line_array = []
                length_counter = 0
                
            else:
                line_array.append(words[i])
                
                if i == len(words) - 1:
                    line_array.append([""])
                    j = 1
                    while j < len(line_array) - 1:
                        line_array[j] = " "
                        j += 2
                        
                    for _ in range(maxWidth - length_counter):
                        line_array[-1].append(" ")
                    
                    line_array[-1] = "".join(line_array[-1])
                    answer_array.append("".join(line_array))
                    return answer_array
                else:
                    length_counter += 1
                    line_array.append([" "])
                    
                
                i += 1
        
        return answer_array

if __name__ == "__main__":
    yes = Solution()

    print(yes.fullJustify(["Twenty","years","from","now","you","will","be","more","disappointed","by","the","things","you","didn't","do","than","by","the","ones","you","did.","So","throw","off","the","bowlines,","Sail","away","from","the","safe","harbor.","Catch","the","trade","winds","in","your","sails.","Explore.","Dream."], 15))