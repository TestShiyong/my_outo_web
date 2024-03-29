import pytest
from common.handle_images import take_screenshot

pytest.main(['-s', '-v', '-n', '3','--alluredir=./allure_report'])
# pytest.main(['-s', '-v', ])

# url ='https://www.azazie.com/products/azazie-alia-matcha-a-line-pleated-chiffon-floor-length-bridesmaid-dress/220853?size=a0'
# path = './'
# take_screenshot(url,)