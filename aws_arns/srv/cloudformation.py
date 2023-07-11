# -*- coding: utf-8 -*-

import dataclasses

from ..model import SlashSeparatedRegional


@dataclasses.dataclass
class CloudFormation(SlashSeparatedRegional):
    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        fullname: str,
        resource_type: str,
    ):
        return super(CloudFormation, cls).new(
            partition="aws",
            service="cloudformation",
            region=aws_region,
            account_id=aws_account_id,
            resource_id=fullname,
            resource_type=resource_type,
        )


@dataclasses.dataclass
class CloudFormationStack(CloudFormation):
    """
    Example: arn:aws:cloudformation:us-east-1:111122223333:stack/my-stack/a1b2c3d4
    """

    @property
    def stack_name(self) -> str:
        return self.resource_id.split("/")[0]

    @property
    def stack_id(self) -> str:
        return self.resource_id.split("/")[1]

    @property
    def stack_fullname(self) -> str:
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        fullname: str,
    ):
        return super(CloudFormationStack, cls).new(
            aws_region=aws_region,
            aws_account_id=aws_account_id,
            fullname=fullname,
            resource_type="stack",
        )


@dataclasses.dataclass
class CloudFormationChangeSet(CloudFormation):
    """
    Example: arn:aws:cloudformation:us-east-1:111122223333:changeSet/my-change-set/a1b2c3d4
    """

    @property
    def changeset_fullname(self) -> str:
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        fullname: str,
    ):
        return super(CloudFormationChangeSet, cls).new(
            aws_region=aws_region,
            aws_account_id=aws_account_id,
            fullname=fullname,
            resource_type="changeSet",
        )


@dataclasses.dataclass
class CloudFormationStackSet(CloudFormation):
    """
    Example: arn:aws:cloudformation:us-east-1:111122223333:stackset/my-stackset:a1b2c3d4
    """

    @property
    def stackset_name(self) -> str:
        return self.resource_id.split(":")[0]

    @property
    def stackset_id(self) -> str:
        return self.resource_id.split(":")[1]

    @property
    def stackset_fullname(self) -> str:
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        fullname: str,
    ):
        return super(CloudFormationStackSet, cls).new(
            aws_region=aws_region,
            aws_account_id=aws_account_id,
            fullname=fullname,
            resource_type="stackset",
        )
