'''
Python Task  

Date 06/07/2023


'''




# s = "Aditya Kamble"
# print(len(s))

# l = [1,2,4,4,2]
# res=1
# for i in l:
#     res+=i
# print(res)


# l = [6,4,3,1222,12,24,54,65,32,446,456]
# s = sorted(l)
# print(s)
# print(s[-1])

def char (String="goggle.com"):
    count={}
    for c in String:
        if c in count:
            count[c]+=1
        else :
            count[c]=1
    return count
result = char () 
print(result)