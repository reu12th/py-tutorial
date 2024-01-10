age = eval(input('Enter age: '))

if age < 5:
    print('Too young')
elif age == 5:
    print('Go to Kindergarten.')
elif (age > 5) and (age <= 17):
    grade = age - 5
    print('Go to grade {} since you are {} years old.'.format(grade, age))
else:
    print('Too old! Go to college bro.')
