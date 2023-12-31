"""
input:
5
10
output:
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
"""
length_ = int(input('enter length:'))
width_ = int(input("enter width:"))

for i in range(length_):
    for i in range(width_):
        print('* ',end='')
    print()