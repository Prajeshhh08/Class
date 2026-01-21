class emp:
    def __init__(self,name,id):
        self.n = name
        self.i = id

class salary(emp):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.s = salary

class payroll(salary):
    def __init__(self, name, id, salary, bonus):
        super().__init__(name, id, salary)
        self.b = bonus

    def disp(self):
        print(f"Name: {self.n}\nEmp id: {self.i}\nSalary: RS.{self.s}\nBonus: Rs.{self.b}\nTotal: Rs.{self.s + self.b}")

s = payroll("Thanu",60,500,100)
s.disp()
        