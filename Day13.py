'''
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.
'''
#function for part 1
def VerticalSymmetry(grid):
    for i in range(1,len(grid)):
        below = grid[:i][::-1]
        above = grid[i:]

        above=above[:len(below)]
        below=below[:len(above)]
        if above==below:
            return i
    return 0

#function for part 2
def VerticalSymmetrySmudge(grid):
    for i in range(1,len(grid)):
        below = grid[:i][::-1]
        above = grid[i:]

        above=above[:len(below)]
        below=below[:len(above)]
        sumDiff=0
        for j in range(len(above)):
            for k in range(len(above[0])):
                if above[j][k]!=below[j][k]:
                    sumDiff+=1
        if sumDiff==1:
            return i
    return 0
with open("day13input.txt") as file:
    lines = file.readlines()
patterns=[]
pattern=[]
for line in lines:
    if line!="\n":
        pattern.append(line.strip())
    else:
        patterns.append(pattern)
        pattern=[]
patterns.append(pattern)
sum=0
sumSmudge=0
for pattern in patterns:
    verticalValue = VerticalSymmetry(pattern)*100
    verticalValueSmudge = VerticalSymmetrySmudge(pattern)*100
    transposedPattern = [[row[i] for row in pattern] for i in range(len(pattern[0]))]
    transposedPattern = ["".join(row) for row in transposedPattern]
    horizontalValue = VerticalSymmetry(transposedPattern)
    horizontalValueSmudge = VerticalSymmetrySmudge(transposedPattern)
    sum += verticalValue+horizontalValue
    sumSmudge += verticalValueSmudge+horizontalValueSmudge
print(sum)
print(sumSmudge)

    