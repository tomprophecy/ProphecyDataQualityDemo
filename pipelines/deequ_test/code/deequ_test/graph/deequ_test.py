from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from deequ_test.config.ConfigStore import *
from deequ_test.udfs.UDFs import *

def deequ_test(spark: SparkSession) -> DataFrame:
    df1 = spark.range(1)

    return df1.select(lit("Test value").alias("input"))
