#:@ TIME 2021/12/22   17:55
#:@FILE  login_data.py
#:@EMAIL  1557225637@QQ.COM

user_data = ['ys@tetx.com', 123456]

all_data_empty = {"data": ["", ""], "expect": "Please enter an email address."}
emial_empty = {"data": ["", "123456"], "expect": "Please enter an email address."}
password_empty = {"data": ["ys@tetx.com", ""], "expect": "Please enter your password."}
invalid_email = {"data": ["ystetx.com", ""], "expect": "Please enter a valid email."}
error_password = {"data": ["ys@tetx.com", "123456756"],
                  "expect": "The email address or password you entered is incorrect."}
