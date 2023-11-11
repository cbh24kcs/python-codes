
arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g']


print(arr[1])
print(arr[1:3]) # 左闭右开 -- 区间

# arr = [1, 2, 3] + [4, 5, 6]
# print(arr)

print(arr[0:5:2])

# 序列类型

print(arr[-3])
print(arr[2:-2])
print(arr[:]) # 浅拷贝

# ...

print(arr[::-1]) # 反转, 但产生一个新的浅拷贝列表，不会影响原来的列表
print(arr[2:-1])
print(arr[2:0:-1])

arr.reverse() # 列表自身反转，没有返回值
print(arr)


