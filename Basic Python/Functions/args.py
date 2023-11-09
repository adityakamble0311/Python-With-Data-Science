'''
*args (Non-Keyword Arguments)
**kwargs (Keyword Arguments)

Both of these arguments are used to pass multiple values into a function. The *arg and **kw

'''

# def fun(*args):
#     for i in args:
#         print(i)
# fun("Aditya","Kamble","Shirdi")



'''
**args used 
ex first=Aditya
First is key and aditya is values

'''

# def fun(args1,**args):
#     for i,j in args.items():
#         print("%s==%s"%(i,j))
# fun("Hello",a="Aditya",m="mohit")



# def fun(*args,**kargs):
#     print("Args:",args,type(args))
#     print("kargs :",kargs,type(kargs))
# fun("Aditya","Kamble",A="Aditya",M="Mohit")