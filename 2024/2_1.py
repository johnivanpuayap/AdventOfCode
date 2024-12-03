safe = 0;
numbers = []

with open("input2.txt", "r") as file:
    for line in file:
        input = line.split(" ")
        numbers.append(list(map(int, input)))


for num in numbers:
    
    isSafe = True;
    increasing = False
    if(num[1] - num[0] > 0):
        increasing = True

    for i in range(len(num) - 1):
        difference = num[i+1] - num[i]
        gap = abs(difference)
        if((difference < 0 and increasing == True) or (difference > 0 and increasing == False) or gap < 1 or gap > 3):
            isSafe = False;
            break    

    if (isSafe):
        safe += 1
            

print(f"The number of reports that are safe is: {safe}")