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
        signals=[]
        if self.type == "%":
            
            if amp==0:
                self.value = self.value^1
                for output in self.outputs:
                    signals.append((self.name,output,self.value))

        elif self.type == "&":
            self.inputs[sender] = amp
            if 0 in self.inputs.values():
                new_amp = 1
            else:
                new_amp = 0
            for output in self.outputs:
                signals.append((self.name,output,new_amp))
        else:
            for output in self.outputs:
                signals.append((self.name,output,amp))

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
Modules["button"] = Module("button")
Modules["button"].outputs = ["broadcaster"]
highCount=0
lowCount=0
signalCount=0
i=0
for i in range(1000):
    signals = [("button","broadcaster",0)]
    signalCount+=1
    lowCount+=1
    while signals:
        signal = signals.pop(0)
        #print(signal)
        sender,reciever,amp = signal
        new_signals = Modules[reciever].recieveSignal(sender,amp)
        signals.extend(new_signals)
        signalCount += len(new_signals)
        for new_signal in new_signals:
            if new_signal[2]==0:
                lowCount+=1
            else:
                highCount+=1  
    
    
    #print(Modules['dt'].inputs)
print(signalCount, highCount, lowCount, highCount*lowCount)     



    
    
        
        
            


        
