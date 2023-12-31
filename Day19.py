with open("day19input.txt") as f:
    lines =  [line.strip() for line in f.readlines()]
workflows=lines[:lines.index('')]
workflowDict={workflow.split('{')[0]:workflow.split('{')[1][:-1] for workflow in workflows}

parts=lines[lines.index('')+1:]
parts=[part[1:-1].split(",") for part in parts]
partDicts=[{coord.split("=")[0]:int(coord.split("=")[1]) for coord in part} for part in parts]


'a<2006:qkq,m>2090:A,rfg'
def workFlowMap(workflow,part):
    dest=""
    rules=workflow.split(',')
    for rule in rules:
        if ":" not in rule:
            dest=rule
            return dest
        else:
            condition , dest=rule.split(':')
            if ">" in condition:
                coord,value = condition.split('>')
                if part[coord]>int(value):
                    return dest
            elif "<" in condition:
                coord,value = condition.split('<')
                if part[coord]<int(value):
                    return dest
total=0
for part in partDicts:
    workflow=workflowDict['in']
    dest="in"
    while dest not in ["A","R"]:
        workflow=workflowDict[dest]
        dest=workFlowMap(workflow,part)
        
    if dest=="A":
        total += sum(part.values())
print(total)
    


    