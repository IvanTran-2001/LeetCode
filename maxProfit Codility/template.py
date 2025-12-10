def solution(A):
    if not A:
        return 0
    
    new_array = []
    for i in range(1, len(A)):
        new_array.append(A[i] - A[i-1])
    
    
    maximum_val = new_array[0]
    value = 0
    
    for n in (new_array):
        
        value += n
        
        if value > maximum_val:
            maximum_val = value
            
        if value <= 0:
            value = 0
    if maximum_val < 0:
        return 0
    return maximum_val
            

if __name__ == "__main__":
    print(solution([5, 4, 3, 2, 1]))