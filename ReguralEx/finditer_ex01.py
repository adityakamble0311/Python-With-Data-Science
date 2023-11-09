import re
str = re.finditer("Aditya","Hello Aditya is good boy !!")
for i in str:
    print(f'Starting index : {i.start()} \nEndling index : {i.end()} \nValues = {i.group()}')