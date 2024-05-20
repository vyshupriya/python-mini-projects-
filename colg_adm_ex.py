fmc2023=("RAM","RAVI")
a=int(input("FMC COLLEGE ADMISSION PROCESS,\n1.NEW STUDENTS NAME ADDED"
      "\n2.STUDENTS IN A LIST"
      "\n3.STUDENTS TOTAL IN B.COM"
      "\n4.CHANGE THE STUDENTS NAME"
      "\n5. ODER THE STUDENTS NAME"
      "\n6.NEW STUDENTS ADDED"
      "\n7.COPY THE STUDENTS NAME"
      "\n8.TOTAL STUDENTS"))
if a==1:
    n=input("enter new student name ")
    fmc20231=list(fmc2023)
    n=n.upper()
    fmc20231.append(n)
    fmc2023=tuple(fmc20231)
    print(fmc2023)
    print("name added successfully")
elif a==2:
    print(fmc2023)
elif a==3:
    print("total count",len(fmc2023))
elif a==4:
    n=input("CHANGE THE STUDENT NAME")
    fmc20231 = list(fmc2023)
    n=n.upper()
    fmc20231[1] = "RAM"
    fmc2023 = tuple(fmc20231)
    print(fmc2023)
    print("ADDED SUCCESSFULLY")
elif a==5:
    for x in fmc2023:
        print(x)
elif a==6:
    n=input("NEW STUDENT NAME")
    fmc20231=list(fmc2023)
    newlist = []
    fmc2023=tuple(fmc20231)
    print("fmc2023")
    for x in fmc2023:
        if "a" in x:
            newlist.append(x)
            print("fmc2023")
            print("added successfully")
elif a==7:
    lis2 = fmc2023.copy()
    print("The new list created is : " + str(lis2))
    lis2.append(5)
    print("The new list after adding new element : \n"+ str(lis2))
    print("The old list after adding new element to new list  : \n" + str(fmc2023))
elif a==8:
    x=fmc2023.count()
    print(x)
else:
    print("invalid")


