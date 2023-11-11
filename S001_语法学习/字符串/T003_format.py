

name = "张三"
age = 18
a = '我叫 {name}, 我今年 {age} 岁了'

# result = a.format(name=name, age=age)
result = a.format(**{"name": "李四", "age": 19})
print(result)

obj = {
    "name": 123,
    name: 123
}
print(obj)
