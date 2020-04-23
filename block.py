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

    def getMineralGrade(self, mineral, model):
        if model.lower() == "newman1":
            if mineral.lower() == 'mineral':
                return self.values[self.columns.index('grade')]
        elif model.lower() == 'zuck_small' or model.lower() == 'zuck_medium' or model.lower() == 'zuck_large':
            ore_tonnes = float(self.values[self.columns.index('ore_tonnes')])
            rock_tonnes = float(self.values[self.columns.index('rock_tonnes')])
            if mineral.lower() == 'ore':
                return (100 * ore_tonnes) / rock_tonnes
            elif mineral.lower() == 'rock':
                return rock_tonnes
        elif model.lower() == 'kd':
            if mineral.lower() == 'copper':
                grade = ''
                try:
                    grade = self.values[self.columns.index('CU %')]
                except:
                    grade = self.values[self.columns.index('<CU %>')]
                return grade
        elif model.lower() == 'p4hd':
            if mineral.lower() == 'copper':
                grade = ''
                try:
                    grade = self.values[self.columns.index('Cu %')]
                except:
                    grade = self.values[self.columns.index('<Cu %>')]
                return grade
            elif mineral.lower() == 'silver':
                silver_ppm = 0
                try:
                    silver_ppm = float(self.values[self.columns.index('Ag (oz/ton)')])
                except:
                    silver_ppm = float(self.values[self.columns.index('<Ag (oz/ton)>')])
                return silver_ppm / 10000
            elif mineral.lower() == 'gold':
                gold_ppm = 0
                try:
                    gold_ppm = float(self.values[self.columns.index('Au (oz/ton)')])
                except:
                    gold_ppm = float(self.values[self.columns.index('<Au (oz/ton)>')])
                return gold_ppm / 10000
        elif model.lower() == 'marvin':
            if mineral.lower() == 'copper':
                grade = ''
                try:
                    grade = self.values[self.columns.index('cu %')]
                except:
                    grade = self.values[self.columns.index('<cu %>')]
                return grade
            elif mineral.lower() == 'gold':
                gold_ppm = 0
                try:
                    gold_ppm = float(self.values[self.columns.index('<au [ppm]>')])
                except:
                    gold_ppm = float(self.values[self.columns.index('au [ppm]')])
                return gold_ppm / 10000
        elif model.lower() == 'w23':
            if mineral.lower() == 'gold':
                gold = 0.0
                try:
                    gold = float(self.values[self.columns.index('AuFA')])
                except:
                    gold = float(self.values[self.columns.index('<AuFA>')])
                return gold * 100
        elif model.lower() == 'mclaughlin_limit' or model.lower() == 'mclaughlin':
            if mineral.lower() == 'gold':
                gold_ppm = 0
                try:
                    gold_ppm = float(self.values[self.columns.index('Au(oz/ton)')])
                except:
                    gold_ppm = float(self.values[self.columns.index('<Au(oz/ton)>')])
                return gold_ppm / 10000
        return "Model or Mineral not valid"
