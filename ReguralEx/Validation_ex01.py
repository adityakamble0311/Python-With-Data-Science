import re
text = 'ABCDEFGIJKLMNOPQUVWXYZabcdefghijklmnopquvwxyz@#$%^&*0123456789'
matches = re.finditer('[^A-Z]', text)
for match in matches:
    if match:
        print(f'Starting index :{match.start()} Ending index :{match.end()} Values = {match.group()}')
        print("Success")
    else:
        print("Not Found")
