# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import dataclasses

from ..model import _SlashSeparatedRegional


@dataclasses.dataclass
class Athena(_SlashSeparatedRegional):
    service: str = dataclasses.field(default="athena")

    @property
    def name(self) -> str:
        return self.resource_id


@dataclasses.dataclass
class _AthenaCommon(Athena):
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
class AthenaCapacityReservation(_AthenaCommon):
    """
    Example: arn:aws:athena:us-east-1:111122223333:capacity-reservation/my_capacity_reservation
    """

    resource_type: str = dataclasses.field(default="capacity-reservation")


@dataclasses.dataclass
class AthenaDataCatalog(_AthenaCommon):
    """
    Example: arn:aws:athena:us-east-1:111122223333:datacatalog/my_datacatalog
    """

    resource_type: str = dataclasses.field(default="datacatalog")


@dataclasses.dataclass
class AthenaWorkgroup(_AthenaCommon):
    """
    Example: arn:aws:athena:us-east-1:111122223333:workgroup/my_workgroup
    """

    resource_type: str = dataclasses.field(default="workgroup")
