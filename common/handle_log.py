#:@ TIME 2021/12/23   10:54
#:@FILE  log.py
#:@EMAIL  1557225637@QQ.COM
import logging
from base_path import log_dir


class Mylog(logging.Logger):
    def __init__(self, name, level, file=None):
        super().__init__(name, level)

        # 设置收集器
        mylog = logging.getLogger('mylog')
        # 设置日志收集级别
        mylog.setLevel(level)
        # 创建渠道
        console_handle = logging.StreamHandler()
        # 定义日志输出格式
        fmt = '%(asctime)s:%(name)s:%(funcName)s:%(filename)s:%(lineno)d:%(levelname)s:%(message)s'
        # 创建日志格式
        format = logging.Formatter(fmt)
        # 渠道绑定日志格式
        console_handle.setFormatter(format)
        # 收集器添加渠道
        self.addHandler(console_handle)
        # 判断是否写入文件
        if file:
            # 创建文件收集渠道
            file_handle = logging.FileHandler(file, mode='w', encoding='utf-8')
            # 日志格式绑定渠道
            file_handle.setFormatter(format)
            # 添加至收集器
            self.addHandler(file_handle)


logg = Mylog('mylog', 'INFO', file=log_dir)

if __name__ == '__main__':
    logg = Mylog('mylog', 'INFO', file=log_dir)
    logg.info('logger................................................')
