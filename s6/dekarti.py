x,y = tuple(map(int,input().split()))
for i in range(x):
    print(" _"*y)
    print("| "*(y+1))
print(" _"*y)