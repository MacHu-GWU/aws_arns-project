# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import dataclasses

from ..model import _SlashSeparatedRegional


@dataclasses.dataclass
class CloudFormation(_SlashSeparatedRegional):
    service: str = dataclasses.field(default="cloudformation")


@dataclasses.dataclass
class CloudFormationStack(CloudFormation):
    """
    Example: arn:aws:cloudformation:us-east-1:111122223333:stack/my-stack/a1b2c3d4
    """
    resource_type: str = dataclasses.field(default="stack")

    @property
    def stack_name(self) -> str:
        """
        The "my-stack" part of
        arn:aws:cloudformation:us-east-1:111122223333:stack/my-stack/a1b2c3d4
        """
        return self.resource_id.split("/")[0]

    @property
    def short_id(self) -> str:
        """
        The "a1b2c3d4" part of
        arn:aws:cloudformation:us-east-1:111122223333:stack/my-stack/a1b2c3d4
        """
        return self.resource_id.split("/")[1]

    @property
    def stack_fullname(self) -> str:
        """
        The "my-stack/a1b2c3d4" part of
        arn:aws:cloudformation:us-east-1:111122223333:stack/my-stack/a1b2c3d4
        """
        return self.resource_id

    @property
    def stack_id(self) -> str:
        """
        It is the stack ARN.
        """
        return self.to_arn()

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        stack_name: str,
        short_id: str
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=f"{stack_name}/{short_id}",
        )


@dataclasses.dataclass
class CloudFormationChangeSet(CloudFormation):
    """
    Example: arn:aws:cloudformation:us-east-1:111122223333:changeSet/my-change-set/a1b2c3d4
    """
    resource_type: str = dataclasses.field(default="changeSet")

    @property
    def changeset_fullname(self) -> str:
        """
        The "my-change-set/a1b2c3d4" part of
        arn:aws:cloudformation:us-east-1:111122223333:changeSet/my-change-set/a1b2c3d4
        """
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        fullname: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=fullname,
        )


@dataclasses.dataclass
class CloudFormationStackSet(CloudFormation):
    """
    Example: arn:aws:cloudformation:us-east-1:111122223333:stackset/my-stackset:a1b2c3d4
    """
    resource_type: str = dataclasses.field(default="stackset")

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
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=fullname,
        )
