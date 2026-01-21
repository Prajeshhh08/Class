class Stud:
    def __init__(self, name, mark = 25):
        self.n = name
        self.m=mark

class Scholarship(Stud):
    
    def __init__(self, name, mark=25):
        super().__init__(name, mark)
    def disp(self):
        if self.m > 25:
            print(f"Since ur mark is {self.m}, ur eligible for this scholarship!")
        else:
            print(f"Since ur mark is {self.m}, ur not eligible for this scholarship!")

s1 = Scholarship("Arun", 85)
s1.disp()
s2 = Scholarship("Jai")
s2.disp()