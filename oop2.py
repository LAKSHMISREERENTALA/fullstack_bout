class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def getname(self):
        print(self.name)
    def getage(self):
        print(self.price)

s1 = Product('vivo y200 5g',23000)
s1.getname()
s1.getage()