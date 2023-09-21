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
