class Bingo_Number:
    def __init__(self, number):
        self.number = number
        self.bingo = False
        
    def __repr__(self):
        return "(% s, % s)" % (self.number, self.bingo)
        
    def __str__(self):
        return "(% s, % s)" % (self.number, self.bingo)