import time
import logging
from Configuration.ConstantConfig import parent_directory_path
class Logger(object):
    def __init__(self, logger):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        rq = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        log_path = parent_directory_path + '/TestResult/TestLog/'
        log_name = log_path + rq + '.log'
        filehandler = logging.FileHandler(log_name)
        filehandler.setLevel(logging.INFO)
        consolehandler = logging.StreamHandler()
        consolehandler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        filehandler.setFormatter(formatter)
        consolehandler.setFormatter(formatter)
        self.logger.addHandler(filehandler)
        self.logger.addHandler(consolehandler)
    def getlog(self):
        return self.logger