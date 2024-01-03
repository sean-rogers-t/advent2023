example="rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
def Hash(input):
    hash=0
    for character in input:
        hash+=ord(character)
        hash*=17
        hash=hash%256
    return hash

with open("day15input.txt") as file:
    input = file.read()
sum=0
boxes = [[[], []] for _ in range(256)]
for direction in input.split(","):
    if direction[-1]=="-":
        label = direction[:-1]
        box = Hash(label)
        if label in boxes[box][0]:
            index= boxes[box][0].index(label)
            del boxes[box][0][index]
            del boxes[box][1][index]
        
    else:
        label = direction.split("=")[0]
        value = int(direction.split("=")[1])
        box = Hash(label)
        if label not in boxes[box][0]:
            boxes[box][0].append(label)
            boxes[box][1].append(value)
        else:
            boxes[box][1][boxes[box][0].index(label)]=value
    
for i in range(len(boxes)):
    for j in range(len(boxes[i][0])):
        power=(i+1)*(j+1)*boxes[i][1][j]
        sum+=power
print(sum)