from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from deequ_test.udfs.UDFs import *

def metadata_columns(spark: SparkSession, in0: DataFrame) -> DataFrame:
    out0 = spark.createDataFrame([[column] for column in in0.columns], schema = ['column'])

    return out0
