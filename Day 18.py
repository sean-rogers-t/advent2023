import numpy as np

def ShoeLaceFormula(vertices):
    sum1=0
    
    for i in range(len(vertices)-1):
        sum1+=int(vertices[i][0])*int(vertices[i+1][1])-int(vertices[i+1][0])*int(vertices[i][1])
        
    sum1=0.5*np.abs(sum1)
    return sum1

directionDictionary={"R":np.array([0,1]),"D":np.array([1,0]),"L":np.array([0,-1]),"U":np.array([-1,0])}
hexDirectionDictionary={"0":np.array([0,1]),"1":np.array([1,0]),"2":np.array([0,-1]),"3":np.array([-1,0])}

with open("day18input.txt") as f:
     directions = [(directionDictionary[direction],int(distance),color.replace('(', '').replace(')', '')) for direction,distance,color in [line.strip().split() for line in f.readlines()]]

simple_directions = [(direction,distance) for direction,distance,color in directions]
hex_directions = [(hexDirectionDictionary[color[-1]],int(color[1:-1],16)) for direction,distance,color in directions]

vertices=[]
prevVertex=np.array([0,0])
vertices.append(prevVertex)

for direction,distance in hex_directions:
    vertex = prevVertex+(distance)*direction
    vertices.append(vertex)
    prevVertex=vertex
#Use shoelace formula to calculate area
area=ShoeLaceFormula(vertices)
perimeter= sum(map(lambda x: x[1], hex_directions))

#Pick's theorem
i=area-1/2*perimeter+1
#Since the perimeter is thick total area is interior area + perimeter
totalArea = i +perimeter

print(totalArea)