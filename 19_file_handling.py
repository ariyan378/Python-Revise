with open("sample.txt", 'w+') as file:
    data = 'Hello world\n'
    file.write(data)
    
    file.seek(0)          
    
    line = file.readline()
    print(line)           