import numpy as np

directionDictionary={"R":np.array([0,1]),"D":np.array([1,0]),"L":np.array([0,-1]),"U":np.array([-1,0])}

with open("day18input.txt") as f:
     directions = [(directionDictionary[direction],int(distance),color.replace('(', '').replace(')', '')) for direction,distance,color in [line.strip().split() for line in f.readlines()]]

simple_directions = [(direction,distance) for direction,distance,color in directions]
vertices=[]
prevVertex=np.array([0,0])
vertices.append(prevVertex)
for direction,distance in simple_directions:
    vertex = prevVertex+(distance)*direction
    vertices.append(vertex)
    prevVertex=vertex
print([tuple(vertex) for vertex in vertices])

def ShoeLaceFormula(vertices):
    sum1=0
    for i in range(len(vertices)-1):
        sum1+=vertices[i][0]*vertices[i+1][1]-vertices[i+1][0]*vertices[i][1]
    sum1=0.5*np.abs(sum1)
    vertices=np.array(vertices)
    sum2=0.5*np.abs(np.dot(vertices[:,0],np.roll(vertices[:,1],-1))-np.dot(vertices[:,1],np.roll(vertices[:,0],-1)))
    return sum2
area=ShoeLaceFormula(vertices)
perimeter= sum(map(lambda x: x[1], simple_directions))

#Pick's theorem
i=area-1/2*perimeter+1
totalArea = i +perimeter
print(totalArea)