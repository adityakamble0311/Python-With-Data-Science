import pandas as pd 
# d = {'Aditya':['OOP','DSA','CG'],'Mohit':['CG','Python','C'],'Keyur':['DEL','DSA','DM']}
# data = pd.DataFrame(d)
# print(data)

# data = {'Aditya':99,'Keyur':87,'Mohit':88}
# x =  pd.Series(data)
# print(x)

# d = {'Aditya':['OOP','DSA','CG'],'Mohit':['CG','Python','C'],'Keyur':['DEL','DSA','DM']}
# data = pd.DataFrame(d,index=[0,9,8])
# print(data)

import matplotlib.pyplot as plt

# Creating a histogram
data['Age'].plot.hist(bins=20)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Creating a bar chart
category_counts = data['Category'].value_counts()
category_counts.plot(kind='bar')
plt.xlabel('Category')
plt.ylabel('Count')
plt.show()
