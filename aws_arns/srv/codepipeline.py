# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import dataclasses

from ..model import _ResourceIdOnlyRegional


@dataclasses.dataclass
class CodePipeline(_ResourceIdOnlyRegional):
    service: str = dataclasses.field(default="codepipeline")


@dataclasses.dataclass
class CodePipelinePipeline(CodePipeline):
    """
    Example: arn:aws:codepipeline:us-east-1:111122223333:test
    """

    @property
    def pipeline_name(self) -> str:
        """
        CodePipeline name
        """
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        name: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=name,
        )
