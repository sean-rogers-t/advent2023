""" broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a """
with open("day20input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

# module types, % flip flop, & conjunction, broadcast
class Module:
    def __init__(self,name,type=None):
        self.name = name
        self.type = type
        self.inputs = {}
        self.outputs = []
        self.value = 0

    def recieveSignal(self,sender,amp):
        if self.type == "%":
            if self.value == 0:
                self.value = amp
            else:
                self.value = 0

        if self.type == "&":
            if self.value == 0:
                self.value = amp
            else:
                self.value = self.value and amp

        return None
    def sendSignal(self,amp):
        signals =[]
        return signals

Modules={}
for line in lines:
    for line in lines:
        mod,outputs = line.split("->")
        outputs = [output.strip() for output in outputs.split(",")]

        if mod.strip()=="broadcaster":
            type="broadcaster"
            name = mod.strip()
            if name not in Modules:
                Modules[name] = Module(name,type)
            Modules[name].outputs = outputs
            for output in outputs:
                if output not in Modules:
                    Modules[output] = Module(output)
                Modules[output].inputs[name] = 0

        else:
            type=mod[0]
            name = mod[1:].strip()
            if name not in Modules:
                Modules[name] = Module(name,type)
            else:
                Modules[name].type = type
            Modules[name].outputs = outputs
            for output in outputs:
                if output not in Modules:
                    Modules[output] = Module(output)
                Modules[output].inputs[name] = 0
signals = [("broadcast",0)]
signalCount = 1
while signals:
    signal = signals.pop(0)
    sender,amp = signal
    
    for output in Modules[sender].outputs:
        if output in Modules:
            signals.append((output,amp))
            Modules[output].recieveSignal(sender,amp)
    signalCount += 1
    
        
        
            

print(Modules["broadcaster"].inputs)
        
