class Category:
    def __init__(self, name):
        self.n = name

class Price:
    def __init__(self, price):
        self.p = price

    def tax(self):
        return self.p * 0.03

class Item(Category, Price):
    def __init__(self, name,  price, weight):
        Category.__init__(self, name )
        Price.__init__(self, price)
        self.w = weight

    def disp(self):
        total = self.p + self.tax()
        print(f"Item: {self.n}")
        print(f"Weight: {self.w}kg")
        print(f"Price: Rs.{self.p:.2f} + Tax: Rs.{self.tax():.2f}")
        print(f"Total: Rs.{total}")

apple = Item(" Apple", 250, 0.5)
apple.disp()