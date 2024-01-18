"""
input:
m 2 sib
k 1 badam
f 2 noshabe
k 0.5 pesteh

output:
mive froshi :
    1. 2kg sib
khoshkbar:
    1. 1kg badam
    2. 0.5kg pesteh
froshgah:
    1. 2ta noshabeh

"""

orderList = {
    'm':{},
    'f':{},
    'g':{},
    'k':{}
}

order = input()
while order.lower() != 'exit':
    loc,qu,name = order.split()
    orderList[loc][name]=qu
    order = input()
print(orderList)
