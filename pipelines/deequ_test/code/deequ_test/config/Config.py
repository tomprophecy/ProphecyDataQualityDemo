from deequ_test.graph.dq_audit.config.Config import SubgraphConfig as dq_audit_Config
from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, dq_audit: dict=None, **kwargs):
        self.spark = None
        self.update(dq_audit)

    def update(self, dq_audit: dict={}, **kwargs):
        prophecy_spark = self.spark
        self.dq_audit = self.get_config_object(
            prophecy_spark, 
            dq_audit_Config(prophecy_spark = prophecy_spark), 
            dq_audit, 
            dq_audit_Config
        )
        pass
