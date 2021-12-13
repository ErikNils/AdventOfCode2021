class Octopus:
    def __init__(self, number):
        self.number = number
        self.flash = False
        
    def __repr__(self):
        return "(% s, % s)" % (self.number, self.flash)
        
    def __str__(self):
        return "(% s, % s)" % (self.number, self.flash)