"""input
int = 5
output:
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""

n = int(input('enter number: '))
# for i in range(n):
#     for j in range(n):
#         print('*', end=' ')
#     print()
# for i in range(n):
#     print('* '*n)

"""
output:
* * * * *
*       *
*       *
*       *
* * * * *
"""

for i in range(n):
    if i == 0 or i == n-1:
        print('* '*n)
    else:
        print('*'+'  '*n-2+ '*')