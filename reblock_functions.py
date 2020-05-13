from block import *
from block_group import *
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

def reblockAroundBlocks(blockmodel, block_x, block_y, block_z, reblock_x, reblock_y, reblock_z):
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
        block_group = BlockGroup(columns, blocks)
        new_block = block_group.calculateBlockValues(block_x, block_y, block_z)
        return new_block
