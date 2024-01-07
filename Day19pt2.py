with open("day19input.txt") as f:
    lines =  [line.strip() for line in f.readlines()]
workflows=lines[:lines.index('')]
workflowDict={workflow.split('{')[0]:workflow.split('{')[1][:-1] for workflow in workflows}


#a<2006:qkq,m>2090:A,rfg
#in{s>2573:cff,ljt}'
#intervals=[[(0,4000)],[(0,4000)],[(0,4000)],[(0,4000)]]'
def workFlowMap(workflow,volumes):
    nextIntervals=[]
    rules=workflow.split(',')
    currentVolumes=volumes.copy()
    for rule in rules:
        if ":" not in rule:
            dest=rule
            nextIntervals.append((dest,currentVolumes))
        else:
            condition , dest = rule.split(':')
            if ">" in condition:
                coord,value = condition.split('>')
                value=int(value)
                new_intervals=currentVolumes.copy()
                interval= currentVolumes[coord]
                if interval[0] < value < interval[1]:
                    new_intervals[coord]=[value+1,interval[1]]
                    currentVolumes[coord]=[interval[0],value]
                nextIntervals.append((dest,new_intervals))

            elif "<" in condition:
                coord,value = condition.split('<')
                value=int(value)
                new_intervals=currentVolumes.copy()
                interval= currentVolumes[coord]
                if interval[0] < value < interval[1]:
                    new_intervals[coord]=[interval[0],value-1]
                    currentVolumes[coord]=[value,interval[1]]
                nextIntervals.append((dest,new_intervals))
    return nextIntervals
totalA=0
totalR=0
A=[]
R=[]
intervals={"x":[1,4000],"m":[1,4000],"a":[1,4000],"s":[1,4000]}
workflowIntervals = [("in",intervals)]
while len(workflowIntervals)>0:
    workflow,intervals = workflowIntervals.pop(0)
    nextIntervals=workFlowMap(workflowDict[workflow],intervals)
    for interval in nextIntervals:
        if interval[0]=="A":
            A.append(interval[1])
        elif interval[0]=="R":
            R.append(interval[1])
        else:
            workflowIntervals.append(interval)
for interval in A:
    total=1
    total*=interval["x"][1]-interval["x"][0]+1
    total*=interval["m"][1]-interval["m"][0]+1
    total*=interval["a"][1]-interval["a"][0]+1
    total*=interval["s"][1]-interval["s"][0]+1
    totalA+=total
for interval in R:
    total=1
    total*=interval["x"][1]-interval["x"][0]+1
    total*=interval["m"][1]-interval["m"][0]+1
    total*=interval["a"][1]-interval["a"][0]+1
    total*=interval["s"][1]-interval["s"][0]+1
    totalR+=total

print(totalA)