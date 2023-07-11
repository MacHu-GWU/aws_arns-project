# -*- coding: utf-8 -*-

import dataclasses

from ..model import SlashSeparatedRegional


@dataclasses.dataclass
class CodeBuild(SlashSeparatedRegional):
    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        fullname: str,
        resource_type: str,
    ):
        return super(CodeBuild, cls).new(
            partition="aws",
            service="codebuild",
            region=aws_region,
            account_id=aws_account_id,
            resource_id=fullname,
            resource_type=resource_type,
        )


@dataclasses.dataclass
class CodeBuildProject(CodeBuild):
    """
    Example: arn:aws:codebuild:us-east-1:111122223333:project/my-project
    """

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
        return super(CodeBuildProject, cls).new(
            aws_region=aws_region,
            aws_account_id=aws_account_id,
            fullname=name,
            resource_type="project",
        )


@dataclasses.dataclass
class CodeBuildRun(CodeBuild):
    """
    Example: arn:aws:codebuild:us-east-1:111122223333:build/my-project:a1b2c3d4
    """

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
        return super(CodeBuildRun, cls).new(
            aws_region=aws_region,
            aws_account_id=aws_account_id,
            fullname=fullname,
            resource_type="build",
        )
