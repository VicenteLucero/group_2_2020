from block import *
import random

class BlockGroup:
    def __init__(self, columns, blocks):
        self.columns = columns
        self.blocks = blocks

    def checkParameters(self, parameters):
        for parameter in parameters:
            if parameter is None:
                return True
        return False

    def calculateBlockValues(self, x, y, z):
        if self.checkParameters([x, y, z]):
            return "Invalid parameters"
        new_values = []
        for column in self.columns:
            if column == "id" or column == "<id>":
                new_values.append(int(self.blocks[0].getValue(column)))
            elif column == "x" or column == "<x>":
                new_values.append(x)
            elif column == "y" or column == "<y>":
                new_values.append(y)
            elif column == "z" or column == "<z>":
                new_values.append(z)
            else:
                values = []
                masses = []
                classification = 0
                for block in self.blocks:
                    val, classification = block.getValueClassificationPair(column)
                    try:
                        values.append(int(val))
                    except:
                        try:
                            values.append(float(val))
                        except:
                            values.append(str(val))
                    mass = float(block.getValue(block.mass))
                    masses.append(mass)
                if classification == 0:
                    new_values.append(sum(values))
                elif classification == 1:
                    weighing = 0
                    total_weight = sum(masses)
                    for m in range(len(masses)):
                        weighing += (masses[m] * values[m])
                    new_values.append(weighing/total_weight)
                elif classification == 2:
                    modes = []
                    mode_max = 0
                    for v in values:
                        if values.count(v) > mode_max:
                            modes = [v]
                            mode_max = values.count(v)
                        elif values.count(v) == mode_max and v not in modes:
                            modes.append(v)
                    mode = modes[random.randint(0, len(modes) - 1)]
                    new_values.append(mode)
        return Block(self.columns, self.blocks[0].mass, self.blocks[0].minerals, new_values, self.blocks[0].classification)