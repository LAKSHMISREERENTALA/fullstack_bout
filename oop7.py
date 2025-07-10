class vehicle:
    def navigate(self):
        pass
class Bussinessure(vehicle):
    def navigate(self):
        print("navigate via vechile")
class car(vehicle):
    def navigate(self):
        print("navigate via car")
class bicycle(vehicle):
    def navigate(self):
        print("navigate via bicycle")
for v in [car(),bicycle()]:
    v.navigate()
