
import re
def IsPossible(red,green,blue,sample):
    isPossible=True
    if sample['red']>red:
        isPossible=False
    if sample['green']>green:
        isPossible=False
    if sample['blue']>blue:
        isPossible=False
    if sample['red']+sample['green']+sample['blue']>red+green+blue:
        isPossible=False
    return isPossible
def PossibleGames(red,green,blue,game):
    # Your code goes here
    pattern = r'(\d+)\s*(green|blue|red)'
    linesParts = game.split(":")
    gameNumber = linesParts[0].split(" ")[1]
    gameParts = linesParts[1].split(";")
    for sample in gameParts:
        color_numbers = {"green": 0, "blue": 0, "red": 0}
        matches = re.findall(pattern, sample)
        for num, color in matches:
            color_numbers[color] = int(num)
        possible=IsPossible(red,green,blue,color_numbers)
        if not possible:
            gameNumber=0
    return int(gameNumber)


def MinCubesPower(game):
    pattern = r'(\d+)\s*(green|blue|red)'
    linesParts = game.split(":")
    gameNumber = linesParts[0].split(" ")[1]
    gameParts = linesParts[1].split(";")
    minCubes= {"green": 0, "blue": 0, "red": 0}
    for sample in gameParts:
        #color_numbers = {"green": 0, "blue": 0, "red": 0}
        matches = re.findall(pattern, sample)
        for num, color in matches:
            if int(num)>minCubes[color]:
                minCubes[color]=int(num)
            #color_numbers[color] = int(num)
    power=1
    for color,num in minCubes.items():
        power*=num
    return power
"""
input_lines = []
while True:
    line = input()
    if line:
        input_lines.append(line)
    else:
        break
"""
file = open("day2input.txt", "r")
# The list of strings
#strings = input_lines
sum=0
for line in file:
    sum+=MinCubesPower(line)
    #sum+=PossibleGames(12,13,14,line)
print(sum)