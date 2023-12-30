cache={}
# read in spring data
def numConfigs(condition,counts):

    if condition == "":
        return 1 if len(counts)==0 else 0
    if len(counts)==0:
        return 0 if "#" in condition else 1
    
    key = (condition,counts)
    if key in cache:
        return cache[key]
    result = 0

    if condition[0] in ".?":
        result += numConfigs(condition[1:],counts)
    if condition[0] in "#?":
        if counts[0]<=len(condition) and "." not in condition[:counts[0]] and (len(condition)==counts[0] or (condition[counts[0]]!="#")):
            result += numConfigs(condition[counts[0]+1:],counts[1:])
        else:
            result+=0
    cache[key]=result
    return result

with open("day12input.txt", "r") as file:
    lines = file.readlines()
lines=[line.strip() for line in lines]
sum=0
i=0

for line in lines:
    condition = line.split(" ")[0]
    #remove following line for part 1
    condition = "?".join([condition]*5)
    counts=tuple(map(int,line.split(" ")[1].split(",")))
    #remove following line for part 1
    counts = 5*counts
    result = numConfigs(condition,counts)
    print(f"Condition {i}: {condition} Counts: {counts} Result: {result}")
    i+=1
    sum+=result
print(f"Part 1: {sum}")



