from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from deequ_test.udfs.UDFs import *

def select_column_as_string(spark: SparkSession, TableIterator_Input: DataFrame) -> DataFrame:
    out0 = TableIterator_Input.select(
        lit(Config.column).alias("col_name"),
        col(Config.column).cast("string").alias("value")
    )

    return out0
