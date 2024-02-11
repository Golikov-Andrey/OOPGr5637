class Places:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.empty = False


    def isEmpty(self):
        return self.empty

    def setEmpty(self, empty):
        result = self.empty
        self.empty = empty
        return result

    def getRow(self):
        return self.row

    def setRow(self, row):
        self.row = row

    def getCol(self):
        return self.col

    def setCol(self, col):
        self.col = col