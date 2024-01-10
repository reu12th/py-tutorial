#!/usr/bin/python3
x = int(input("enter integer: "))
if x < 0:
    x = 0
    print('negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
