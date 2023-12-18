
import re

def GetNumbers(line):
    pattern = r'(\d+)'
    numbers=line.split(":")
    parts= numbers[1].split("|")
    winningNumbers = set(re.findall(pattern, parts[0]))
    yourNumbers = set(re.findall(pattern, parts[1]))
    return winningNumbers, yourNumbers
def EvaluateCard(line):
    winningNumbers, yourNumbers = GetNumbers(line)
    numIntersection = len(winningNumbers.intersection(yourNumbers))
    return numIntersection

with open("day4input.txt", "r") as file:
    lines = file.readlines()
total=0
#dict for part 2
dict_num={i:1 for i in range(len(lines))}
for i,line in enumerate(lines):
    intersections=EvaluateCard(line)
    total+=int(1 * pow(2, intersections-1))
    for j in range(intersections):
        dict_num[i+j+1]+=dict_num[i]
numCards=0
for key in dict_num:
    numCards+=dict_num[key]
print(total)
print(numCards)