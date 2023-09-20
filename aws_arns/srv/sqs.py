# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import dataclasses

from ..model import _ResourceIdOnlyRegional


@dataclasses.dataclass
class Sqs(_ResourceIdOnlyRegional):
    service: str = dataclasses.field(default="sqs")


@dataclasses.dataclass
class SqsQueue(Sqs):
    """
    Example: arn:aws:sqs:us-east-1:111122223333:my_queue
    """

    @property
    def queue_name(self) -> str:
        """
        Queue short name, if it is fifo queue, it has to end with .fifo.
        """
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        queue_name: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=queue_name,
        )

    @property
    def queue_url(self) -> str:
        """
        Example: https://sqs.us-east-1.amazonaws.com/111122223333/my_queue
        """
        return (
            f"https://sqs.{self.aws_region}.amazonaws.com"
            f"/{self.aws_account_id}/{self.queue_name}"
        )

    @classmethod
    def from_queue_url(cls, url: str):
        """
        Parse a queue URL into an SQS object.
        """
        parts = url.split("/")
        aws_region = parts[2].split(".")[1]
        aws_account_id = parts[3]
        queue_name = parts[4]
        return cls.new(
            aws_account_id=aws_account_id,
            aws_region=aws_region,
            queue_name=queue_name,
        )
