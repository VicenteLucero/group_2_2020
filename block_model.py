from reblock_functions import *


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
            try:  
                x_index = current_block.columns.index("x") 
                y_index = current_block.columns.index("y") 
                z_index = current_block.columns.index("z") 
                if int(current_block.values[x_index]) == X and int(current_block.values[y_index]) == Y and int(current_block.values[z_index]) == Z:
                    return current_block
            except:
                x_index = current_block.columns.index("<x>") 
                y_index = current_block.columns.index("<y>") 
                z_index = current_block.columns.index("<z>") 
                if int(current_block.values[x_index]) == X and int(current_block.values[y_index]) == Y and int(current_block.values[z_index]) == Z:
                    return current_block
        return "Block does not exist"

    def reBlock(self, rx, ry, rz):
        new_x = len(self.blocks) / rx
        new_y = 0
        if not new_x == new_y:
            new_y = len(self.blocks[0]) / ry
        new_z = 0
        if not new_y == new_z:
            new_z = len(self.blocks[0][0]) / rz

        new_blocks = emptyblocks(new_x, new_y, new_z)

        count_x = 0
        count_y = 0
        count_z = 0
        for i in range(0, len(self.blocks)-1, rx):
            count_y = 0
            for j in range(0, len(self.blocks[0])-1, ry):
                count_z = 0
                for k in range(0, len(self.blocks[0][0])-1, rz):
                    new_blocks[count_x][count_y][count_z] = reblockArroundBlocks(self, i, j, k, rx, ry, rz)
                    count_z += 1
                count_y += 1
            count_x += 1
        return new_blocks


