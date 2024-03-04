def rotate_list(lst, n):
    n = n % len(lst)
    return lst[-n:] + lst[:-n]


original_list = [1, 2, 3, 4, 5]
rot = int(input("Enter the Rotation:"))
result = (rotate_list(original_list,rot))

print(result)
