from functions.duplicate_check import file_db_duplicate_validation
from utils.logger import logger


def test_duplicates():

    logger.info(
      "🚀 Starting File to DB duplicate validation"
    )

    result = file_db_duplicate_validation()

    assert result, (
      "❌ Duplicate validation failed"
    )

    print(
      "✅ File to DB duplicate validation passed"
    )