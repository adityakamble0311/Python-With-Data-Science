class a :
    def __init__(self,name):
        self.name = name
        print("Aditya K")
class b(a):
    def __init__(self,name,lastname):
        a.__init__(self,name) #calling the constructor of parent class using'super()' function
        self.lastname=lastname
obj  = b("Aditya","Kamble")
print(obj.name,"|",obj.lastname)
