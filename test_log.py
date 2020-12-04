import logging
from logging import handlers
import datetime

nowTime = datetime.datetime.now().strftime('%Y%m%d%H%M')
log_name = './log_' + str(nowTime) + '.log'

logger = logging.getLogger()
logger.setLevel(level=logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
# 输出到文件
file_handler = logging.FileHandler(log_name,'a','utf-8')
file_handler.setLevel(level=logging.DEBUG)
file_handler.setFormatter(formatter)
# 输出到控制台
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)
# 以天（'D'）为周期进行日志分割，分、秒分别是M S
# time_rotating_file_handler = handlers.TimedRotatingFileHandler(filename='rotating_test.log', when='D')
# time_rotating_file_handler.setLevel(logging.DEBUG)
# time_rotating_file_handler.setFormatter(formatter)
# 加载handler
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
# logger.addHandler(time_rotating_file_handler)

logger.info('hh_{:.3f}_hh'.format(10.0))