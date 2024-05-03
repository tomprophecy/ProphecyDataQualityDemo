from prophecy.config import ConfigBase


class SubgraphConfig(ConfigBase):

    def __init__(self, prophecy_spark=None, column: str="", **kwargs):
        self.column = column
        pass

    def update(self, updated_config):
        self.column = updated_config.column
        pass

Config = SubgraphConfig()
