
f = open('a.txt', 'r+', encoding='utf8')

# f.write('####')

"""
文件指针定位：f.seek(N, [whence])
    whence=0（默认）：从文件开头开始计算
    whence=1：从当前位置开始计算
    whence=2：从文件末尾开始计算
    
获取文件指针当前位置：f.tell()
"""

f.seek(0)
f.write("#")
f.seek(100)
f.write("#")

