from functools import reduce
import math
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


with open("day8input.txt", "r") as file:
    lines = file.readlines()
instructions=[x for x in lines[0].strip()]
directionBinary={"L":0,"R":1}
instructions=[directionBinary[x] for x in instructions]
i=2
coordinates ={}
for i in range(2,len(lines)):
    coordinate= lines[i].split("=")[0].strip()
    left, right = lines[i].split("=")[1].strip()[1:-1].strip().split(",")
    right = right.strip()

    coordinates[coordinate]=[left,right]
    

numInstructions = len(instructions)
# Part 1
""" start="AAA"
while start!="ZZZ":
    nextmove=instructions[i%numInstructions]
    if nextmove==0:
        start=coordinates[start][0]
    else:
        start=coordinates[start][1]
    i+=1
    
print(i) """
# Part 2
starts=[x for x in coordinates.keys() if x[-1]=="A"]
times=[]
for start in starts:
    i=0
    while start[-1]!="Z":
        nextmove=instructions[i%numInstructions]
        if nextmove==0:
            start=coordinates[start][0]
        else:
            start=coordinates[start][1]
        i+=1
    times.append(i)
answer = reduce(lcm, times)
print(answer)