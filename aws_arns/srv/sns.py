# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import dataclasses

from ..model import _ResourceIdOnlyRegional


@dataclasses.dataclass
class Sns(_ResourceIdOnlyRegional):
    service: str = dataclasses.field(default="sns")


@dataclasses.dataclass
class SnsTopic(Sns):
    """
    Example: arn:aws:s3:::my-bucket
    """

    @property
    def topic_name(self) -> str:
        """
        SNS topic name
        """
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        topic_name: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=topic_name,
        )


@dataclasses.dataclass
class SnsSubscription(Sns):
    """
    Example: arn:aws:s3:::my-bucket
    """

    @property
    def topic_name(self) -> str:
        return self.resource_id.split(":", 1)[0]

    @property
    def subscription_id(self) -> str:
        return self.resource_id.split(":", 1)[1]

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        topic_name: str,
        subscription_id: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=f"{topic_name}:{subscription_id}",
        )
