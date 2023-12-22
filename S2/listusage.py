names = []
ages = []
for i in range(3):
    name = input(f'enter name {i+1}:')
    age = input(f'enter age {i+1}:')
    names.append(name)
    ages.append(age)

# print(names,ages)
for i in range(3):
    print(f"{names[i]:^20}|{ages[i]:^5}")