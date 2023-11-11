
s1 = {1, 2, 3}
s2 = set([1, 2, 3])

arr = [1, 2, 1, 2, 1, 1, 2, 3, 4, 3]
arr1 = list(set(arr))
print(arr1)

s1 = {1, 2, 3}
s2 = {2, 3, 4}
print("交集", s1 & s2)
print("并集", s1 | s2)
print("交叉补集", s1 ^ s2)


