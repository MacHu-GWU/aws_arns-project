# -*- coding: utf-8 -*-

import dataclasses
from ..model import Arn


@dataclasses.dataclass
class _Iam(Arn):
    @classmethod
    def _new(
        cls,
        aws_account_id: str,
        resource_type: str,
        name: str,
    ):
        return cls(
            partition="aws",
            service="iam",
            region=None,
            account_id=aws_account_id,
            resource_id=name,
            resource_type=resource_type,
            sep="/",
        )

    @property
    def short_name(self) -> str:
        return self.resource_id.split("/")[-1]


@dataclasses.dataclass
class IamGroup(_Iam):
    @property
    def iam_group_name(self) -> str:
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        name: str,
    ) -> "IamGroup":
        return cls._new(
            aws_account_id=aws_account_id,
            resource_type="group",
            name=name,
        )


@dataclasses.dataclass
class IamUser(_Iam):
    @property
    def iam_user_name(self) -> str:
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        name: str,
    ) -> "IamUser":
        return cls._new(
            aws_account_id=aws_account_id,
            resource_type="user",
            name=name,
        )


@dataclasses.dataclass
class IamRole(_Iam):
    @property
    def iam_role_name(self) -> str:
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        name: str,
    ) -> "IamRole":
        return cls._new(
            aws_account_id=aws_account_id,
            resource_type="role",
            name=name,
        )

    def is_service_role(self) -> bool:
        return self.iam_role_name.startswith("aws-service-role")


@dataclasses.dataclass
class IamPolicy(_Iam):
    @property
    def iam_policy_name(self) -> str:
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        name: str,
    ) -> "IamPolicy":
        return cls._new(
            aws_account_id=aws_account_id,
            resource_type="policy",
            name=name,
        )


@dataclasses.dataclass
class IamInstanceProfile(_Iam):
    @property
    def iam_instance_profile_name(self) -> str:
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        name: str,
    ) -> "IamInstanceProfile":
        return cls._new(
            aws_account_id=aws_account_id,
            resource_type="instance-profile",
            name=name,
        )
