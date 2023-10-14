# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import dataclasses

from ..model import _ColonSeparatedRegional


@dataclasses.dataclass
class Cloud9(_ColonSeparatedRegional):
    service: str = dataclasses.field(default="cloud9")

    @property
    def name(self) -> str:
        return self.resource_id


@dataclasses.dataclass
class _Cloud9Common(Cloud9):
    """
    todo: docstring
    """

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
class Cloud9Environment(_Cloud9Common):
    """
    Example: arn:aws:cloud9:us-east-1:111122223333:environment:my_environment
    """

    resource_type: str = dataclasses.field(default="environment")
