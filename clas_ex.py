class college:
      def __init__(stud,name,age,id,city):
        stud . name = name
        stud.age=age
        stud.id=id
        stud.city=city

      def __str__(stud):
        return f"{stud.name}({stud.age})({stud.id}){stud.city}"

s1=college("Ram",23,121,"Rjpm")
print(s1)