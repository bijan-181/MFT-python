x= list(map(int,input().split()))
for i in range(3):
    for k in range(x[0]):
        for j in range(3):
            if (j == 0 and i ==0) or (j==2 and i==0) or (j==1 and i==1) or (j==0 and i==2) or (j==2 and i==2) or (j==2 and i==2):
                print("X" *x[1],end="")
            elif (j==1 and i==0) or (j==0 and i==1) or (j==2 and i==1) or (j==1 and i==2):
                print("."*x[1],end="")
        print()
