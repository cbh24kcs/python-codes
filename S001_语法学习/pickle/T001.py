import pickle

a = {
    "name": "张三",
}


pickle.dump(a, file=open('a', 'wb'))


