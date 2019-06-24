from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from logging.handlers import SysLogHandler,TimedRotatingFileHandler
from logging import FileHandler
import logging,os



def initLoggers(loggers):
    formatter = logging.Formatter(
            '%(asctime)s | %(name)s | %(levelname)s | %(created)f | %(thread)d '
            '%(pathname)s | %(lineno)s | %(message)s')
    path="logs"
    if not os.path.exists(path):
        os.mkdir(path)
    rotateFileHandler=TimedRotatingFileHandler(path+os.sep+"flask_log", "D", 1, 100) # 一天一文件，保留100天
    rotateFileHandler.suffix="%Y-%m-%d %H_%M_%S.log"
    rotateFileHandler.setFormatter(formatter)

    # filehandler = FileHandler("flask.log")
    # filehandler.setFormatter(formatter)
    sysHandler=SysLogHandler()
    loggers.addHandler(rotateFileHandler)
    loggers.addHandler(sysHandler)
    loggers.setLevel(logging.INFO)


app = Flask(__name__)
app.config.from_object(Config)
initLoggers(app.logger)
db = SQLAlchemy(app)




from app import routes, models
