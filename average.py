n = int(input())
for i in range(n):
    a, b, c = map(int, input().split())
    if (a + b)/2 > c:
        print("YES")
    else:
        print("NO")

'''
Test case
5
5 9 6
5 8 6
5 7 6
4 9 8
3 7 2

output:
YES
YES
NO
NO
YES

'''