# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import dataclasses

from ..model import _ColonSeparatedRegional


@dataclasses.dataclass
class CloudWatchLogs(_ColonSeparatedRegional):
    service: str = dataclasses.field(default="logs")


@dataclasses.dataclass
class CloudWatchLogGroup(CloudWatchLogs):
    """
    Example: arn:aws:logs:us-east-1:111122223333:log-group:/aws/lambda/my-func:*
    """

    resource_type: str = dataclasses.field(default="log-group")

    @property
    def log_group_name(self) -> str:
        """
        The "/aws/lambda/my-func:*" part of
        arn:aws:logs:us-east-1:111122223333:log-group:/aws/lambda/my-func:*
        """
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        log_group_name: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=log_group_name,
        )


@dataclasses.dataclass
class CloudWatchLogGroupStream(CloudWatchLogs):
    """
    Example: arn:aws:logs:us-east-1:111122223333:log-group:/aws/lambda/my-func:*
    """

    resource_type: str = dataclasses.field(default="log-group")

    @property
    def log_group_name(self) -> str:
        """
        The "my-log-group*" part of
        arn:aws:logs:us-east-1:111122223333:log-group:my-log-group*:log-stream:my-log-stream*
        """
        return self.resource_id.split(":", 2)[0]

    @property
    def stream_name(self) -> str:
        """
        The "my-log-stream*" part of
        arn:aws:logs:us-east-1:111122223333:log-group:my-log-group*:log-stream:my-log-stream*
        """
        return self.resource_id.split(":", 2)[2]

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        log_group_name: str,
        stream_name: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=f"{log_group_name}:log-stream:{stream_name}",
        )
