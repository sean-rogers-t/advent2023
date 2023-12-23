import re
pattern=r'(\d+)'

with open("day9input.txt", "r") as file:
    lines = file.readlines()
starts=[]
for line in lines:
    starts.append(list(map(int,line.strip().split())))

nextNumbers=[]
prevNumbers=[]
for start in starts:
    lastNumber=[]
    firstNumber=[]
    while any(start):
        lastNumber.append(start[-1])
        firstNumber.append(start[0])
        nextSequence=[]
        for i in range(len(start)-1):
            nextSequence.append(start[i+1]-start[i])
        start=nextSequence
    nextNumbers.append(sum(lastNumber))
    #firstNumber=firstNumber[::-1]
    firstNumber= [-1*firstNumber[i] if i%2==1 else firstNumber[i] for i in range(len(firstNumber))]
    prevNumbers.append(sum(firstNumber))
print(sum(nextNumbers))
print(sum(prevNumbers))

