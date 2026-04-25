import pandas as pd
from mysql.connector.constants import flag_is_set

from utils.logger import logger
from config.configfile import hr_file_db_mapping,DATA_DIR
from config.db_connection import tgt_db_connection

def record_count_validation():

    t_conn = tgt_db_connection()

    if  not t_conn:
        logger.error(f"connection failed for tgt db")
        return False

    all_passed = True

    for src_file, tgt_table in hr_file_db_mapping.items():
        try:
            src_df = pd.read_csv(DATA_DIR/src_file)
            s_count = len(src_df)
            # That's unnecessary overhead.
            # If target has 10 million rows:
            # •	SQL count → fast
            # •	pandas load all rows → heavy
            # So we used SQL intentionally.
            # Rule of thumb
            # Use SQL when database can validate cheaply:
            # •	Record count
            # •	Duplicates
            # •	Aggregates
            # •	Null checks
            # •	Min/max
            # •	Joins
            # Use pandas when you need richer comparison:
            # •	Source vs target row comparison
            # •	File vs DB reconciliation
            # •	Column-level validations
            # •	Data mismatch checks
            # •	Complex transformations validation
            # Need only count? Use SQL for target.
            # Need full data comparison? Pull target into pandas.

            t_cursor = t_conn.cursor()
            t_cursor.execute(f"select count(*) from {tgt_table}")
            t_count = t_cursor.fetchone()[0]
            t_cursor.close()

            if s_count != t_count:
                logger.error(f"Count mismatch :: File {src_file} = {s_count}, Table {tgt_table} = {t_count}")
                all_passed = False
            else:
                logger.info(f"Count match :: File {src_file} = {s_count}, Table {tgt_table} = {t_count}")

        except Exception as e:
            logger.error(f"some  dd issue occured:{e}")
            all_passed = False


    t_conn.close()
    return all_passed

