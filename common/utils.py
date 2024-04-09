from pages import all_page_url as pgs
import pytest


class HandleDate:
    """
    pytest的数据驱动
    """
    users = [{'id': 1, 'name': '钱七', 'sex': '女', 'age': 45},
             {'id': 2, 'name': '张三', 'sex': '男', 'age': 22},
             {'id': 3, 'name': '李四', 'sex': '女', 'age': 31},
             {'id': 4, 'name': '赵六', 'sex': '男', 'age': 49},
             {'id': 5, 'name': '王五', 'sex': '女', 'age': 26}]

    users2 = [[1, '赵六', '男', 58],
              [2, '王五', '男', 35],
              [3, '钱七', '女', 46],
              [4, '李四', '女', 24],
              [5, '张三', '男', 30]]

    sum = 0

    def put_user(self, users):
        global sum
        sum += 1
        print(f'运行第 {sum}次')
        print(f'------------------{users}')

    @pytest.mark.parametrize('list_users', users)
    def test_func(self, list_users):
        self.put_user(list_users)

    @pytest.mark.parametrize('id,name,sex,age', users2)
    def test_func2(self, id, name, sex, age):
        print(id, name, sex, age)


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


def singleton_instance(cls):
    """
    单例模式装饰器 可以装饰类
    :param cls:
    :return:
    """
    instance = {}

    def func(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
            return instance[cls]
        return instance[cls]

    return func


if __name__ == '__main__':
    pass
    # obj1 = Singleton()
    # obj2 = Singleton()
    # print(id(obj1))
    # print(id(obj2))
    #
    #
    # @singleton_instance
    # class SingletonInstance:
    #     def __init__(self, name):
    #         self.name = name
    #
    #     def run(self):
    #         print('run-----------------------')
    #
    #
    # instance = SingletonInstance('SHIYONG')
    # instance2 = SingletonInstance('SHIYONG')
    # print(id(instance))
    # print(id(instance2))
