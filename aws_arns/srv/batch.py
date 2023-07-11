# -*- coding: utf-8 -*-

import dataclasses

from ..model import SlashSeparatedRegional


@dataclasses.dataclass
class Batch(SlashSeparatedRegional):
    @property
    def name(self) -> str:
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        name: str,
        resource_type: str,
    ):
        return super(Batch, cls).new(
            partition="aws",
            service="batch",
            region=aws_region,
            account_id=aws_account_id,
            resource_id=name,
            resource_type=resource_type,
        )


@dataclasses.dataclass
class BatchComputeEnvironment(Batch):
    """
    Example: arn:aws:batch:us-east-1:111122223333:compute-environment/my-ce
    """
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
        return super(BatchComputeEnvironment, cls).new(
            aws_region=aws_region,
            aws_account_id=aws_account_id,
            name=name,
            resource_type="compute-environment",
        )


@dataclasses.dataclass
class BatchJobQueue(Batch):
    """
    Example: arn:aws:batch:us-east-1:111122223333:job-queue/my-queue
    """
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
        return super(BatchJobQueue, cls).new(
            aws_region=aws_region,
            aws_account_id=aws_account_id,
            name=name,
            resource_type="job-queue",
        )


@dataclasses.dataclass
class BatchJobDefinition(Batch):
    """
    Example: arn:aws:batch:us-east-1:111122223333:job-definition/my-job-def:1
    """
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
        return super(BatchJobDefinition, cls).new(
            aws_region=aws_region,
            aws_account_id=aws_account_id,
            name=f"{name}:{revision}",
            resource_type="job-definition",
        )


@dataclasses.dataclass
class BatchJob(Batch):
    """
    Example: arn:aws:batch:us-east-1:111122223333:job/a974ee84-1da8-40bf-bca9-ef4253fac3c6
    """
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
        return super(BatchJob, cls).new(
            aws_region=aws_region,
            aws_account_id=aws_account_id,
            name=job_id,
            resource_type="job",
        )


@dataclasses.dataclass
class BatchSchedulingPolicy(Batch):
    """
    Example: arn:aws:batch:us-east-1:111122223333:scheduling-policy/my-policy
    """
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
        return super(BatchSchedulingPolicy, cls).new(
            aws_region=aws_region,
            aws_account_id=aws_account_id,
            name=name,
            resource_type="scheduling-policy",
        )
