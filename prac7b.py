class employee():
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
class childemployee1(employee):
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
class childemployee2(childemployee1):
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
emp1=employee('harshit',22,10000)
emp2=childemployee('arjun',25,24000)
print(emp1.age)
print(emp2.age)
print(emp2.salary)
