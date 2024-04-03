def singleton_instance(cls):
    instances = {}

    def fun(*ars, **kwargs):
        if cls in instances:
            return instances[cls]
        else:
            instances[cls] = cls(*ars, **kwargs)
            return instances[cls]

    return fun


@singleton_instance
class SingletonObject:
    def __init__(self, name):
        self.name = name

    def test_func(self):
        print('11111111111')


singleton_instance1 = SingletonObject('shiyong')
singleton_instance2 = SingletonObject('shiyong1')

print(id(singleton_instance1))
print(id(singleton_instance2))
