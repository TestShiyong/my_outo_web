import os

base_dir = os.path.dirname(os.path.abspath(__file__))

log_dir = os.path.join(base_dir, r'output', 'log', 'logs.log')

allure_report_dir = os.path.join(base_dir, 'allure_report')

error_picture_dir = os.path.join(base_dir, r'output', 'error_picture')

allure_dir = os.path.join(base_dir, 'output', 'allure_report')

erp_file_path = os.path.join(base_dir, 'az_job/erp/server_config_file/azft.azft')

erp_file_path2 = os.path.join(base_dir, 'az_job/erp/server_config_file/erp-test-aws.rsa')

base = os.path.dirname(os.path.abspath(__file__))

config_file_dir = os.path.join(base, 'pytest.ini')

screenshots_path = os.path.join(base_dir, 'output', 'screenshot')


if __name__ == '__main__':
    print(config_file_dir)
    print()
