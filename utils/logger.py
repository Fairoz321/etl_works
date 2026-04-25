import os
import logging
from email import message_from_bytes

if not os.path.exists('logs'):
    os.makedirs('logs')

logger = logging.getLogger('etl_logger')
logger.setLevel(logging.INFO)

filehandler = logging.FileHandler('logs/etl_logs.log',encoding='utf-8')
formatter= logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
filehandler.setFormatter(formatter)

logger.addHandler(filehandler)