def fibonacci(terms):
    a, b = 0, 1
    print("Fibonacci Series:", end=" ")
    for i in range(terms):
        print(a, end="")
        if i < terms - 1:
            print(", ", end="")
        a, b = b, a + b


term = int(input("Enter the term: "))
fibonacci(term)