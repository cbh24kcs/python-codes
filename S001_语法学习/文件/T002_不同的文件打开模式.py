
"""
r   以只读模式打开文件，如果文件不存在，输出 FileNotFoundError 错误；这是默认打开模式
w   以写模式打开文件，如果文件非空，则文件已有的内容会被清空；如果文件不存在，则创建文件
a   写模式，但是在原有文件末尾追加内容
x   创建一个新文件，如果文件存在，则抛出 FileExistsError 文件已存在错误

r+  读 + 写
a+ 打开一个文件用于读写....
w+

rb  b表示以二进制方式打开文件
"""

f = open('a.txt')



