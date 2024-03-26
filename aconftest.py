# :@ TIME 2021/11/25   20:25
# :@FILE  conftest.py
# :@EMAIL  1557225637@QQ.COM
import pytest

#定义方法级别fixture
@pytest.fixture()
def main_fixture():
    print('fixture前置条件-----------------》')

    yield  True,666

    print('fixture后置条件-----------------》')


#定义类级别fixture,每个类只运行一次此前置后置
@pytest.fixture()
def class_fixcure():
    print('类级别fixture前置条件=============================》')

    yield  {"name":"shiyong"}

    print('类级别fixtur后置条件=============================》')

