def cache(fun):
    map = {}
    
    def inner(x, y):
        
        if (x, y) in map:
            print("取缓存值:", map[(x, y)])
            return map[(x, y)]
        else:
            result = fun(x, y)
            map[(x, y)] = result
            return result
    
    return inner


@cache
def add(x, y):
    return x + y

# add = cache(add)

print(add(3, 4))
print(add(3, 4))
print(add(3, 4))