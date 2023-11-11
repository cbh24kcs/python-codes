import copy

arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', [1, 2, 3]]

b = arr # 赋值
b[1] = 666
print(arr)

c = arr.copy() # 浅拷贝 arr[:]
c[-1][1] = 666
print(arr)

d = copy.deepcopy(arr) # 深拷贝
d[-1][1] = 999
print(arr)
print(d)
