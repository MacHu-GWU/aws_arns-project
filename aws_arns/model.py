# -*- coding: utf-8 -*-

import typing as T
import dataclasses

from . import compat


def _handle_empty_str(s: str) -> T.Optional[str]:
    if s:
        return s
    else:
        return None


def _handle_none(s: T.Optional[str]) -> str:
    if s is None:
        return ""
    else:
        return s


@dataclasses.dataclass
class Arn:
    """
    Amazon Resource Names (ARNs) data model. is a unique identifier for AWS resources.

    ARN format::

        - format: arn:partition:service:region:account-id:resource-id
        - example: arn:aws:sqs:us-east-1:111122223333:my-queue
        - format: arn:partition:service:region:account-id:resource-type/resource-id
        - example: arn:aws:iam::111122223333:role/aws-service-role/batch.amazonaws.com/AWSServiceRoleForBatch
        - format: arn:partition:service:region:account-id:resource-type:resource-id
        - example: arn:aws:batch:us-east-1:111122223333:job-definition/my-job-def:1

    Reference:

    - Amazon Resource Names (ARNs): https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html
    """

    partition: str = dataclasses.field()
    service: str = dataclasses.field()
    region: T.Optional[str] = dataclasses.field()
    account_id: T.Optional[str] = dataclasses.field()
    resource_type: T.Optional[str] = dataclasses.field()
    resource_id: str = dataclasses.field()
    sep: T.Optional[str] = dataclasses.field()

    @classmethod
    def new(
        cls,
        service: str,
        resource_id: str,
        partition: str = "aws",
        region: T.Optional[str] = None,
        account_id: T.Optional[str] = None,
        resource_type: T.Optional[str] = None,
        sep: T.Optional[str] = None,
    ):
        """
        new 这个构造器的目的是为了方便创建一个 Arn 对象.
        """
        return cls(
            service=service,
            resource_id=resource_id,
            partition=partition,
            region=region,
            account_id=account_id,
            resource_type=resource_type,
            sep=sep,
        )

    @classmethod
    def from_arn(cls, arn: str) -> "Arn":
        """
        parse arn string into Arn object.
        """
        if not arn.startswith("arn:"):
            raise ValueError(f"Invalid ARN: {arn!r}")

        _, partition, service, region, account_id, resource = arn.split(":", 5)

        if "/" in resource:
            sep = "/"
            resource_type, resource_id = resource.split("/", 1)
        elif ":" in resource:
            sep = ":"
            resource_type, resource_id = resource.split(":", 1)
        else:
            sep = None
            resource_type, resource_id = None, resource

        return cls(
            partition=partition,
            service=service,
            region=_handle_empty_str(region),
            account_id=_handle_empty_str(account_id),
            resource_id=resource_id,
            resource_type=resource_type,
            sep=sep,
        )

    def to_arn(self) -> str:
        """
        convert Arn object into arn string.
        """
        if self.sep:
            resource = f"{self.resource_type}{self.sep}{self.resource_id}"
        else:
            resource = self.resource_id
        return f"arn:{self.partition}:{self.service}:{_handle_none(self.region)}:{_handle_none(self.account_id)}:{resource}"


@dataclasses.dataclass
class CrossAccountGlobal(Arn):
    """
    No account, no region. Example:

    - AWS S3
    """

    @classmethod
    def new(
        cls,
        service: str,
        resource_id: str,
        partition: str = "aws",
        resource_type: T.Optional[str] = None,
        sep: T.Optional[str] = None,
    ):
        return super(CrossAccountGlobal, cls).new(
            partition=partition,
            service=service,
            region=None,
            account_id=None,
            resource_id=resource_id,
            resource_type=resource_type,
            sep=sep,
        )


@dataclasses.dataclass
class Global(Arn):
    """
    No region. Example:

    - AWS IAM
    - AWS Route53
    """

    @classmethod
    def new(
        cls,
        service: str,
        resource_id: str,
        account_id: str,
        partition: str = "aws",
        resource_type: T.Optional[str] = None,
        sep: T.Optional[str] = None,
    ):
        return super(Global, cls).new(
            partition=partition,
            service=service,
            region=None,
            account_id=account_id,
            resource_id=resource_id,
            resource_type=resource_type,
            sep=sep,
        )


@dataclasses.dataclass
class Regional(Arn):
    """
    Normal regional resources. Example:

    - AWS SQS
    - AWS Lambda
    """

    @classmethod
    def new(
        cls,
        service: str,
        resource_id: str,
        region: str,
        account_id: str,
        partition: str = "aws",
        resource_type: T.Optional[str] = None,
        sep: T.Optional[str] = None,
    ):
        return super(Regional, cls).new(
            partition=partition,
            service=service,
            region=region,
            account_id=account_id,
            resource_id=resource_id,
            resource_type=resource_type,
            sep=sep,
        )


@dataclasses.dataclass
class ResourceIdOnlyRegional(Arn):
    """
    Only one resource type in this service. Example:

    - AWS SQS
    - AWS SNS
    """

    @classmethod
    def new(
        cls,
        service: str,
        resource_id: str,
        region: str,
        account_id: str,
        partition: str = "aws",
    ):
        return super(ResourceIdOnlyRegional, cls).new(
            partition=partition,
            service=service,
            region=region,
            account_id=account_id,
            resource_id=resource_id,
            resource_type=None,
            sep=None,
        )


@dataclasses.dataclass
class ColonSeparatedRegional(Arn):
    """
    Example:

    - AWS Lambda
    """

    @classmethod
    def new(
        cls,
        service: str,
        resource_id: str,
        region: str,
        account_id: str,
        partition: str = "aws",
        resource_type: T.Optional[str] = None,
    ):
        return super(ColonSeparatedRegional, cls).new(
            partition=partition,
            service=service,
            region=region,
            account_id=account_id,
            resource_id=resource_id,
            resource_type=resource_type,
            sep=":",
        )


@dataclasses.dataclass
class SlashSeparatedRegional(Arn):
    """
    Example:

    - AWS CloudFormation
    """

    @classmethod
    def new(
        cls,
        service: str,
        resource_id: str,
        region: str,
        account_id: str,
        partition: str = "aws",
        resource_type: T.Optional[str] = None,
    ):
        return super(SlashSeparatedRegional, cls).new(
            partition=partition,
            service=service,
            region=region,
            account_id=account_id,
            resource_id=resource_id,
            resource_type=resource_type,
            sep="/",
        )
