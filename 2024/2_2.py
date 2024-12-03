safe = 0;
numbers = []

with open("input2.txt", "r") as file:
    for line in file:
        input = line.split(" ")
        numbers.append(list(map(int, input)))

def check_safety(num, level):
    increasing = False
    if(num[1] - num[0] > 0):
        increasing = True

    for i in range(len(num) - 1):
        difference = num[i+1] - num[i]
        gap = abs(difference)

        if(gap < 1 or gap > 3 or (difference < 0 and increasing == True) or (difference > 0 and increasing == False)):
            
            level += 1        
            if level == 1:

                first_list = num[:i] + num[i+1:]
                first = check_safety(first_list, level)
                print(first_list)

                second_list = num[:i+1] + num[i+2:]
                second = check_safety(second_list, level)
                print(second_list)

                if first or second or check_safety(num[1:], level):
                    return True
                
            return False
    
    return True


for num in numbers:

    isSafe = check_safety(num, 0)

    
    if (isSafe):
        safe += 1
    else:
        print(num)

print(f"The number of reports that are safe is: {safe}")