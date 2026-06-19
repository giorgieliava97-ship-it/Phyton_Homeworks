# დავალება ა
body_weight = int(input('Please enter your bodyweight: '))
height = float(input('Please enter your height: '))
BMI = body_weight / height ** 2

# print('Your BMI is ', BMI)

# if BMI < 19:
#     print('You are underweight')
# if BMI > 19 and BMI < 25:
#     print('You are normalweight')
# if BMI > 25:
#     print('You are overweight')

if BMI < 19:
    print('You are underweight')

elif BMI >= 19 and BMI <= 25:
    print('You are normalweight')
    
else:
    print('You are overweight')

# _____________________________________________________

# დავალება ბ

numb1 = float(input('Please enter first number: '))
numb2 = float(input('Please enter second number: '))
operator = input('Please enter desired arithmetic operator(+, -, *, /, %, //, **): ')

if operator == '+':
    print(numb1 + numb2)

elif operator == '-':
    print(numb1 - numb2)

elif operator == '*':
    print(numb1 * numb2)

elif operator == '/':
    if numb2 != 0:
        print(numb1 / numb2)
    else:
        print('Cannot divide by zero')

elif operator == '%':
    if numb2 != 0:
        print(numb1 % numb2)
    else:
        print('Cannot divide by zero')

elif operator == '//':
    if numb2 != 0:
        print(numb1 // numb2)
    else:
        print('Cannot divide by zero')

elif operator == '**':
    print(numb1 ** numb2)

else:
    print('incorrect operator')

# ________________________________________________

# დავალება გ

numb1 = float(input('Please enter first number: '))
numb2 = float(input('Please enter second number: '))
numb3 = float(input('Please enter third number: '))

if numb1 == numb2 and numb2 == numb3 and numb1 == numb3:
    print('Please enter different numbers')
else:
    if numb1 > numb2 and numb1 > numb3:
        print('The biggest number is ', numb1)

    elif numb2 > numb1 and numb2 > numb3:
        print('The biggest number is ', numb2)

    elif numb3 > numb1 and numb3 > numb2:
        print('The biggest number is ', numb3)
    