# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import dataclasses
from ..model import _Global


@dataclasses.dataclass
class Iam(_Global):
    service: str = dataclasses.field(default="iam")
    sep: str = dataclasses.field(default="/")

    @property
    def short_name(self) -> str:
        return self.resource_id.split("/")[-1]


@dataclasses.dataclass
class IamGroup(Iam):
    """
    Example: arn:aws:iam::111122223333:group/Admin
    """

    resource_type: str = dataclasses.field(default="group")

    @property
    def iam_group_name(self) -> str:
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        name: str,
    ):
        return cls(
            account_id=aws_account_id,
            resource_id=name,
        )


@dataclasses.dataclass
class IamUser(Iam):
    """
    Example: arn:aws:iam::111122223333:user/alice
    """

    resource_type: str = dataclasses.field(default="user")

    @property
    def iam_user_name(self) -> str:
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        name: str,
    ) -> "IamUser":
        return cls(
            account_id=aws_account_id,
            resource_id=name,
        )


@dataclasses.dataclass
class IamRole(Iam):
    """
    Example: arn:aws:iam::111122223333:role/aws-service-role/batch.amazonaws.com/AWSServiceRoleForBatch
    """

    resource_type: str = dataclasses.field(default="role")

    @property
    def iam_role_name(self) -> str:
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        name: str,
    ) -> "IamRole":
        return cls(
            account_id=aws_account_id,
            resource_id=name,
        )

    def is_service_role(self) -> bool:
        return self.iam_role_name.startswith("aws-service-role")


@dataclasses.dataclass
class IamPolicy(Iam):
    """
    Example: arn:aws:iam::111122223333:policy/service-role/codebuild-policy
    """

    resource_type: str = dataclasses.field(default="policy")

    @property
    def iam_policy_name(self) -> str:
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        name: str,
    ) -> "IamPolicy":
        return cls(
            account_id=aws_account_id,
            resource_id=name,
        )


@dataclasses.dataclass
class IamInstanceProfile(Iam):
    """
    Example: arn:aws:iam::111122223333:instance-profile/cloud9/AWSCloud9SSMInstanceProfile
    """

    resource_type: str = dataclasses.field(default="instance-profile")

    @property
    def iam_instance_profile_name(self) -> str:
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        name: str,
    ) -> "IamInstanceProfile":
        return cls(
            account_id=aws_account_id,
            resource_id=name,
        )
