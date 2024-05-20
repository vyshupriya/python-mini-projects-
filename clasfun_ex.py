class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc (self):
    print("Hello my name is " , self.name ,"my age", self.age)
    


p1 = Person("RAM",22)
p1.myfunc()