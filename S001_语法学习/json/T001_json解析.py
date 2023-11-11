import json

s = """
{
    "name": "张三",
    "age": 18
}
"""

d = json.loads(s)
print(d)

d["sex"] = '女'
s = json.dumps(d)
print(s)

