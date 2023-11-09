def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
my_list = input("Enter a number :")
user = [int (x) for x in my_list.split()]
bubble_sort(user)
print("The sorted list :",user)