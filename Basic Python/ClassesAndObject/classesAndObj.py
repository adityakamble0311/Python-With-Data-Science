class  Aditya():
    id=0
    def __init__(self,name,college):
        self.id=Aditya.id=1
        self.name=name
        self.college=college
        Aditya.id+=1
    def dis(self):
        print("Ïd :",Aditya.id)
        print("Name :",self.name)
        print("College :",self.college)
obj = Aditya("Aditya","Sanjivani")
obj.dis()

obj1  = Aditya("Anupam","Sanjivani")
obj1.dis() 

obj3  = Aditya("Anupam","Sanjivani")
obj3.dis() 
