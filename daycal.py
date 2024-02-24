def days_cal(n):
    year, month, day = 0, 0, 0
    for i in range(n):
        if n >= 365:
            year += 1
            n -= 365
        elif n >= 30:
            month += 1
            n -= 30
        else:
            day += n
    print("Month:", month)
    print("Year:", year)
    print("Day:", day)


n = int(input("Enter the day:"))
days_cal(n)
