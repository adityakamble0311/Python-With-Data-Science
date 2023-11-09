# 31/08/2023  Array D Funtions 

# import numpy as np 
# arr1 = np.array([1,2,3,4])
# print(arr1)                   One D array

# import numpy as np 
# arr2 = np.array([[1,2,3,4],[5,6,7,8]])
# print(arr2)                   two D array

# import numpy as np 
# arr3 = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
# print(arr3)             three d array


# import numpy as np 
# arr1 = np.array([1,2,3,4])
# for i in arr1:
#     print(i)          One d array using for loop

# import numpy as np 
# arr1 = np.array([[1,2,3,4],[5,6,7,8]])
# for i in arr1:
#     for j in i:
#         print(j)      Two D array using for loop



# import numpy as np 
# arr1 = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
# for i in arr1:
#     for j in i:
#         for h in j:
#             print(h)   Three D array using for loop 


        # Functions using array

# import numpy as np 
# arr1 = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
# # print(arr1.size)            Size of array


# import numpy as np 
# arr1 = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
# print(arr1.ndim)              check the array types

# import numpy as np 
# arr1 = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
# print(arr1)
# print(arr1.shape)      check how many use colunm and rows this array 
                        # Out put (1,3,4)
import numpy as np

arr1 = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]])
result = arr1.reshape(3, 4)
print(result)

