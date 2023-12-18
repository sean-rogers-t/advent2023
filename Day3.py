import re

#s="467..114.."
patternNum = r'(\d+)'
patternSpcChar = r'[^A-Za-z0-9\.\n]'
#matches = re.findall(pattern, s)
#193425, 532207, 532331
patternGear = r'\*'
sum=0
with open("day3input.txt", "r") as file:
    lines = file.readlines()
def PartNumber(lines):
    for i, line in enumerate(lines):
        nums = re.findall(patternNum, line)
        
        end = 0
        for num in nums:
            start = line[end:].find(num)+end
            end = start + len(num)
            
            if start==0:
                before=0
                after=end
            elif end==len(line):
                before=start-1
                after=len(line)-1
            else:
                before = start-1 
                after = end
            currentLine = line[before:after+1]
            prevLine = lines[i-1][before:after+1]
            nextLine = lines[i+1][before:after+1] if i+1<len(lines) else ""
            if re.search(patternSpcChar, currentLine):
                sum+=int(num)
            elif i==0:
                if re.search(patternSpcChar, nextLine):
                    sum+=int(num)
            elif i==len(lines)-1:
                if re.search(patternSpcChar, prevLine):
                    sum+=int(num)
            elif(re.search(patternSpcChar, prevLine) or re.search(patternSpcChar, nextLine)):
                sum+=int(num)
    return sum


def find_asterisks_indices(text):
    pattern = r'\*'
    return [match.start() for match in re.finditer(pattern, text)]
def GearDict(lines):
    sum=0
    gearDict={}
    for i, line in enumerate(lines):
        nums = re.findall(patternNum, line)
        
        end = 0
        for num in nums:
            start = line[end:].find(num)+end
            end = start + len(num)
            
            if start==0:
                before=0
                after=end
            elif end==len(line):
                before=start-1
                after=len(line)-1
            else:
                before = start-1 
                after = end
            currentLine = line[before:after+1]
            prevLine = lines[i-1][before:after+1]
            nextLine = lines[i+1][before:after+1] if i+1<len(lines) else ""
            prevMatch = find_asterisks_indices(prevLine)
            currMatch = find_asterisks_indices(currentLine)
            nextMatch = find_asterisks_indices(nextLine)
            for match in currMatch:
                coords = (i, match+before)
                if coords not in gearDict:
                    gearDict[coords]=[]
                    gearDict[coords].append(int(num))
                else:
                    gearDict[coords].append(int(num))
            for match in prevMatch:
                coords = (i-1, match+before)
                if coords not in gearDict:
                    gearDict[coords]=[]
                    gearDict[coords].append(int(num))
                else:
                    gearDict[coords].append(int(num))
            for match in nextMatch:
                coords = (i+1, match+before)
                if coords not in gearDict:
                    gearDict[coords]=[]
                    gearDict[coords].append(int(num))
                else:
                    gearDict[coords].append(int(num))
    for key in gearDict:
        if len(gearDict[key])>1:
            prod=1
            for num in gearDict[key]:
                prod*=num
            sum += prod 

        
    return sum
#sum=PartNumber(lines) part 1
sum=GearDict(lines) # part 2
print(sum)
