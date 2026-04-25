from functions.null_check import file_db_null_validation
from utils.logger import logger

def test_nulls():
    logger.info(f""" ==================
        comparing the null check of src and tgt""")
    result = file_db_null_validation()

    assert result, "Null check mismatch found"
    print(f" null is matching in both src an tgt for all tables")




