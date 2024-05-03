from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from deequ_test.udfs.UDFs import *

def null_not_null_count_by_col_name(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("col_name"))

    return df1.agg(
        sum(expr("if((value IS NULL), 1, 0)")).alias("count_null"), 
        sum(expr("if((value IS NOT NULL), 1, 0)")).alias("count_not_null")
    )
