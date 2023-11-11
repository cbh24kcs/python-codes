
arr = []

# 末尾添加
arr.append(111)
print(arr)

# 末尾添加多个
arr.extend([1, 2, 3])
print(arr)

arr += ['a', 'b']
print(arr)

# 指定位置添加
arr.insert(2, '#')
print(arr)

# 切片赋值，进行添加
arr[1:2] = [123123123]
print(arr)

