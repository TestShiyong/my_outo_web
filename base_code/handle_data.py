from pages import all_page_url as pgs
import pytest

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


def put_user(users):
    global sum
    sum += 1
    print(f'运行第 {sum}次')
    print(f'------------------{users}')


@pytest.mark.parametrize('list_users', users)
def test_func(list_users):
    put_user(list_users)


@pytest.mark.parametrize('id,name,sex,age', users2)
def test_func2(id, name, sex, age):
    print(id, name, sex, age)
