from abc import ABC, abstractmethod

class Appliance(ABC):
    @abstractmethod
    def switch(self, button):
        pass
class Fridge(Appliance):
    def switch(self, button):
        print(f"Switching {button} to fridge")
class Washingmachine(Appliance):
    def switch(self, button):
        print(f"Switching {button} to washing machine")
a = Fridge()
a.switch("on")
b = Washingmachine()
b.switch("off")
