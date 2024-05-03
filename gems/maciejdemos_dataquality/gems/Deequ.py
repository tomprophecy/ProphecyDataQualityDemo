from prophecy.cb.server.base.ComponentBuilderBase import *
from pyspark.sql import *
from pyspark.sql.functions import *

from prophecy.cb.server.base import WorkflowContext
from prophecy.cb.server.base.datatypes import SInt, SString
from prophecy.cb.ui.uispec import *

@dataclass(frozen=True)
class RuleDef:
    colName: str
    ruleName: str
    extraParams: Optional[str] = None

class Deequ(ComponentSpec):
    name: str = "Deequ"
    category: str = "Transform"

    def optimizeCode(self) -> bool:
        return True

    @dataclass(frozen=True)
    class DeequProperties(ComponentProperties):
        columnsSelector: List[str] = field(default_factory=list)
        rulesColumns: List[RuleDef] = field(default_factory=list)

    def onClickFunc(
        self, portId: str, column: str, state: Component[DeequProperties]
    ):
        rules = state.properties.rulesColumns
        rules.append(RuleDef(column, "isComplete"))
        return state.bindProperties(replace(state.properties, rulesColumns=rules))

    def dialog(self) -> Dialog:
        selectBox = (
            SelectBox("")
                .addOption("Is Not Null", "isComplete")
                .addOption("Is Unique", "isUnique")
                .addOption("Is Non Negative", "isNonNegative")
                .addOption("Is Contained In", "isContainedIn")
        )

        ruleTable = BasicTable(
            "Rule Table",
            height="300px",
            columns=[
                Column(
                    "Column Name",
                    "colName",
                    (ExpressionBox("").withSchemaSuggestions()),
                ),
                Column(
                    "Rule",
                    "ruleName",
                    selectBox,
                ),
                Column(
                    "Values",
                    "extraParams",
                    (TextBox("", ignoreTitle=True).bindPlaceholder("")),
                )
            ],
        ).bindProperty("rulesColumns")
        
        return Dialog("Deequ").addElement(
            ColumnsLayout(gap=("1rem"), height=("100%"))
                .addColumn(
                PortSchemaTabs(
                    selectedFieldsProperty=("columnsSelector"),
                    singleColumnClickCallback=self.onClickFunc,
                ).importSchema()
            ).addColumn(StackLayout(height=("100%"))
                    .addElement(ruleTable), "2fr")
        )

    def validate(self, context: WorkflowContext, component: Component[DeequProperties]) -> List[Diagnostic]:
        diagnostics = []

        if len(component.properties.rulesColumns) == 0:
            diagnostics.append(
                Diagnostic(
                    "properties.rulesColumns",
                    "At least one rule has to be specified",
                    SeverityLevelEnum.Error,
                )
            )
        
        for idx, rule in enumerate(component.properties.rulesColumns):
            if rule.ruleName == "isContainedIn":
                if rule.extraParams is None:
                    diagnostics.append(
                        Diagnostic(
                            f"properties.rulesColumns[{idx}].extraParams",
                            "Extra Argument needs to be provided for Is Contained In rule type. Please provide comma separated list of categorical values.",
                            SeverityLevelEnum.Error
                        )
                    )
        return diagnostics

    def onChange(self, context: WorkflowContext, oldState: Component[DeequProperties], newState: Component[DeequProperties]) -> Component[
    DeequProperties]:
        newState = replace(newState, ports=replace(newState.ports, isCustomOutputSchema = True, autoUpdateOnRun = True))
        return newState


    class DeequCode(ComponentCode):
        def __init__(self, newProps):
            self.props: Deequ.DeequProperties = newProps

        def apply(self, spark: SparkSession, in0: DataFrame) -> (DataFrame, DataFrame):
            import os
            os.environ["SPARK_VERSION"] = '3.3'

            from pydeequ.checks import Check, CheckLevel
            from pydeequ.verification import VerificationSuite, VerificationResult
            check = Check(spark, CheckLevel.Error, "Review Check")

            for rules in self.props.rulesColumns:
                if rules.ruleName == "isComplete":
                    check = check.isComplete(rules.colName)
                elif rules.ruleName == "isUnique":
                    check = check.isUnique(rules.colName)
                elif rules.ruleName == "isNonNegative":
                    check = check.isNonNegative(rules.colName)
                elif rules.ruleName == "isContainedIn":
                    check = check.isContainedIn(rules.colName, [val.strip() for val in rules.extraParams.split(",")])

            checkResult = VerificationSuite(spark).onData(in0).addCheck(check).run()
            checkResult_df = VerificationResult.checkResultsAsDataFrame(spark, checkResult)
            return in0, checkResult_df
