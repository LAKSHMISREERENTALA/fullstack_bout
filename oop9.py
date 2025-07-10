class Demo:
    def show(self,a=None,b=None,c=None):
        if a and b and c:
            print("3 arg")
        elif a and b or c and b or a and c:
            print("2 arg")
        elif a or b or c:
           print("1 arg")
        else:
            print("no arg")
a=Demo()
a.show(8)
a.show(9,3,4)
a.show(3,4)