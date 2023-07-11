# -*- coding: utf-8 -*-

import dataclasses
from ..model import Global


@dataclasses.dataclass
class Iam(Global):
    @classmethod
    def new(
        cls,
        aws_account_id: str,
        resource_type: str,
        name: str,
    ):
        return super(Iam, cls).new(
            partition="aws",
            service="iam",
            account_id=aws_account_id,
            resource_id=name,
            resource_type=resource_type,
            sep="/",
        )

    @property
    def short_name(self) -> str:
        return self.resource_id.split("/")[-1]


@dataclasses.dataclass
class IamGroup(Iam):
    """
    Example: arn:aws:iam::111122223333:group/Admin
    """
    @property
    def iam_group_name(self) -> str:
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        name: str,
    ) -> "IamGroup":
        return super(IamGroup, cls).new(
            aws_account_id=aws_account_id,
            resource_type="group",
            name=name,
        )


@dataclasses.dataclass
class IamUser(Iam):
    """
    Example: arn:aws:iam::111122223333:user/alice
    """
    @property
    def iam_user_name(self) -> str:
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        name: str,
    ) -> "IamUser":
        return super(IamUser, cls).new(
            aws_account_id=aws_account_id,
            resource_type="user",
            name=name,
        )


@dataclasses.dataclass
class IamRole(Iam):
    """
    Example: arn:aws:iam::111122223333:role/aws-service-role/batch.amazonaws.com/AWSServiceRoleForBatch
    """
    @property
    def iam_role_name(self) -> str:
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        name: str,
    ) -> "IamRole":
        return super(IamRole, cls).new(
            aws_account_id=aws_account_id,
            resource_type="role",
            name=name,
        )

    def is_service_role(self) -> bool:
        return self.iam_role_name.startswith("aws-service-role")


@dataclasses.dataclass
class IamPolicy(Iam):
    """
    Example: arn:aws:iam::111122223333:policy/service-role/codebuild-policy
    """
    @property
    def iam_policy_name(self) -> str:
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        name: str,
    ) -> "IamPolicy":
        return super(IamPolicy, cls).new(
            aws_account_id=aws_account_id,
            resource_type="policy",
            name=name,
        )


@dataclasses.dataclass
class IamInstanceProfile(Iam):
    """
    Example: arn:aws:iam::111122223333:instance-profile/cloud9/AWSCloud9SSMInstanceProfile
    """
    @property
    def iam_instance_profile_name(self) -> str:
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        name: str,
    ) -> "IamInstanceProfile":
        return super(IamInstanceProfile, cls).new(
            aws_account_id=aws_account_id,
            resource_type="instance-profile",
            name=name,
        )
