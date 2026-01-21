class Payment:
    def process(self ,amount = 0):
        print(f"Amount to be paid....")

class Card(Payment):
    def process(self, amount):
        self.a = amount
        self.t = self.a * 0.03
        print(f"Amount: Rs.{amount} + Card Transaction fee 2%: Rs.{self.t}")

class Online(Payment):
    def process(self, amount):
        self.a = amount
        self.t = self.a * 0.04
        print(f"Amount: Rs.{amount} + Online Transaction fee 2%: Rs.{self.t}")

class Final(Payment):
    def process(self,amount = 0):
        print("Select transaction method")
        print("Enter pin to complete transaction!")

lst = [Payment(),Card(),Online(),Final()]
for i in lst:
    i.process(100)    


