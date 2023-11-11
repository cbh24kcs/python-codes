
f = open('a.txt', encoding='utf8')

# 读取整个文件内容
# content = f.read()
# print(content)

# 读取一行
# line = f.readline()
# print(line)

# 将多行读取为一个列表
# lines = f.readlines()
# # print(lines)
# for line in lines:
#     print(line)

# for line in f:
#     print(line)

# for line in open('a.txt', encoding='utf8'):
#     print(line)


# 判断文件是否可读
print(f.readable())
