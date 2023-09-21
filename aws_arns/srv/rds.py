# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import dataclasses

from ..model import _ColonSeparatedRegional


@dataclasses.dataclass
class Rds(_ColonSeparatedRegional):
    """
    todo: docstring
    """
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
    """
    Example: arn:aws:rds:us-east-1:111122223333:db:my-mysql-instance-1
    """
    resource_type: str = dataclasses.field(default="db")

    @property
    def db_instance_id(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class RdsDBCluster(_RdsCommon):
    """
    Example: arn:aws:rds:us-east-1:111122223333:cluster:my-aurora-cluster-1
    """
    resource_type: str = dataclasses.field(default="cluster")

    @property
    def db_cluster_id(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class RdsEventSubscription(_RdsCommon):
    """
    Example: arn:aws:rds:us-east-1:111122223333:es:my-subscription
    """
    resource_type: str = dataclasses.field(default="es")

    @property
    def db_event_subscription_id(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class RdsDBOptionGroup(_RdsCommon):
    """
    Example: arn:aws:rds:us-east-1:111122223333:og:my-og
    """
    resource_type: str = dataclasses.field(default="og")

    @property
    def db_option_group_id(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class RdsDBParameterGroup(_RdsCommon):
    """
    Example: arn:aws:rds:us-east-2:123456789012:pg:my-param-enable-logs
    """
    resource_type: str = dataclasses.field(default="pg")

    @property
    def db_parameter_group_id(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class RdsDBClusterParameterGroup(_RdsCommon):
    """
    Example: arn:aws:rds:us-east-1:111122223333:cluster-pg:my-cluster-param-timezone
    """
    resource_type: str = dataclasses.field(default="cluster-pg")

    @property
    def db_cluster_parameter_group_id(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class RdsReservedDBInstance(_RdsCommon):
    """
    Example: arn:aws:rds:us-east-1:111122223333:ri:my-reserved-postgresql
    """
    resource_type: str = dataclasses.field(default="ri")

    @property
    def reserved_db_instance_id(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class RdsDBSecurityGroup(_RdsCommon):
    """
    Example: arn:aws:rds:us-east-1:111122223333:secgrp:my-public
    """
    resource_type: str = dataclasses.field(default="secgrp")

    @property
    def db_security_group_id(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class RdsDBInstanceSnapshot(_RdsCommon):
    """
    Example:

    - arn:aws:rds:us-east-1:111122223333:snapshot:rds:my-mysql-db-2020-01-01-00-00
    - arn:aws:rds:us-east-1:111122223333:snapshot:my-mysql-db-snap
    """
    resource_type: str = dataclasses.field(default="snapshot")

    @property
    def db_instance_snapshot_name(self) -> str:  # pragma: no cover
        return self.resource_id

    def is_system_managed(self) -> bool:
        return self.db_instance_snapshot_name.startswith("rds:")


@dataclasses.dataclass
class RdsDBClusterSnapshot(_RdsCommon):
    """
    Example:

    - arn:aws:rds:us-east-1:111122223333:cluster-snapshot:rds:my-aurora-cluster-2020-01-01-00-00
    - arn:aws:rds:us-east-1:111122223333:cluster-snapshot:my-aurora-cluster-snap
    """
    resource_type: str = dataclasses.field(default="cluster-snapshot")

    @property
    def db_cluster_snapshot_name(self) -> str:  # pragma: no cover
        return self.resource_id

    def is_system_managed(self) -> bool:
        return self.db_cluster_snapshot_name.startswith("rds:")


@dataclasses.dataclass
class RdsDBSubnetGroup(_RdsCommon):
    """
    Example: arn:aws:rds:us-east-1:111122223333:subgrp:my-subnet-10
    """
    resource_type: str = dataclasses.field(default="subgrp")

    @property
    def db_subnet_group_name(self) -> str:  # pragma: no cover
        return self.resource_id
