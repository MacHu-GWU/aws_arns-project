# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import dataclasses

from ..model import _SlashSeparatedRegional


@dataclasses.dataclass
class Batch(_SlashSeparatedRegional):
    service: str = dataclasses.field(default="batch")

    @property
    def name(self) -> str:
        return self.resource_id


@dataclasses.dataclass
class BatchComputeEnvironment(Batch):
    """
    Example: arn:aws:batch:us-east-1:111122223333:compute-environment/my-ce
    """

    resource_type: str = dataclasses.field(default="compute-environment")

    @property
    def batch_compute_environment_name(self) -> str:
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        name: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=name,
        )


@dataclasses.dataclass
class BatchJobQueue(Batch):
    """
    Example: arn:aws:batch:us-east-1:111122223333:job-queue/my-queue
    """

    resource_type: str = dataclasses.field(default="job-queue")

    @property
    def batch_job_queue_name(self) -> str:
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        name: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=name,
        )


@dataclasses.dataclass
class BatchJobDefinition(Batch):
    """
    Example: arn:aws:batch:us-east-1:111122223333:job-definition/my-job-def:1
    """

    resource_type: str = dataclasses.field(default="job-definition")

    @property
    def batch_job_definition_fullname(self) -> str:
        return self.resource_id

    @property
    def batch_job_definition_name(self) -> str:
        return self.resource_id.split(":")[0]

    @property
    def batch_job_definition_revision(self) -> int:
        return int(self.resource_id.split(":")[1])

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        name: str,
        revision: int,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=f"{name}:{revision}",
        )


@dataclasses.dataclass
class BatchJob(Batch):
    """
    Example: arn:aws:batch:us-east-1:111122223333:job/a974ee84-1da8-40bf-bca9-ef4253fac3c6
    """

    resource_type: str = dataclasses.field(default="job")

    @property
    def batch_job_id(self) -> str:
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        job_id: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=job_id,
        )


@dataclasses.dataclass
class BatchSchedulingPolicy(Batch):
    """
    Example: arn:aws:batch:us-east-1:111122223333:scheduling-policy/my-policy
    """

    resource_type: str = dataclasses.field(default="scheduling-policy")

    @property
    def batch_scheduling_policy_name(self) -> str:
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        name: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=name,
        )
