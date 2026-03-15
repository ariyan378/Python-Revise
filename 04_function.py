def add_num(*args):
    
    sum= 0
    for num in args:
        sum+=num
    return sum


result = add_num(1,2,3,4,5)
print(result)