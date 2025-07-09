def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return 0
a=int(input("Enter a number"))
b=int(input("Enter another number"))
print(div(a,b))
b=int(input())
print(div(a,b))