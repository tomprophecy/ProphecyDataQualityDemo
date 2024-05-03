from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from deequ_test.udfs.UDFs import *
from . import *
from .config import *

def dq_audit(spark: SparkSession, subgraph_config: SubgraphConfig, in0: DataFrame) -> None:
    Config.update(subgraph_config)
    df_metadata_columns = metadata_columns(spark, in0)
    df_stack = stack(subgraph_config.stack).apply(spark, df_metadata_columns, in0)
    df_null_not_null_count_by_col_name = null_not_null_count_by_col_name(spark, df_stack)
    df_format_null_not_null_counts = format_null_not_null_counts(spark, df_null_not_null_count_by_col_name)
    dq_audits(spark, df_format_null_not_null_counts)
    subgraph_config.update(Config)
