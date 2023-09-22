# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import dataclasses

from ..model import _ColonSeparatedRegional, _SlashSeparatedRegional


@dataclasses.dataclass
class Redshift(_ColonSeparatedRegional):
    service: str = dataclasses.field(default="redshift")


@dataclasses.dataclass
class RedshiftServerless(_SlashSeparatedRegional):
    service: str = dataclasses.field(default="redshift-serverless")


@dataclasses.dataclass
class _RedshiftCommon(Redshift):
    """
    todo: docstring
    """


@dataclasses.dataclass
class RedshiftCluster(_RedshiftCommon):
    """
    Example: arn:aws:redshift:us-east-1:414570653400:cluster:my_cluster
    """

    resource_type: str = dataclasses.field(default="cluster")

    @property
    def cluster_id(self) -> str:
        """
        "my_cluster" part of
        arn:aws:redshift:us-east-1:414570653400:cluster:my_cluster
        """

        return self.resource_id


@dataclasses.dataclass
class _RedshiftClusterCommon(Redshift):
    """
    todo: docstring
    """

    @property
    def cluster_id(self) -> str:
        return self.resource_id.split("/", 1)[0]

    @property
    def resource_name(self) -> str:
        return self.resource_id.split("/", 1)[1]


@dataclasses.dataclass
class RedshiftDatabaseUserGroup(_RedshiftClusterCommon):
    """
    Example: arn:aws:redshift:us-east-1:414570653400:dbgroup:my_cluster/my_db_group
    """

    resource_type: str = dataclasses.field(default="dbgroup")

    @property
    def user_group(self) -> str:
        return self.resource_id.split("/", 1)[1]

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        cluster_name: str,
        user_group: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=f"{cluster_name}/{user_group}",
        )


@dataclasses.dataclass
class RedshiftDatabaseName(_RedshiftClusterCommon):
    """
    Example: arn:aws:redshift:us-east-1:414570653400:dbname:my_cluster/my_database
    """

    resource_type: str = dataclasses.field(default="dbname")

    @property
    def database_name(self) -> str:
        return self.resource_id.split("/", 1)[1]

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        cluster_name: str,
        database_name: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=f"{cluster_name}/{database_name}",
        )


@dataclasses.dataclass
class RedshiftSnapshot(_RedshiftClusterCommon):
    """
    Example: arn:aws:redshift:us-east-1:414570653400:snapshot:my_cluster/my_snapshot
    """

    resource_type: str = dataclasses.field(default="snapshot")

    @property
    def snapshot_name(self) -> str:
        return self.resource_id.split("/", 1)[1]

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        cluster_name: str,
        snapshot_name: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=f"{cluster_name}/{snapshot_name}",
        )


@dataclasses.dataclass
class RedshiftSnapshotSchedule(_RedshiftCommon):
    """
    Example: arn:aws:redshift:us-east-1:414570653400:snapshotschedule:my_snapshot_schedule
    """

    resource_type: str = dataclasses.field(default="snapshotschedule")

    @property
    def snapshot_schedule_name(self) -> str:
        return self.resource_id


@dataclasses.dataclass
class RedshiftParameterGroup(_RedshiftCommon):
    """
    Example: arn:aws:redshift:us-east-1:414570653400:parametergroup:my_parameter_group
    """

    resource_type: str = dataclasses.field(default="parametergroup")

    @property
    def parameter_group_name(self) -> str:
        return self.resource_id


@dataclasses.dataclass
class RedshiftSubnetGroup(_RedshiftCommon):
    """
    Example: arn:aws:redshift:us-east-1:111122223333:subnetgroup:my_subnet_group
    """

    resource_type: str = dataclasses.field(default="subnetgroup")

    @property
    def subnet_group_name(self) -> str:
        return self.resource_id


@dataclasses.dataclass
class RedshiftSecurityGroup(Redshift):
    """
    Example: arn:aws:redshift:us-east-1:111122223333:securitygroup:my_group_name/ec2securitygroup/owner_name/sg-1a2b
    """

    resource_type: str = dataclasses.field(default="securitygroup")

    @property
    def security_group_name(self) -> str:
        return self.resource_id.split("/", 3)[0]

    @property
    def owner_name(self) -> str:
        return self.resource_id.split("/", 3)[2]

    @property
    def ec2_security_group_id(self) -> str:
        return self.resource_id.split("/", 3)[3]

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        security_group_name: str,
        owner_name: str,
        ec2_security_group_id: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=f"{security_group_name}/ec2securitygroup/{owner_name}/{ec2_security_group_id}",
        )


@dataclasses.dataclass
class _RedshiftServerlessCommon(RedshiftServerless):
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
class RedshiftServerlessNamespace(_RedshiftServerlessCommon):
    """
    Example: arn:aws:redshift-serverless:us-east-1:111122223333:namespace/my_namespace
    """

    resource_type: str = dataclasses.field(default="namespace")

    @property
    def namespace_id(self) -> str:
        return self.resource_id

    @property
    def namespace_name(self):  # pragma: no cover
        raise AttributeError("You cannot get the human friendly name from the ARN!")


@dataclasses.dataclass
class RedshiftServerlessWorkgroup(_RedshiftServerlessCommon):
    """
    Example: arn:aws:redshift-serverless:us-east-1:111122223333:workgroup/my_workgroup
    """

    resource_type: str = dataclasses.field(default="workgroup")

    @property
    def workgroup_id(self) -> str:
        return self.resource_id

    @property
    def workgroup_name(self):  # pragma: no cover
        raise AttributeError("You cannot get the human friendly name from the ARN!")


@dataclasses.dataclass
class RedshiftServerlessSnapshot(_RedshiftServerlessCommon):
    """
    Example: arn:aws:redshift-serverless:us-east-1:111122223333:snapshot/my_snapshot
    """

    resource_type: str = dataclasses.field(default="snapshot")

    @property
    def snapshot_id(self) -> str:
        return self.resource_id

    @property
    def snapshot_name(self):  # pragma: no cover
        raise AttributeError("You cannot get the human friendly name from the ARN!")


@dataclasses.dataclass
class RedshiftServerlessManagedVpcEndpoint(_RedshiftServerlessCommon):
    """
    Example: arn:aws:redshift-serverless:us-east-1:111122223333:managedvpcendpoint/my_vpc_endpoint
    """

    resource_type: str = dataclasses.field(default="managedvpcendpoint")
