n, m = map(int, input().split())
for i in range(3*n):
    if n <= i < 2*n:
        print('.'*m,'X'*m,'.'*m,sep='')
    else:
        print('X'*m,'.'*m,'X'*m,sep='')
