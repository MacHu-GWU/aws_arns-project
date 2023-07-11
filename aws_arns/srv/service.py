# -*- coding: utf-8 -*-

"""
This is for internal use, don't import
"""

import dataclasses
from ..model import (
    CrossAccountGlobal,
    Global,
    Regional,
    ResourceIdOnlyRegional,
    ColonSeparatedRegional,
    SlashSeparatedRegional,
)


@dataclasses.dataclass
class S3(CrossAccountGlobal):
    pass


# --- ResourceIdOnlyRegional
@dataclasses.dataclass
class SQS(ResourceIdOnlyRegional):
    pass


@dataclasses.dataclass
class SNS(ResourceIdOnlyRegional):
    pass


@dataclasses.dataclass
class CodeCommit(ResourceIdOnlyRegional):
    pass


@dataclasses.dataclass
class CodePipeline(ResourceIdOnlyRegional):
    pass


# --- ColonSeparatedRegional
@dataclasses.dataclass
class Lambda(ColonSeparatedRegional):
    pass


@dataclasses.dataclass
class Sfn(ColonSeparatedRegional):
    pass


@dataclasses.dataclass
class SecretManager(ColonSeparatedRegional):
    pass


# --- SlashSeparatedRegional
@dataclasses.dataclass
class CloudFormation(SlashSeparatedRegional):
    pass


@dataclasses.dataclass
class CodeBuild(SlashSeparatedRegional):
    pass


@dataclasses.dataclass
class ECS(SlashSeparatedRegional):
    pass


@dataclasses.dataclass
class Dynamodb(SlashSeparatedRegional):
    pass


@dataclasses.dataclass
class Glue(SlashSeparatedRegional):
    pass


@dataclasses.dataclass
class KMS(SlashSeparatedRegional):
    pass


@dataclasses.dataclass
class SageMaker(SlashSeparatedRegional):
    pass


@dataclasses.dataclass
class SSMParameterStore(SlashSeparatedRegional):
    pass
