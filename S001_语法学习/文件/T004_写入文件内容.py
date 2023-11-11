
f = open('a.txt', 'a', encoding='utf8')

f.write("你好啊")

# 写入多行
f.writelines([
    "你好啊\n",
    "Hello World\n",
    "123123123123\n",
])
