# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import dataclasses

from ..model import _SlashSeparatedRegional


@dataclasses.dataclass
class EFS(_SlashSeparatedRegional):
    service: str = dataclasses.field(default="elasticfilesystem")


@dataclasses.dataclass
class _EFSCommon(EFS):
    """
    todo: docstring
    """

    @property
    def name(self) -> str:
        return self.resource_id

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
class EFSAccessPoint(_EFSCommon):
    """
    Example: arn:aws:elasticfilesystem:us-east-1:111122223333:access-point/my_access_point
    """

    resource_type: str = dataclasses.field(default="access-point")


@dataclasses.dataclass
class EFSFileSystem(_EFSCommon):
    """
    Example: arn:aws:elasticfilesystem:us-east-1:111122223333:file-system/my_file_system
    """

    resource_type: str = dataclasses.field(default="file-system")
