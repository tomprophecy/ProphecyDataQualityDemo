from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from deequ_test.config.ConfigStore import *
from deequ_test.udfs.UDFs import *
from prophecy.utils import *
from deequ_test.graph import *

def pipeline(spark: SparkSession) -> None:
    df_deequ_test = deequ_test(spark)
    df_adds_null = adds_null(spark, df_deequ_test)
    df_deequ_text_column_completeness_check_out0, df_deequ_text_column_completeness_check_out1 = deequ_text_column_completeness_check(
        spark, 
        df_adds_null
    )
    dq_audit(spark, Config.dq_audit, df_adds_null)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/deequ_test")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/deequ_test", config = Config)(pipeline)

if __name__ == "__main__":
    main()
