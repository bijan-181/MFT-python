a = [1,2,3,4,5,6,7,8,9]
print(a)
d = {}
# print(tuple(enumerate(a)))
for i,j in enumerate(a):
    d[f'a{i}']=j
print(d)