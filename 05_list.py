def add_num(List):
    
    sum= 0
    for num in List:
        sum+=num
    return sum



List = []


num=int(input('How many number you want to add:'))

for i in range(num):
    element = int(input('Enter element :'))
    List.append(element)

print(List)

result = add_num(List)
print(result)