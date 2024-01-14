a1 = list(map(int,input().split()))
a2 = list(map(int,input().split()))
a3 = list(map(int,input().split()))
a4 = []
if a1[0] == a2[0]:
    a4.append(a3[0])
elif a1[0] == a3[0]:
    a4.append(a2[0])
elif a2[0] == a3[0]:
    a4.append(a1[0])
if a1[1] == a2[1]:
    a4.append(a3[1])
elif a1[1] == a3[1]:
    a4.append(a2[1])
elif a2[1] == a3[1]:
    a4.append(a1[1])
print(a4[0],a4[1])