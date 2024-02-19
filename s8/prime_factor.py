# https://quera.org/course/assignments/64295/problems/218369

number = int(input())
i = 2
factors = {}
while number != 1:
    while number % i == 0:
        if i in factors:
            factors[i] += 1
        else:
            factors[i] = 1
        number /= i
    i += 1
strlist = []
for i in factors:
    if (pow:=factors[i])>1:
        strlist.append(f"{i}^{pow}")
    else:
        strlist.append(f"{i}")
print("*".join(strlist))