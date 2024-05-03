from deequ_test.graph.dq_audit.stack.config.Config import SubgraphConfig as stack_Config
from prophecy.config import ConfigBase


class SubgraphConfig(ConfigBase):

    def __init__(self, prophecy_spark=None, stack: dict={}, **kwargs):
        self.stack = self.get_config_object(
            prophecy_spark, 
            stack_Config(prophecy_spark = prophecy_spark), 
            stack, 
            stack_Config
        )
        pass

    def update(self, updated_config):
        self.stack = updated_config.stack
        pass

Config = SubgraphConfig()
