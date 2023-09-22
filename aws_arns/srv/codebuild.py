# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import dataclasses

from ..model import _SlashSeparatedRegional


@dataclasses.dataclass
class CodeBuild(_SlashSeparatedRegional):
    service: str = dataclasses.field(default="codebuild")


@dataclasses.dataclass
class CodeBuildProject(CodeBuild):
    """
    Example: arn:aws:codebuild:us-east-1:111122223333:project/my-project
    """

    resource_type: str = dataclasses.field(default="project")

    @property
    def codebuild_project_name(self) -> str:
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


@dataclasses.dataclass
class _CodeBuildRunCommon(CodeBuild):
    @property
    def codebuild_run_fullname(self) -> str:
        return self.resource_id

    @property
    def codebuild_project_name(self) -> str:
        return self.resource_id.split(":")[0]

    @property
    def codebuild_run_id(self) -> str:
        return self.resource_id.split(":")[-1]

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        fullname: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=fullname,
        )


@dataclasses.dataclass
class CodeBuildRun(_CodeBuildRunCommon):
    """
    Example: arn:aws:codebuild:us-east-1:111122223333:build/my-project:a1b2c3d4
    """

    resource_type: str = dataclasses.field(default="build")


@dataclasses.dataclass
class CodeBuildBatchRun(_CodeBuildRunCommon):
    """
    Example: arn:aws:codebuild:us-east-1:111122223333:build-batch/my-project:a1b2c3d4
    """

    resource_type: str = dataclasses.field(default="build-batch")
