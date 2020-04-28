from block import *

def emptyblocks(x_index, y_index, z_index):
    new_blocks = []
    for i in range(0, x_index-1):
        new_blocks[i] = []
        for j in range(0, y_index-1):
            new_blocks[i][j] = []
            for k in range(0, z_index-1):
                new_blocks[i][j][k] = None
    return new_blocks


def reblockArroundBlocks(blockmodel, block_x, block_y, block_z, reblock_x, reblock_y, reblock_z):
    columns = blockmodel.columns
    blocks = []
    for x in range(block_x, (block_x + reblock_x -1)):
        for y in range(block_y, (block_y + reblock_y -1)):
            for z in range(block_z, (block_z + reblock_z -1)):
                current_block = blockmodel.getBlock(x, y, z)
                if current_block != "Block does not exist":
                    blocks.append(current_block)
    if len(blocks) == 1:
        return blocks[0]
    else:
        new_block = newBlockValues(columns, blocks, block_x, block_y, block_z)
        return new_block


def newBlockValues(columns, blocks, x, y, z):
    # new_values = [x, y, z]
    # value_int = 0
    # value_string = []
    # string_column = False
    # for c in columns[3:]:
    #    for b in blocks:
    #        t_value = Block.getValue(b, c)
    #        try:
    #            value_int += int(t_value)
    #        except AttributeError:
    #            string_column = True
    #            value_string.append(t_value)
    #    if string_column:
    #        new_values.append(t_value)
    #    else:
    #        new_values.append(t_value)
    #    string_column = False
    # new_block = Block(columns, new_values)
    # return new_block
    return 0
