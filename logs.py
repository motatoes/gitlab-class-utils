from loader import get_settings
import logging
from logging import FileHandler

def createLogger(fileLocation='degug.log'):
    CONFIG = get_settings()

    logger = logging.getLogger('gitlab-class-utils')
    fileHandler = FileHandler(fileLocation) 
    fileHandler.setLevel(logging.WARNING)
    fileHandler.setFormatter(Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'
    ))
    logger.addHandler(fileHandler)

    return logger
    
    
