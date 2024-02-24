''' For example, the boys can divide the watermelon
into two parts of 2 and 6 kilo respectively
(another variant — two parts of 4 and 4 kilos) '''
lst =[]
n = int(input())
if n % 2 != 0:
    print("NO")
else:
    for i in range(2, n, 2):
        if i <= n-i:
            lst.append((i, n-i))
    print("Yes")
    print(lst)








