import logging
from logging import handlers

def log_file():
    '''
    %(name)s：Logger的名字
    %(levelno)s：打印日志级别的数值
    %(levelname)s：打印日志级别的名称
    %(pathname)s：打印当前执行程序的路径，其实就是sys.argv[0]
    %(filename)s：打印当前执行程序名
    %(funcName)s：打印日志的当前函数
    %(lineno)d：打印日志的当前行号
    %(asctime)s：打印日志的时间
    %(thread)d：打印线程ID
    %(threadName)s：打印线程名称
    %(process)d：打印进程ID
    %(message)s：打印日志信息
    '''
    logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
        filename='test.log',
        filemode='a',
        level=logging.INFO)# a为追加模式，w为覆写模式
    logging.debug('debug级别，一般用来打印一些调试信息，级别最低')
    logging.info('info级别，一般用来打印一些正常的操作信息')
    logging.warning('waring级别，一般用来打印警告信息')
    logging.error('error级别，一般用来打印一些错误信息')
    logging.critical('critical级别，一般用来打印一些致命的错误信息，等级最高')


def log_module():
    '''
    Log的模块化设计：
        Logger 暴露了应用程序代码能直接使用的接口。
        Handler 将（记录器产生的）日志记录发送至合适的目的地。
        Filter 提供了更好的粒度控制，它可以决定输出哪些日志记录。
        Formatter 指明了最终输出中日志记录的内容和格式。

    常用的4种handler：
        logging.StreamHandler -> 控制台输出
        logging.FileHandler -> 文件输出
        logging.handlers.RotatingFileHandler -> 按照大小自动分割日志文件，一旦达到指定的大小重新生成文件
        logging.handlers.TimedRotatingFileHandler -> 按照时间自动分割日志文件
    '''
    logger = logging.getLogger('test')
    logger.setLevel(level=logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    stream_handler = logging.StreamHandler()

    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    logger.debug('debug级别，一般用来打印一些调试信息，级别最低')
    logger.info('info级别，一般用来打印一些正常的操作信息')
    logger.warning('waring级别，一般用来打印警告信息')
    logger.error('error级别，一般用来打印一些错误信息')
    logger.critical('critical级别，一般用来打印一些致命的错误信息，等级最高')

def log_print_file():
    logger = logging.getLogger('test')
    logger.setLevel(level=logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    # 输出到文件
    file_handler = logging.FileHandler('./test2.log','a','utf-8')
    file_handler.setLevel(level=logging.DEBUG)
    file_handler.setFormatter(formatter)
    # 输出到控制台
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    logger.debug('debug级别，一般用来打印一些调试信息，级别最低')
    logger.info('info级别，一般用来打印一些正常的操作信息')
    logger.warning('waring级别，一般用来打印警告信息')
    logger.error('error级别，一般用来打印一些错误信息')
    logger.critical('critical级别，一般用来打印一些致命的错误信息，等级最高')

def log_split():
    '''
    logging.handlers.RotatingFileHandler -> 按照大小自动分割日志文件，一旦达到指定的大小重新生成文件
    logging.handlers.TimedRotatingFileHandler -> 按照时间自动分割日志文件
    '''
    
    logger = logging.getLogger('test')
    logger.setLevel(level=logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    # 输出到文件
    file_handler = logging.FileHandler('./test2.log','a','utf-8')
    file_handler.setLevel(level=logging.DEBUG)
    file_handler.setFormatter(formatter)
    # 输出到控制台
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)
    # 以天（'D'）为周期进行日志分割，分、秒分别是M S
    time_rotating_file_handler = handlers.TimedRotatingFileHandler(filename='rotating_test.log', when='D')
    time_rotating_file_handler.setLevel(logging.DEBUG)
    time_rotating_file_handler.setFormatter(formatter)
    # 加载handler
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    logger.addHandler(time_rotating_file_handler)

    logger.debug('debug级别，一般用来打印一些调试信息，级别最低')
    logger.info('info级别，一般用来打印一些正常的操作信息')
    logger.warning('waring级别，一般用来打印警告信息')
    logger.error('error级别，一般用来打印一些错误信息')
    logger.critical('critical级别，一般用来打印一些致命的错误信息，等级最高')

def my_log(level,str):
    logger = logging.getLogger('test')
    logger.setLevel(level=logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    # 输出到文件
    file_handler = logging.FileHandler('./test2.log','a','utf-8')
    file_handler.setLevel(level=logging.DEBUG)
    file_handler.setFormatter(formatter)
    # 输出到控制台
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)
    # 以天（'D'）为周期进行日志分割，分、秒分别是M S
    time_rotating_file_handler = handlers.TimedRotatingFileHandler(filename='rotating_test.log', when='D')
    time_rotating_file_handler.setLevel(logging.DEBUG)
    time_rotating_file_handler.setFormatter(formatter)
    # 加载handler
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    logger.addHandler(time_rotating_file_handler)

    if level=='info':
        logger.info(str)
    elif level == 'error':
        logger.error(str)

