class Block:
    def __init__(self, columns, values):
        self.columns = columns
        self.values = values

    def __eq__(self, other):
        try:
            if len(self.columns) != len(other.columns):
                return False
            if len(self.values) != len(other.values):
                return False
            for i in range(len(self.columns)):
                if not(self.columns[i] == other.columns[i]):
                    return False
                if not(self.values[i] == other.values[i]):
                    return False
            return True
        except:
            return False

    def getValue(self, column):
        try:
            return self.values[self.columns.index(column)]
        except:
            return "Column does not exist"