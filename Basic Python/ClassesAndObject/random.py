class atm():
    password=0
    pin=0
    id=0
    def __init__(self,name,city,baleance):
        self.id=atm.id+1
        self.name=name
        self.city=city
        self.baleance=baleance
        atm.id+=1

    def info(self):
                print('-'*30)
                print('name: ',self.name,end='\t')
                print('city: ',self.city)
                print(self.id)
                print('-'*30)
                print('Baleance: ',self.baleance,'\n\n')

    def widrow(self):
            amount=int(input('Enter the Ammount: '))
        
            if amount<self.baleance:
                self.baleance-=amount
                print('money widrow sucessful...!')
            else:
                print('amount is more then your baleance please try again')
                

    def deposite(self):
        amount=int(input('Enter the amount: '))
        self.baleance+=amount
        print('your diposite is sucessful')
Anupam=atm('Anupam','Rahata',10000)
Aditya=atm('Aditya','Shirdi',2000)
def operation(obj):
    while True:
        print('1.info \n2.widrow \n3.deposite \n4.exit')
        ch=int(input('Enter te coice : '))

        if ch==1:
            while atm.pin != atm.password:
                atm.pin=int(input('Enter Te password: '))
            if atm.pin==atm.password:
                    obj.info()
            else:
                 print('Please try aain invalid password...!')             
        elif ch==2:
            while atm.pin != atm.password:
                atm.pin=int(input('Enter Te password: '))
            if atm.pin==atm.password:
                obj.widrow()
            else:
                 print('Please try aain invalid password...!')
        elif ch==3:
            while atm.pin != atm.password:
                atm.pin=int(input('Enter The password: '))
            if atm.pin==atm.password:
                obj.deposite()
            else:
                 print('Please try aain invalid password...!')
        elif ch==4:
            break




def main():
    while True:
        print('1.Anupam \n2.Aditya')
        ch=int(input('Which account you want to lo in  : '))
        if ch==1:
            password=int(input('Create password: '))
            atm.password=password
            operation(Anupam)
        elif ch==2:
            password=int(input('Create password: '))
            atm.password=password
            operation(Aditya)
        else:
            break
main()