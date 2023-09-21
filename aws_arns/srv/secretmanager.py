# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import dataclasses

from ..model import _ColonSeparatedRegional


@dataclasses.dataclass
class SecretManager(_ColonSeparatedRegional):
    service: str = dataclasses.field(default="secretsmanager")


@dataclasses.dataclass
class SecretManagerSecret(SecretManager):
    """
    Example: "arn:aws:secretsmanager:us-east-1:111122223333:secret:MyFolder/MySecret-a1b2c3"
    """
    resource_type: str = dataclasses.field(default="secret")

    @property
    def secret_name(self) -> str:
        """
        "MyFolder/MySecret" part of
        arn:aws:secretsmanager:us-east-1:111122223333:secret:MyFolder/MySecret-a1b2c3
        """
        return "-".join(self.resource_id.split("-")[:-1])

    @property
    def long_name(self) -> str:
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        long_name: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=long_name,
        )
