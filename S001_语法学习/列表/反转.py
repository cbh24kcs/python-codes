arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g']


print(arr[::-1]) # 反转, 但产生一个新的浅拷贝列表，不会影响原来的列表


arr.reverse() # 列表自身反转，没有返回值
print(arr)