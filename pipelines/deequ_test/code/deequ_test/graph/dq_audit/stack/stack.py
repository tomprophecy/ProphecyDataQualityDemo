from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from deequ_test.udfs.UDFs import *
from . import *
from .config import *


class stack(MetaGemExec):

    def __init__(self, config):
        self.config = config
        super().__init__()

    def execute(self, spark: SparkSession, subgraph_config: SubgraphConfig, out0: DataFrame) -> List[DataFrame]:
        Config.update(subgraph_config)
        df_select_column_as_string = select_column_as_string(spark, out0)
        subgraph_config.update(Config)

        return list((df_select_column_as_string, ))

    def apply(self, spark: SparkSession, metadata_columns: DataFrame, in1: DataFrame) -> DataFrame:
        in0 = metadata_columns
        inDFs = [in1]
        results = []
        conf_to_column = dict([("column", "column")])

        if metadata_columns.count() > 1000:
            raise Exception(f"Config DataFrame row count::{in0.count()} exceeds max run count")

        for row in metadata_columns.collect():
            update_config = self.config.update_from_row_map(row, conf_to_column)
            _inputs = inDFs
            results.append(self.__run__(spark, update_config, *_inputs))

        return do_union(results)
