class Marks:
    def __init__(self):
        self.mark=[]
    def addMark(self,mark):
        self.mark.append(mark)
    def getMark(self):
        return self.mark
s1=Marks()
s1.addMark(100)
s1.addMark(90)
s1.addMark(80)
s1.addMark(70)
print(s1.getMark())
