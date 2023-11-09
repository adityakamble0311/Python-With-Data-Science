li = [1,2,3,4,5,6,7,7,8,9]
unique = [item for item in li if li.count(item)>1]
print (f'Duplicate value in the list :',unique)