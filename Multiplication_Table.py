def multiply_table(n=0, limit=0):
    for i in range(limit):
        print(f"{n} x {i+1} = {n*i}")


number = int(input("number = "))
range_limit = int(input("range_limit = "))
multiply_table(number, range_limit)