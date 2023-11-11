print("你好")

# 列表 - 可变的
arr = [1, 'a', 'asda', True, False]
print(arr)

# 元组 - 不可变性
t1 = (1, 2, 3, True)


arr[1] = 666
print(arr)

# t1[1] = 666
# print(t1)

# 万物皆对象
a = 1

# 数字
# a = 2 ** 10000
# print(a)

# Python代码 -> 解释 -> 编译 -> 链接依赖库 -> 运行
# 可执行文件 -> 运行

# 解释型语言: Python、JS
# 编译型语言：C/C++
# 半编译半解释：Java

a = 3

if a > 2:
    print("a > 2")
elif a < 2:
    print("a < 2")
else:
    print("a = 2")


# a = 1
# while a < 10:
#     print(a)
#     a += 1


arr = ['a', 'b', 'c', 'd']

for x in arr:
    print(x)


# JS：弱类型
# Python：强类型
# JS、Python：动态类型

# 函数
def fun(x, y, *arr, **obj):
    print("这是一个函数", x, y, arr, obj)


# 按位置传参
fun(3, 4)
# 按参数名传参
fun(y=3, x=4)
fun(1, 2, 3, 4, 5, a=3, b=4, c=5)

# lambda表达式
f = lambda x, y: x+y

class User:
    pass


user = User()


def add(x: int, y: int) -> int:
    return x + y





