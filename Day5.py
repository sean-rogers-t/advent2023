#seed numbers
# destination range start - source range start - range length

#parse input
# seeds: 79 14 55 13
import re
with open("day5input.txt", "r") as file:
    lines = file.readlines()
maxSeed=0


seeds = [int(num) for num in lines[0].split(":")[1].strip().split(" ")]
seedRanges = seeds
totalSeeds=[]

lines=lines[2:]
pattern = r'(\d+)'
maps=[]
mapping=[]
for i,line in enumerate(lines):
    if re.findall(pattern, line):
        mapping.append([int(num) for num in re.findall(pattern, line)])
    elif line.strip()=="":
        maps.append(mapping)
        mapping=[]

def createMap(mapping):
    dest=[]
    source=[]
    length=[]
    for piece in mapping:
        dest.append(piece[0])
        source.append(piece[1])
        length.append(piece[2])
    def seedMap(x):
        for i in range(len(source)):
            if x>=source[i] and x<source[i]+length[i]:
                return dest[i]+x-source[i]
        return x
    return seedMap

seedDestinations=seeds

for mapping in maps:
    seedDestinations=list(map(createMap(mapping), seedDestinations))
    
print(min(seedDestinations))

        
    