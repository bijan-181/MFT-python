k = [3, 3, 1, 1, 2, 2]
n = [1, 2, 3]
s = [2, 1, 2, 3]
ks, ns, ss = 0, 0, 0
l = int(input())
kilid = input()
for i in range(l):
    a = int(kilid[i])
    if a == k[i % 6]:
        ks += 1
    if a == n[i % 3]:
        ns += 1
    if a == s[i % 4]:
        ss += 1
maxx = max(ks,ns,ss)
print(maxx)
if ks == maxx:
    print("keyvoon")
if ns == maxx:
    print("nezam")
if ss == maxx:
    print("shir farhad")
