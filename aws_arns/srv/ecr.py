# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import dataclasses

from ..model import _SlashSeparatedRegional


@dataclasses.dataclass
class Ecr(_SlashSeparatedRegional):
    service: str = dataclasses.field(default="ecr")


@dataclasses.dataclass
class EcrRepository(Ecr):
    """
    Example: arn:aws:ecr:us-east-1:123456789012:repository/my-repo
    """

    resource_type: str = dataclasses.field(default="repository")

    @property
    def repo_name(self) -> str:
        """
        The "my-repo" part of
        arn:aws:ecr:us-east-1:123456789012:repository/my-repo
        """
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        repo_name: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=repo_name,
        )

    @property
    def uri(self) -> str:
        return f"{self.aws_account_id}.dkr.ecr.{self.aws_region}.amazonaws.com/{self.repo_name}"

    @classmethod
    def from_uri(cls, uri: str):
        """
        Factory method.
        """
        domain, name = uri.split("/", 1)
        parts = domain.split(".")
        aws_account_id = parts[0]
        aws_region = parts[3]
        return cls.new(
            aws_account_id=aws_account_id,
            aws_region=aws_region,
            repo_name=name,
        )
