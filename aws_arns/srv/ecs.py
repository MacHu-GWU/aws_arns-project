# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import dataclasses

from ..model import _SlashSeparatedRegional


@dataclasses.dataclass
class Ecs(_SlashSeparatedRegional):
    service: str = dataclasses.field(default="ecs")


@dataclasses.dataclass
class EcsCluster(Ecs):
    """
    Example: arn:aws:ecs:us-east-1:123456789012:cluster/my-cluster-1
    """

    resource_type: str = dataclasses.field(default="cluster")

    @property
    def cluster_name(self) -> str:  # pragma: no cover
        """
        The "my-cluster-1" part of
        arn:aws:ecs:us-east-1:123456789012:cluster/my-cluster-1
        """
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        cluster_name: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=cluster_name,
        )


@dataclasses.dataclass
class EcsTaskDefinition(Ecs):
    """
    Example: arn:aws:ecs:us-east-1:111122223333:task-definition/my-task:1
    """

    resource_type: str = dataclasses.field(default="task-definition")

    @property
    def task_name(self) -> str:  # pragma: no cover
        """
        The "my-task" part of
        arn:aws:ecs:us-east-1:111122223333:task-definition/my-task:1
        """
        return self.resource_id.split(":", 1)[0]

    @property
    def version(self) -> int:  # pragma: no cover
        """
        The "1" part of
        arn:aws:ecs:us-east-1:111122223333:task-definition/my-task:1
        """
        return int(self.resource_id.split(":", 1)[1])

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        task_name: str,
        version: int,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=f"{task_name}:{version}",
        )


@dataclasses.dataclass
class EcsContainerInstance(Ecs):
    """
    Example: arn:aws:ecs:us-east-1:111122223333:container-instance/my-cluster/container_instance_UUID
    """

    resource_type: str = dataclasses.field(default="container-instance")

    @property
    def cluster_name(self) -> str:  # pragma: no cover
        """
        The "my-cluster" part of
        arn:aws:ecs:us-east-1:111122223333:container-instance/my-cluster/container_instance_UUID
        """
        return self.resource_id.split("/", 1)[0]

    @property
    def container_instance_id(self) -> str:  # pragma: no cover
        """
        The "container_instance_UUID" part of
        arn:aws:ecs:us-east-1:111122223333:container-instance/my-cluster/container_instance_UUID
        """
        return self.resource_id.split("/", 1)[1]

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        cluster_name: str,
        container_instance_id: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=f"{cluster_name}/{container_instance_id}",
        )


@dataclasses.dataclass
class EcsService(Ecs):
    """
    Example: arn:aws:ecs:us-east-1:111122223333:service/service_name
    """

    resource_type: str = dataclasses.field(default="service")

    @property
    def service_name(self) -> str:  # pragma: no cover
        """
        The "service_name" part of
        arn:aws:ecs:us-east-1:111122223333:service/service_name
        """
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        service_name: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=service_name,
        )


@dataclasses.dataclass
class EcsTaskRun(Ecs):
    """
    Example: arn:aws:ecs:us-east-1:123456789012:task/a1b2c3d4-5678-90ab-ccdef-11111EXAMPLE
    """

    resource_type: str = dataclasses.field(default="task")

    @property
    def run_id(self) -> str:  # pragma: no cover
        """
        The "a1b2c3d4-5678-90ab-ccdef-11111EXAMPLE" part of
        arn:aws:ecs:us-east-1:123456789012:task/a1b2c3d4-5678-90ab-ccdef-11111EXAMPLE
        """
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        run_id: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=run_id,
        )
