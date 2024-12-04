
with open("input3.txt", "r") as file:
    input = file.read()

def extract_number(idx, delimiter):
    num = ''
    while idx < len(input) and input[idx] != delimiter:
        if input[idx].isdigit():
            num += input[idx]
        else:
            return None, idx
        idx += 1
    
    return (num, idx + 1) if num else (None, idx)

idx = 0
total_sum = 0
enabled = True

while idx < len(input):

    if input[idx:idx+4] == 'do()':
        enabled = True
        idx += 4
        continue

    if input[idx:idx+7] == "don't()":
        enabled = False
        idx += 7
        continue
    
    
    if enabled and input[idx:idx+4] == 'mul(':
        idx += 4  # Move past 'mul('
        
        # Extract first number
        num1, idx = extract_number(idx, ',')
        
        if num1 is None:  # Invalid number
            continue

        # Extract second number
        num2, idx = extract_number(idx, ')')
        
        if num2 is None:  # Invalid number
            continue
        
        total_sum += int(num1) * int(num2)
        continue # continue so it doesn't move to the next character
    
    idx += 1

print("The sum is:", total_sum)