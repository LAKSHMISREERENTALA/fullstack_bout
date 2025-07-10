from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
class UPIPayment(Payment):
    def pay(self,amount):
        print(f"Paid: {amount} via UPI")
upi=UPIPayment()
upi.pay(100)