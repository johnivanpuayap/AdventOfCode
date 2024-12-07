import time

def is_possible(target, nums, current=0, index=0, prev_num=None):
    
    if index == len(nums):
        return current == target
    
    if current > target:
        return False

    # Get the current number
    num = nums[index]

    concat = None
    concat_result = False

    if (index == 1):
        concat = int(str(prev_num) + str(num))
        concat_result = is_possible(target, nums, concat, index + 1, num)
    elif (index > 1):
        concat = int(str(current) + str(num))
        concat_result = is_possible(target, nums, concat, index + 1, num)
        
    add_result = is_possible(target, nums, current + num, index + 1, num)
    multiply_result = is_possible(target, nums, current * num, index + 1, num)

    return add_result or multiply_result or concat_result

# Start the timer
start_time = time.time()

input_data = dict()

# Read input data
with open('input7.txt', 'r') as file:
    for line in file.readlines():
        data = line.split(': ')
        split_data = data[1].split(' ') 
        int_data = [int(i) for i in split_data]
        input_data[int(data[0])] = int_data

# Loop through the input dictionary and check if it's possible to form the target
total_sum = 0
for key, value in input_data.items():
    if is_possible(key, value):
        total_sum += key

# Print the total sum
print(f"Total sum of possible targets: {total_sum}")

# Stop the timer
end_time = time.time()

# Calculate elapsed time
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.4f} seconds")