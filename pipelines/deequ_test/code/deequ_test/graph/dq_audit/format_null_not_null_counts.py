from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from deequ_test.udfs.UDFs import *

def format_null_not_null_counts(spark: SparkSession, null_not_null_count_by_col_name: DataFrame) -> DataFrame:
    return null_not_null_count_by_col_name.select(
        current_timestamp().alias("run_at"), 
        col("col_name"), 
        col("count_null"), 
        col("count_not_null")
    )
