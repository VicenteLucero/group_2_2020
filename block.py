from block_flyweight_factory import BlockFlyweightFactory

class Block:
    def __init__(self, columns, mass, minerals, values, classification):
        self.flyweight = BlockFlyweightFactory().create_flyweight(columns, mass, minerals, values, classification)

    #Fix this with new parameters
    def __eq__(self, other):
        try:
            if len(self.flyweight.columns) != len(other.flyweight.columns):
                return False
            if len(self.flyweight.values) != len(other.flyweight.values):
                return False
            for list_index in range(len(self.flyweight.columns)):
                if not(self.flyweight.columns[list_index] == other.flyweight.columns[list_index]):
                    return False
                if self.flyweight.classification[list_index] == 2:
                    continue
                if not(self.flyweight.values[list_index] == other.flyweight.values[list_index]):
                    return False
            return True
        except:
            return False

    def getValue(self, column):
        try:
            return self.flyweight.values[self.flyweight.columns.index(column)]
        except:
            return "Column does not exist"

    def getMineralGrade(self, mineral):
        MINERAL_UNIT = 0
        MINERAL_COLUMN = 1
        OZ_TON_TO_GRAMS = 28.3495
        mineral_column_name = ""
        mineral_value = 0.0
        if mineral in self.flyweight.minerals.keys():
            mineral_column_name = self.flyweight.minerals[mineral][MINERAL_COLUMN]
            try:
                mineral_value = float(self.flyweight.values[self.flyweight.columns.index(mineral_column_name)])
            except:
                return "Column of the mineral does not match any of the existing columns"
            if self.flyweight.minerals[mineral][MINERAL_UNIT] == "%":
                return mineral_value
            elif self.flyweight.minerals[mineral][MINERAL_UNIT] == "oz/ton":
                return mineral_value * OZ_TON_TO_GRAMS / 10000
            elif self.flyweight.minerals[mineral][MINERAL_UNIT] == "ppm":
                return float(mineral_value) / 10000
            elif self.flyweight.minerals[mineral][MINERAL_UNIT] == "tonn":
                return 100 * float(mineral_value) / float(self.flyweight.values[self.flyweight.columns.index(self.flyweight.mass)])
            else:
                return "Unit of meassurement not recognised"           
        else:
            return "Mineral does not exist in this model"

    def getValueClassificationPair(self, column):
        try:
            column_index = self.flyweight.columns.index(column)
            return self.flyweight.values[column_index], self.flyweight.classification[column_index]
        except:
            return "Column does not exist"
