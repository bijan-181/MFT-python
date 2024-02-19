def sortedkey(dictitem):
    return dictitem[1]
count = int(input())
majik = list(map(int,input().split()))
majikset = sorted(list(set(majik)))
majikdict = {}
for i in majikset:
    majikdict[i]=majik.count(i)
print(sorted(majikdict.items(),key=sortedkey)[0][0])
