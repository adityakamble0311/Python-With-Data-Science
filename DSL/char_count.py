word = "ADITYA KAMBLE SHIRDI"
char_count={}
for char in word:
    if char in char_count:
        char_count[char]+=1
    else:
        char_count[char]=1
for char,count in char_count.items():
    print(f'The Character {char} : {count} Times is use in the word')