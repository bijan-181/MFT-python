x,y = tuple(map(int,input().split()))
matrix =[]
for _ in range(x):
    matrix.append(list(map(int,input().split())))
counter = 0
for i in range(1, x-1):
    for j in range(1, y-1):
        if ((matrix[i][j-1] < matrix[i][j] < matrix[i-1][j] and
             matrix[i][j+1] < matrix[i][j] < matrix[i+1][j]) or
            (matrix[i-1][j] < matrix[i][j] < matrix[i][j-1] and
             matrix[i+1][j] < matrix[i][j] < matrix[i][j+1])):
            counter += 1
print(counter)