# -*- coding: utf-8 -*-

"""
This is for internal use, don't import
"""

import dataclasses
from ..model import (
    _CrossAccountGlobal,
    _Global,
    _Regional,
    ResourceIdOnlyRegional,
    _ColonSeparatedRegional,
    _SlashSeparatedRegional,
)

from .batch import Batch
from .s3 import S3
from .iam import Iam
from .cloudformation import CloudFormation
from .codebuild import CodeBuild
from .sagemaker_a2i import A2I


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
class Lambda(_ColonSeparatedRegional):
    pass


@dataclasses.dataclass
class Sfn(_ColonSeparatedRegional):
    pass


@dataclasses.dataclass
class SecretManager(_ColonSeparatedRegional):
    pass


# --- SlashSeparatedRegional


@dataclasses.dataclass
class CodeBuild(_SlashSeparatedRegional):
    pass


@dataclasses.dataclass
class ECS(_SlashSeparatedRegional):
    pass


@dataclasses.dataclass
class Dynamodb(_SlashSeparatedRegional):
    pass


@dataclasses.dataclass
class Glue(_SlashSeparatedRegional):
    pass


@dataclasses.dataclass
class KMS(_SlashSeparatedRegional):
    pass


@dataclasses.dataclass
class SageMaker(_SlashSeparatedRegional):
    pass


@dataclasses.dataclass
class SSMParameterStore(_SlashSeparatedRegional):
    pass
