from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
# =====================================
# record count validation : all file names from src and table tgt

hr_file_db_mapping = {
    "employee_src.csv": "employee_tgt_pandas",

    "department_src.csv": "department_tgt_pandas"
}
# ======================================
#  null checkkkkk
null_check_file_db = {

    "department_src.csv": {
        "tgt_table": "department_tgt_pandas",
        "columns": [
            "dept_id",
            "dept_name",
            "location"
        ]
    },

    "employee_src.csv": {
        "tgt_table": "employee_tgt_pandas",
        "columns": [
            "id",
            "name",
            "dept_id",
            "salary",
            "last_updated",
            "status",
            "age"
        ]
    }

}
# ===========================================
duplicate_check_file_db = {

    "department_src.csv": {
        "tgt_table": "department_tgt_pandas",
        "columns": [
            "dept_name"
        ]
    },

    "employee_src.csv": {
        "tgt_table": "employee_tgt_pandas",
        "columns": [
            "name",
            "dept_id",
            "salary",
            "status"
        ]
    }

}