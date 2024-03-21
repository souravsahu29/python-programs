def sort(n):
    for i in range(len(n)):
        for j in range(i+1,len(n)):
            if n[i] > n[j]:
                n[i],n[j] = n[j], n[i]
    return n


n = [2,7,1,5]
print(sort(n))



