import pandas as pd
from utils.logger import logger
from config.configfile import duplicate_check_file_db
from config.db_connection import tgt_db_connection

# Yes — if goal is proper duplicate validation, I’d update function to not compare source vs target,
# just validate target has zero duplicates (much cleaner for this testcase).
# if tgt is file then use  for src_file, config in duplicate_check_file_db.items():
#
#         tgt_table = config["tgt_table"]
#         key_cols = config["columns"]
#
#
#         # -----------------------------
#         # Source duplicate check (pandas)
#         # -----------------------------
#         src_df = pd.read_csv(f"../data/{src_file}")
#
#         src_duplicates = (
#             src_df
#             .duplicated(subset=key_cols)
#             .sum()
#         )
def file_db_duplicate_validation():

    conn = tgt_db_connection()

    if not conn:
        logger.error(
           "❌ Target DB connection failed"
        )
        return False


    all_passed = True


    for src_file, config in duplicate_check_file_db.items():

        tgt_table = config["tgt_table"]

        key_cols = config["columns"]

        col_str = ", ".join(key_cols)


        try:

            cursor = conn.cursor()

            query = f"""
                SELECT COUNT(*)
                FROM
                (
                    SELECT {col_str}
                    FROM {tgt_table}
                    GROUP BY {col_str}
                    HAVING COUNT(*) > 1
                ) a
            """

            cursor.execute(query)

            tgt_duplicates = cursor.fetchone()[0]

            cursor.close()


            if tgt_duplicates > 0:

                logger.error(
                    f"Duplicates found :: "
                    f"Table {tgt_table} = "
                    f"{tgt_duplicates} duplicate groups"
                )

                all_passed = False


            else:

                logger.info(
                    f"No duplicates :: "
                    f"Table {tgt_table}"
                )


        except Exception as e:

            logger.error(
                f" Error checking duplicates "
                f"in {tgt_table}: {e}"
            )

            all_passed = False


    conn.close()

    return all_passed