from block import *
import random

def invalidParameters(parameters):
    for parameter in parameters:
        if parameter is None:
            return True
    return False

def emptyblocks(x_index, y_index, z_index):
    if invalidParameters([x_index, y_index, z_index]):
        return "Invalid parameters"
    new_blocks = []
    for i in range(0, x_index):
        new_blocks.append([])
        for j in range(0, y_index):
            new_blocks[i].append([])
            for k in range(0, z_index):
                new_blocks[i][j].append(None)
    return new_blocks

def newBlockValues(columns, blocks, x, y, z):
    if invalidParameters([columns, blocks, x, y, z]):
        return "Invalid parameters"
    new_values = []
    for column in columns:
        if column == "id" or column == "<id>":
            new_values.append(int(blocks[0].getValue(column)))
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
            for block in blocks:
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
                #print(values, sum(values))
            elif classification == 1:
                weighing = 0
                total_weight = sum(masses)
                for m in range(len(masses)):
                    weighing += (masses[m] * values[m])
                new_values.append(weighing/total_weight)
                #print(masses, weighing/total_weight)
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
                #print(mode)
    return Block(columns, blocks[0].mass, blocks[0].minerals, new_values, blocks[0].classification)

def reblockArroundBlocks(blockmodel, block_x, block_y, block_z, reblock_x, reblock_y, reblock_z):
    if invalidParameters([blockmodel, block_x, block_y, block_z, reblock_x, reblock_y, reblock_z]):
        return "Invalid parameters"
    columns = blockmodel.columns
    blocks = []
    for x in range(block_x, (block_x + reblock_x)):
        for y in range(block_y, (block_y + reblock_y)):
            for z in range(block_z, (block_z + reblock_z)):
                current_block = blockmodel.getBlock(x, y, z)
                if current_block != "Block does not exist":
                    blocks.append(current_block)
    if len(blocks) == 1:
        return blocks[0]
    elif len(blocks) > 1:
        new_block = newBlockValues(columns, blocks, block_x, block_y, block_z)
        return new_block
