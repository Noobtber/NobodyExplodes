# complicatedWiresModule.py

# complicated wires module
class complicatedWires:

    def __init__(self, snEven=None, parallel=None, batteries=None):
        self.wires = []
        self.snEven = snEven
        self.parallel = parallel
        self.batteries = batteries

        self.createDecisionArray()

    def addWire(self, isRed, isBlue, isStar, isLed):
        self.wires.append(complicatedWire(isRed, isBlue, isStar, isLed))

    def returnInstructions(self):
        # 1 = Cut
        # 0 = Don't Cut
        # -1 = If Serial Number is Even
        # -2 = If Parallel
        # -3 = If 2 or more Batteries
        instructions = [] # create an empty list

        for wire in self.wires:
            instructions.append(self.decider[self.wire.isRed][self.wire.isBlue][self.wire.isStar][self.wire.isLed])

        for i in range(len(instructions)):
            if(self.snEven != None and instructions[i] == -1):
                if(self.snEven):
                    instructions[i] = 1
                else:
                    instructions[i] = 0
            if(self.parallel != None and instructions[i] == -2):
                if(self.parallel):
                    instructions[i] = 1
                else:
                    instructions[i] = 0
            if(self.batteries != None and instructions[i] == -3):
                if(self.batteries):
                    instructions[i] = 1
                else:
                    instructions[i] = 0

        return instructions

    def createDecisionArray(self):
        self.decider = [[[[0 for red in range(2)] for blue in range(2)] for star in range(2)] for led in range(2)]

        # 1 = Cut
        # 0 = Don't Cut
        # -1 = If Serial Number is Even
        # -2 = If Parallel
        # -3 = If 2 or more Batteries

        #            r  b  s  l
        self.decider[0][0][0][0] = 1
        self.decider[0][0][0][1] = 0
        self.decider[0][0][1][0] = 1
        self.decider[0][0][1][1] = -3
        self.decider[0][1][0][0] = -1
        self.decider[0][1][0][1] = -2
        self.decider[0][1][1][0] = 0
        self.decider[0][1][1][1] = -2
        self.decider[1][0][0][0] = -1
        self.decider[1][0][0][1] = -3
        self.decider[1][0][1][0] = 1
        self.decider[1][0][1][1] = -3
        self.decider[1][1][0][0] = -1
        self.decider[1][1][0][1] = -1
        self.decider[1][1][1][0] = -2
        self.decider[1][1][1][1] = 0
        



    
    
# represents an individual wire
class complicatedWire:

    def __init__(self, isRed, isBlue, isStar, isLed):
        self.isRed = isRed
        self.isBlue = isBlue
        self.isStar = isStar
        self.isLed = isLed

    #L = led on S= star R= red B = blue N= nothing