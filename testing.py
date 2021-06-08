arr = [17, 18, 5, 4, 6, 1]
lst = []
for i in range(1, len(arr)):
    arr[i-1] = (max(arr[i:]))
lst.append(-1)
print(arr)
