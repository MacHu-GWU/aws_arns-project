# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import dataclasses

from ..model import _SlashSeparatedRegional


@dataclasses.dataclass
class Bedrock(_SlashSeparatedRegional):
    """
    todo: docstring
    """

    service: str = dataclasses.field(default="bedrock")

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        resource_id: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=resource_id,
        )


@dataclasses.dataclass
class BedrockAgent(Bedrock):
    """
    Example: arn:aws:bedrock:us-east-1:111122223333:agent/a1b2c3
    """

    resource_type: str = dataclasses.field(default="agent")


@dataclasses.dataclass
class BedrockAgent(Bedrock):
    """
    Example: arn:aws:bedrock:us-east-1:111122223333:agent-alias/AgentId/AliasId
    """

    resource_type: str = dataclasses.field(default="agent-alias")

    @classmethod
    def new(cls, aws_account_id: str, aws_region: str, agent_name: str, alias: str):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=f"{agent_name}/{alias}",
        )


@dataclasses.dataclass
class BedrockApplicationInferenceProfile(Bedrock):
    """
    Example: arn:aws:bedrock:us-east-1:111122223333:application-inference-profile/a1b2c3
    """

    resource_type: str = dataclasses.field(default="application-inference-profile")


@dataclasses.dataclass
class BedrockAsyncInvoke(Bedrock):
    """
    Example: arn:aws:bedrock:us-east-1:111122223333:async-invoke/a1b2c3
    """

    resource_type: str = dataclasses.field(default="async-invoke")


@dataclasses.dataclass
class BedrockCustomModel(Bedrock):
    """
    Example: arn:aws:bedrock:us-east-1:111122223333:custom-model/a1b2c3
    """

    resource_type: str = dataclasses.field(default="custom-model")


@dataclasses.dataclass
class BedrockDataAutomationInvocationJob(Bedrock):
    """
    Example: arn:aws:bedrock:us-east-1:111122223333:data-automation-invocation/a1b2c3
    """

    resource_type: str = dataclasses.field(default="data-automation-invocation")


@dataclasses.dataclass
class BedrockDataAutomationProfile(Bedrock):
    """
    Example: arn:aws:bedrock:us-east-1:111122223333:data-automation-profile/a1b2c3
    """

    resource_type: str = dataclasses.field(default="data-automation-profile")


@dataclasses.dataclass
class BedrockDataAutomationProject(Bedrock):
    """
    Example: arn:aws:bedrock:us-east-1:111122223333:data-automation-project/a1b2c3
    """

    resource_type: str = dataclasses.field(default="data-automation-project")


@dataclasses.dataclass
class BedrockDefaultPromptRouter(Bedrock):
    """
    Example: arn:aws:bedrock:us-east-1:111122223333:default-prompt-router/a1b2c3
    """

    resource_type: str = dataclasses.field(default="default-prompt-router")


@dataclasses.dataclass
class BedrockEvaluationJob(Bedrock):
    """
    Example: arn:aws:bedrock:us-east-1:111122223333:evaluation-job/a1b2c3
    """

    resource_type: str = dataclasses.field(default="evaluation-job")


@dataclasses.dataclass
class BedrockFlow(Bedrock):
    """
    Example: arn:aws:bedrock:us-east-1:111122223333:flow/a1b2c3
    """

    resource_type: str = dataclasses.field(default="flow")


@dataclasses.dataclass
class BedrockFlowAlias(Bedrock):
    """
    Example: arn:aws:bedrock:us-east-1:111122223333:flow-alias/FlowId/alias/AliasId
    """

    resource_type: str = dataclasses.field(default="flow-alias")

    @classmethod
    def new(cls, aws_account_id: str, aws_region: str, flow_name: str, alias: str):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=f"{flow_name}/alias/{alias}",
        )


@dataclasses.dataclass
class BedrockFoundationModel(Bedrock):
    """
    Example: arn:aws:bedrock:us-east-1::foundation-model/a1b2c3
    """

    resource_type: str = dataclasses.field(default="foundation-model")

    @classmethod
    def new(
        cls,
        aws_region: str,
        resource_id: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id="",
            region=aws_region,
            resource_id=resource_id,
        )


@dataclasses.dataclass
class BedrockGuardrail(Bedrock):
    """
    Example: arn:aws:bedrock:us-east-1:111122223333:guardrail/a1b2c3
    """

    resource_type: str = dataclasses.field(default="guardrail")


@dataclasses.dataclass
class BedrockInferenceProfile(Bedrock):
    """
    Example: arn:aws:bedrock:us-east-1:111122223333:inference-profile/a1b2c3
    """

    resource_type: str = dataclasses.field(default="knowledge-base")


@dataclasses.dataclass
class BedrockKnowledgeBase(Bedrock):
    """
    Example: arn:aws:bedrock:us-east-1:111122223333:knowledge-base/a1b2c3
    """

    resource_type: str = dataclasses.field(default="knowledge-base")


@dataclasses.dataclass
class BedrockModelCopyJob(Bedrock):
    """
    Example: arn:aws:bedrock:us-east-1:111122223333:model-copy-job/a1b2c3
    """

    resource_type: str = dataclasses.field(default="model-copy-job")


@dataclasses.dataclass
class BedrockModelCustomizationJob(Bedrock):
    """
    Example: arn:aws:bedrock:us-east-1:111122223333:model-customization-job/a1b2c3
    """

    resource_type: str = dataclasses.field(default="model-customization-job")


@dataclasses.dataclass
class BedrockModelEvaluationJob(Bedrock):
    """
    Example: arn:aws:bedrock:us-east-1:111122223333:model-evaluation-job/a1b2c3
    """

    resource_type: str = dataclasses.field(default="model-evaluation-job")


@dataclasses.dataclass
class BedrockModelImportJob(Bedrock):
    """
    Example: arn:aws:bedrock:us-east-1:111122223333:model-import-job/a1b2c3
    """

    resource_type: str = dataclasses.field(default="model-import-job")


@dataclasses.dataclass
class BedrockModelInvocationJob(Bedrock):
    """
    Example: arn:aws:bedrock:us-east-1:111122223333:model-invocation-job/a1b2c3
    """

    resource_type: str = dataclasses.field(default="model-invocation-job")


@dataclasses.dataclass
class BedrockPrompt(Bedrock):
    """
    Example: arn:aws:bedrock:us-east-1:111122223333:prompt/a1b2c3
    """

    resource_type: str = dataclasses.field(default="prompt")


@dataclasses.dataclass
class BedrockPromptRouter(Bedrock):
    """
    Example: arn:aws:bedrock:us-east-1:111122223333:prompt-router/a1b2c3
    """

    resource_type: str = dataclasses.field(default="prompt-router")


@dataclasses.dataclass
class BedrockPromptVersion(Bedrock):
    """
    Example: arn:aws:bedrock:us-east-1:111122223333:prompt-version/a1b2c3
    """

    resource_type: str = dataclasses.field(default="prompt-version")

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        prompt: str,
        version: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=f"{prompt}:{version}",
        )


@dataclasses.dataclass
class BedrockProvisionedModel(Bedrock):
    """
    Example: arn:aws:bedrock:us-east-1:111122223333:provisioned-model/a1b2c3
    """

    resource_type: str = dataclasses.field(default="provisioned-model")


@dataclasses.dataclass
class BedrockSession(Bedrock):
    """
    Example: arn:aws:bedrock:us-east-1:111122223333:session/a1b2c3
    """

    resource_type: str = dataclasses.field(default="session")
