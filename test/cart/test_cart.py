import allure


# @allure.feature('cart模块')
@allure.story('cart')
@allure.title('加车成功')
def test_cart1():
    print('test_allure11111111111111111111111111111')


# @allure.feature('cart模块')
@allure.story('cart')
@allure.title('加车失败')
def test_cart2():
    print('test_allure2222222222222222222222222222')


# @allure.feature('cart模块')
@allure.story('cart')
@allure.title('加车多个商品')
def test_cart3():
    print('test_allure33333333333333333333333333333333')
