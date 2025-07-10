class Animail:
    def navigate(self):
        pass
class Dog(Animail):
    def navigate(self):
        print("Bow Bow")
class Cat(Animail):
    def navigate(self):
        print("Mewo Mewo")
for v in [Dog(),Cat()]:
    v.navigate()