import re 
user = input("Enter a find name in the list :")
str = re.finditer(user,"Hello Aditya is good boy !!!")
for i in str:
    print(f'Starting index {i.start()} \nEnding point : {i.end()}\nValues : {i.group()}')