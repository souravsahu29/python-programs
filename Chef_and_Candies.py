import math
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    if a <= b:
        print(0)
    else:
        d = a - b
        print(math.ceil(d/4))


'''
input
4
20 12
10 100
10 9
20 9
output
2
0
1
3

'''