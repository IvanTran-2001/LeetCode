import time

# Function to iterate and find the number
def find_number(lst, num):
    for i in lst:
        if i:
            return True
    return False

def find_numberZeroes(lst, num):
    for i in lst:
        if i == num:
            return True
    return False

# Run multiple tests and average the results
def average_time(lst, num, runs=100):
    total_time = 0
    for _ in range(runs):
        start_time = time.time()
        find_number(lst, num)
        end_time = time.time()
        total_time += end_time - start_time
    return total_time / runs

def average_timeZeroes(lst, num, runs=100):
    total_time = 0
    for _ in range(runs):
        start_time = time.time()
        find_numberZeroes(lst, num)
        end_time = time.time()
        total_time += end_time - start_time
    return total_time / runs

# Create large lists
list1 = [None] * (10**5 - 1) + [1]
list2 = [0] * (10**5 - 1) + [1]

# Measure average time for list1
avg_time_list1 = average_time(list1, 1)

# Measure average time for list2
avg_time_list2 = average_timeZeroes(list2, 1)

print(avg_time_list1, avg_time_list2)