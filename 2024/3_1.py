# Solution without using regex
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

while idx < len(input):
    if input[idx:idx+4] == 'mul(':
        idx += 4
        
        num1, idx = extract_number(idx, ',')
        
        if num1 is None:
            continue

        num2, idx = extract_number(idx, ')')
        
        if num2 is None:
            continue
        
        total_sum += int(num1) * int(num2)
        continue # continue so it doesn't move to the next character
    
    idx += 1

print("The sum is:", total_sum)


# Solution using Regex
import re

total_sum = 0
pattern = r"mul\((\d+),(\d+)\)"

all_matches = re.finditer(pattern, input)

for match in all_matches:
    total_sum += int(match.group(1)) * int(match.group(2))

print("The sum of the Regex solution is:", total_sum)