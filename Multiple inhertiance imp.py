class product:
    def __init__(self):
        print("------PSG STORES-----")
        print("*****MENU*****")
        print("1.Apple         Rs.50")
        print("2.Mango         Rs.40")
        print("3.Orange        Rs.45")
        print("4.Strawberry    Rs.90")
        k=int(input("Enter the no of products:"))
        self.lst=[]
        self.lst1=[]
        for i in range (k):
            self.lst.append(int(input("Enter the product:")))
            self.lst1.append(int(input("Enter the quantity:")))

class customer:
    def __init__(self,name,id):
        self.n = name
        self.d = id

class order(product,customer):
    def __init__(self,name,id):
        product.__init__(self)
        customer.__init__(self,name,id)
        self.amt = 0
        print(f"Customer: {self.n}\nID: {self.d}")
        for i,j in zip(self.lst,self.lst1):
            if i == 1:
                self.p = 50*j
                self.amt+=self.p
                print(f"Product: Apple\tQuantity: {j}\nTotal: {self.p}")
            elif i == 2:
                self.p = 40*j
                self.amt+=self.p
                print(f"Product: Mango\tQuantity: {j}\nTotal: {self.p}")
            elif i == 3:
                self.p = 45*j
                self.amt+=self.p
                print(f"Product: Orange\tQuantity: {j}\nTotal: {self.p}")
            elif i == 4:
                self.p = 90*j
                self.amt+=self.p
                print(f"Product: Apple\tQuantity: {j}\nTotal: {self.p}")

        print(f"Final amount:{self.amt}")

k = input("Enter name :")
l = int(input("Enter id :"))
s = order(k,l)



                

