from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from deequ_test.config.ConfigStore import *
from deequ_test.udfs.UDFs import *

def adds_null(spark: SparkSession, deequ_test: DataFrame) -> DataFrame:
    return deequ_test.select(col("input").alias("TEXT_COLUMN"), lit(None).alias("NULL_COLUMN"))
