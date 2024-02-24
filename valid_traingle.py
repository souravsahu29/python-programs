a, b, c = list(map(int, input().split()))

# if l**2 + b**2 == h**2:
#     print("Yes")
# else:
#     print("No")
if (a+b > c) or (a+c > b) or (b+c > a):
    print("Yes")
else:
    print("No")





