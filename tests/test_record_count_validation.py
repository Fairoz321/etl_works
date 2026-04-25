from utils.logger import logger
from functions.record_count import record_count_validation

def test_rec_count_src_tgt():

    logger.info(f""" ==================
    comparing the rec count of src and tgt""")

    result=record_count_validation()
    assert result, "❌ One or more table record counts did not match."
    print(f" count is matching in both src an tgt for all tables")

