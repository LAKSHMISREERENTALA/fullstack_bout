class Account:

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.__balance = 0
    def getBalance(self):
        return self.__balance
    def setBalance(self,balance):
        self.__balance += balance
acc = Account("sree",20)
print(acc.getBalance())
acc.setBalance(100)
print(acc.getBalance())


