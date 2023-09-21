# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import dataclasses

from ..model import _ColonSeparatedRegional


@dataclasses.dataclass
class Rds(_ColonSeparatedRegional):
    service: str = dataclasses.field(default="rds")


@dataclasses.dataclass
class _RdsCommon(Rds):
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
class RdsDBInstance(_RdsCommon):
    resource_type: str = dataclasses.field(default="db")

    @property
    def db_instance_id(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class RdsDBCluster(_RdsCommon):
    resource_type: str = dataclasses.field(default="cluster")

    @property
    def db_cluster_id(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class RdsEventSubscription(_RdsCommon):
    resource_type: str = dataclasses.field(default="es")

    @property
    def db_event_subscription_id(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class RdsDBOptionGroup(_RdsCommon):
    resource_type: str = dataclasses.field(default="og")

    @property
    def db_option_group_id(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class RdsDBParameterGroup(_RdsCommon):
    resource_type: str = dataclasses.field(default="pg")

    @property
    def db_parameter_group_id(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class RdsDBClusterParameterGroup(_RdsCommon):
    resource_type: str = dataclasses.field(default="cluster-pg")

    @property
    def db_cluster_parameter_group_id(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class RdsReservedDBInstance(_RdsCommon):
    resource_type: str = dataclasses.field(default="ri")

    @property
    def reserved_db_instance_id(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class RdsDBSecurityGroup(_RdsCommon):
    resource_type: str = dataclasses.field(default="secgrp")

    @property
    def db_security_group_id(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class RdsDBInstanceSnapshot(_RdsCommon):
    resource_type: str = dataclasses.field(default="snapshot")

    @property
    def db_instance_snapshot_name(self) -> str:  # pragma: no cover
        return self.resource_id

    def is_system_managed(self) -> bool:
        return self.db_instance_snapshot_name.startswith("rds:")


@dataclasses.dataclass
class RdsDBClusterSnapshot(_RdsCommon):
    resource_type: str = dataclasses.field(default="cluster-snapshot")

    @property
    def db_cluster_snapshot_name(self) -> str:  # pragma: no cover
        return self.resource_id

    def is_system_managed(self) -> bool:
        return self.db_cluster_snapshot_name.startswith("rds:")


@dataclasses.dataclass
class RdsDBSubnetGroup(_RdsCommon):
    resource_type: str = dataclasses.field(default="subgrp")

    @property
    def db_subnet_group_name(self) -> str:  # pragma: no cover
        return self.resource_id
