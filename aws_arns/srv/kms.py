# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import dataclasses

from ..model import _SlashSeparatedRegional


@dataclasses.dataclass
class Kms(_SlashSeparatedRegional):
    service: str = dataclasses.field(default="kms")


@dataclasses.dataclass
class KmsKey(Kms):
    """
    Example: "arn:aws:kms:us-east-1:111122223333:key/1a2b3c"
    """

    resource_type: str = dataclasses.field(default="key")

    @property
    def key_id(self) -> str:
        """
        "1a2b3c" part of
        arn:aws:kms:us-east-1:111122223333:key/1a2b3c
        """
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        key_id: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=key_id,
        )


@dataclasses.dataclass
class KmsAlias(Kms):
    """
    Example: "arn:aws:kms:us-east-1:111122223333:alias/my_key"
    """

    resource_type: str = dataclasses.field(default="alias")

    @property
    def alias(self) -> str:
        """
        "my_key" part of
        arn:aws:kms:us-east-1:111122223333:alias/my_key
        """
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        alias: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=alias,
        )
