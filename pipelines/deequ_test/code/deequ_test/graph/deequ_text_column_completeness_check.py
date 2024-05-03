from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from deequ_test.config.ConfigStore import *
from deequ_test.udfs.UDFs import *

def deequ_text_column_completeness_check(spark: SparkSession, in0: DataFrame) -> (DataFrame, DataFrame):
    import os
    os.environ["SPARK_VERSION"] = '3.3'
    from pydeequ.checks import Check, CheckLevel
    from pydeequ.verification import VerificationSuite, VerificationResult

    return (in0,
            VerificationResult.checkResultsAsDataFrame(
              spark,
              VerificationSuite(spark)\
                .onData(in0)\
                .addCheck(Check(spark, CheckLevel.Error, "Review Check").isComplete("TEXT_COLUMN"))\
                .run()
            ))
