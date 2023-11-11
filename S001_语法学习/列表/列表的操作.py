
arr = [1, 2, 3]
print(arr)

arr.append(123)
print(arr)

# 在指定位置【之前】插入指定元素
# arr.insert(1, [1, 2, 3])
arr = arr[:1] + ['a', 'b', 'c'] + arr[1:]
print(arr)



