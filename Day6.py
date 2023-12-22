

import re
import math
pattern = r'(\d+)'
with open("day6input.txt", "r") as file:
    lines = file.readlines()
#For Part 1
times = re.findall(pattern,lines[0].split(":")[1].strip())
distances = re.findall(pattern,lines[1].split(":")[1].strip())
# For Part 2
bigTime = lines[0].split(":")[1].strip().replace(" ","")
bigDistance = lines[1].split(":")[1].strip().replace(" ","")
# if c is charging time and T is total time of the race, the distance is
# d(t)=c*(T-c)=-c^2+T*c, optimal time is c=T/2. Note d(c)=d(T-c)
# if d0 is the best so far we want to solve d0 < (-c^2+T*c) for c
# the values of c that satisfy this are 
#                (T-sqrt(T^2+4*d0))/2 < c < (T+sqrt(T^2+4*d0))/2
# Could also do a binary search on the interval [0,T/2] to find the minimal c and then use the symmetry
def Distance(c,T):
    return -c*c+T*c
def WaysToWin(T,d0):
    alpha = ((T+pow(T*T-4*d0,0.5))/2)
    beta = ((T-pow(T*T-4*d0,0.5))/2)
    top = math.floor(alpha)
    bottom = math.ceil(beta)
    numWays = top-bottom+1-(1 if Distance(top,T)==d0 else 0)-(1 if Distance(bottom,T)==d0 else 0)
    return numWays
answer1=1
for i in range(len(times)):
    print(WaysToWin(int(times[i]),int(distances[i])))
    answer1*=WaysToWin(int(times[i]),int(distances[i]))
print(answer1)
answer2 = WaysToWin(int(bigTime),int(bigDistance))
print(answer2)