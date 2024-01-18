inp = input().split()
n = int(inp[0])
basecode = set(inp[1])
codes = []
for _ in range(n):
    codes.append(input())
for code in codes:
    if set(code) == basecode:
        print('Yes')
    else:
        print('No')