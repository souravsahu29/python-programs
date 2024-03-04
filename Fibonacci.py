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

# def fibonacci_list(n):
#     if n == 0:
#         return [0]
#     elif n == 1:
#         return [0, 1]
#     else:
#         fib_list = fibonacci_list(n - 1)
#         fib_list.append(fib_list[-1] + fib_list[-2])
#         return fib_list
#
# # Example usage:
# number_of_terms = 7
# fibonacci_series = fibonacci_list(number_of_terms - 1)  # Subtract 1 to get the first n terms
#
# print(f"Fibonacci series up to {number_of_terms} terms: {fibonacci_series}")