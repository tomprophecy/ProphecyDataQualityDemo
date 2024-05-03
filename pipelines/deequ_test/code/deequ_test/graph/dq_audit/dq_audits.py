from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from deequ_test.udfs.UDFs import *

def dq_audits(spark: SparkSession, null_not_null_count_by_col_name: DataFrame):
    null_not_null_count_by_col_name.write\
        .format("delta")\
        .option("overwriteSchema", True)\
        .mode("overwrite")\
        .saveAsTable("`main`.`default`.`webinar_self_serve_dq_audits`")
