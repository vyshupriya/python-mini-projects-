def add(a,b):
    c=a+b
    return c
def sub(a,b):
  c=a-b
  return c
def mul(a,b):
    c=a*b
    return c
def div(a,b):
    c=a/b
    return c
n=int(input("select the option,\n1.add\n2.sub\n3.mul\n4.div"))
if n==1:
    e=int(input("enter the value:"))
    f=int(input("enter the value:"))
    x=e+f
    print("sum:",x)
elif n==2:
    e = int(input("enter the value:"))
    f = int(input("enter the value:"))
    x=e-f
    print("sub:",x)
elif n==3:
    e = int(input("enter the value:"))
    f = int(input("enter the value:"))
    x = e * f
    print("mul:", x)
elif n == 4:
    e = int(input("enter the value:"))
    f = int(input("enter the value:"))
    x = e / f
    print("div:", x)

else:
    print("no")

