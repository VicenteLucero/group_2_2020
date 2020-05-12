from block_flyweight import BlockFlyweight

class BlockFlyweightFactory:
    def __init__(self):
        self.block_flyweight_map = {}

    def create_flyweight(self, columns, mass, minerals, values, classification):
        h = hash((frozenset(columns), mass, frozenset(minerals), frozenset(values), frozenset(classification)))
        if h not in self.block_flyweight_map:
            self.block_flyweight_map[h] = BlockFlyweight(columns, mass, minerals, values, classification)

        return self.block_flyweight_map[h]
