import re
pattern=r'(\d+)'

with open("day9input.txt", "r") as file:
    lines = file.readlines()
starts=[]
for line in lines:
    starts.append(list(map(int,line.strip().split())))

nextNumbers=[]
for start in starts:
    lastNumber=[]
    while any(start):
        lastNumber.append(start[-1])
        nextSequence=[]
        for i in range(len(start)-1):
            nextSequence.append(start[i+1]-start[i])
        start=nextSequence
    nextNumbers.append(sum(lastNumber))
print(sum(nextNumbers))

