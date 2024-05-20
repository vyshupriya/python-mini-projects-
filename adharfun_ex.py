class Aathar:
    def __init__(self,Name,Age,Fathername,DOB,Sex):
        self.Name=Name
        self.Age=Age
        self.Fathername=Fathername
        self.DOB=DOB
        self.Sex=Sex


    def myid (self):
        print("Name :",self.Name)
        print("Age: ",self.Age)
        print("Fathername:",self.Fathername)
        print("DOB:",self.DOB)
        print("Sex:",self.Sex)



a1=Aathar("vaishnavi",32,"Balasubaramaniyan",1991,"Female")
a1.myid()

