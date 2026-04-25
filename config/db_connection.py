import os
import mysql.connector
from mysql.connector import Error
from utils.logger import logger
from dotenv import load_dotenv

load_dotenv()



def tgt_db_connection():
    try:
        tgt_conn= mysql.connector.connect(
        user=os.getenv('TGT_DB_USER'),
        password=os.getenv('TGT_DB_PASSWORD'),
        host=os.getenv('TGT_DB_HOST'),
        database= os.getenv('TGT_DB_NAME'),
        port=int(os.getenv('TGT_DB_PORT'))
        )

        if tgt_conn.is_connected():
            logger.info(f"connected to target db : {os.getenv('TGT_DB_NAME')} successfully")
            return tgt_conn

    except Error as e:
        logger.error(f"failed to connect to target db: {os.getenv('TGT_DB_NAME')} {e}")
        return None



