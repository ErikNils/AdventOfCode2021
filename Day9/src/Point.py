class Point:
    def __init__(self, number):
        self.number = number
        self.checked = False
        
    def __repr__(self):
        return "(% s, % s)" % (self.number, self.checked)
        
    def __str__(self):
        return "(% s, % s)" % (self.number, self.checked)