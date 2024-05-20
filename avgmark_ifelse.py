a=int(input("ENTER THE TAMIL MARK:"))
b=int(input ("ENTER THE ENGLISH MARK:"))
c=int(input("ENTER THE MATHS MARK:"))
d=int(input("ENTER THE SCIENCE MARK:"))
e=int(input("ENTER THE SOCIAL MARK:"))
marks=a+b+c+d+e
print("TOTAL",marks)
avg=marks/5
print("TOTAL MARK AVERAGE:",avg)
if avg>90:
    print("A GRADE")
elif avg>80:
    print("B GRADE")
elif avg>70:
    print("C GRADE")
elif avg>60:
    print("D GRADE")
elif avg>50:
    print("E GRADE")
else:
    print("FAIL")




