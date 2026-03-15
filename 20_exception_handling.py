num1 = int(input('Enter your Num1 :'))
num2 = int(input('Enter your Num2 :'))

try:
    result= num1/num2
except ZeroDivisionError as e :
    print("can't divided by zero")
except Exception as e :
    print("Some error have occured")
else:
    print(round(result,1))
finally:
    print('Congratulation')