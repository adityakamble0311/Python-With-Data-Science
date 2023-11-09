f=open("Addi.txt",'a+')
while True:
    user = input("Enter a line :")
    if user == 'end':
         break
    f.write(user+'\n')
    print('Done!')
    f.seek(0)
    result = f.read()
    print("Content of the file".center(40,'-'))
    print(result)