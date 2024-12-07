def is_possible(target, nums, current=0, index=0):
    # Base Case: If we have considered all numbers
    if index == len(nums):
        return current == target

    # Get the current number
    num = nums[index]

    # Explore both '+' and '*' operations
    add_result = is_possible(target, nums, current + num, index + 1)
    multiply_result = is_possible(target, nums, current * num, index + 1)

    # Return True if any path gives the target
    return add_result or multiply_result

# Read the input file and parse the data
input_data = dict()

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
        print(f"Target {key} can be formed from {value}")
        total_sum += key

print(f"Total sum of possible targets: {total_sum}")        