r1,rc,c2 = map(int,input().split())
m1 =[]
m2 = []
for _ in range(r1):
    m1.append(list(map(int,input().split())))
for _ in range(rc):
    m2.append(list(map(int,input().split())))
mr = []
for i in range(r1):
    rowlist = []
    for j in range(c2):
        mulsum = 0
        for k in range(rc):
            mulsum += m1[i][k] * m2[k][j]
        rowlist.append(mulsum)
    mr.append(rowlist)
for i in mr:
    print(" ".join(list(map(str,i))))