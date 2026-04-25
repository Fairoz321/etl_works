import pandas as pd
from utils.logger import logger
from config.configfile import null_check_file_db,DATA_DIR
from config.db_connection import tgt_db_connection


def file_db_null_validation():

    conn = tgt_db_connection()

    all_passed = True

    for src_file, config in null_check_file_db.items():

        cols = config["columns"]
        tgt_table = config["tgt_table"]

        # Source file checks using pandas
        src_df = pd.read_csv(DATA_DIR / src_file)

        for col in cols:

            src_nulls = src_df[col].isnull().sum()

            cursor = conn.cursor()
            cursor.execute(
             f"""
             select count(*)
             from {tgt_table}
             where {col} is null
             """
            )

            tgt_nulls = cursor.fetchone()[0]
            cursor.close()

            if src_nulls != tgt_nulls:
                logger.error(
                    f"NULL mismatch :: "
                    f"File {src_file}.{col} = {src_nulls}, "
                    f"Table {tgt_table}.{col} = {tgt_nulls}"
                )
                all_passed = False

            else:
                logger.info(
                    f"NULL match :: "
                    f"File {src_file}.{col} = {src_nulls}, "
                    f"Table {tgt_table}.{col} = {tgt_nulls}"
                )

    conn.close()
    return all_passed