class BlockModel:
    def __init__(self, columns, blocks):
        self.columns = columns
        self.blocks = blocks

    def __eq__(self, other):
        try:
            if len(self.blocks) != len(other.blocks):
                return False
            if len(self.columns) != len(other.columns):
                return False
            for n in range(len(self.columns)):
                if not(self.columns[n] == other.columns[n]):
                    return False
            for i in range(len(self.blocks)):
                if not(self.blocks[i].__eq__(other.blocks[i])):
                    return False
            return True
        except:
            return False

    def getBlock(self, X, Y, Z):
        for i in range(len(self.blocks)):
            current_block = self.blocks[i]
            if current_block.values[current_block.columns.index("X")] == X and current_block.values[current_block.columns.index("Y")] == Y and current_block.values[current_block.columns.index("Z")] == Z:
                return current_block
        return "Block does not exist"