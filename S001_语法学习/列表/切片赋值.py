
arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# print(arr[2:-2])

arr[2:-2] = [1, 2, 3, 4, 5]
print(arr)

a = 3
b = 4
[a, b] = [b, a]
print(a, b)

arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

[a, b, *c] = arr
print(a, b)
print(c)
