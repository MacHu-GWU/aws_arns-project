# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import dataclasses

from ..model import _SlashSeparatedRegional, _ResourceIdOnlyRegional


@dataclasses.dataclass
class Kinesis(_SlashSeparatedRegional):
    service: str = dataclasses.field(default="kinesis")


@dataclasses.dataclass
class KinesisStream(Kinesis):
    """
    Example: arn:aws:kinesis:us-east-1:111122223333:stream/my_stream
    """

    resource_type: str = dataclasses.field(default="stream")

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        stream_name: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=stream_name,
        )

    @property
    def stream_name(self) -> str:
        return self.resource_id


@dataclasses.dataclass
class KinesisStreamConsumer(_ResourceIdOnlyRegional):
    """
    Example: arn:aws:kinesis:us-east-1:111122223333:my_stream_type/stream_name/consumer/consumer_name:creation_timestamp
    """

    service: str = dataclasses.field(default="kinesis")
    resource_type: str = dataclasses.field(default="stream")

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        stream_type: str,
        stream_name: str,
        consumer_name: str,
        consumer_creation_timestamp: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=f"{stream_type}/{stream_name}/consumer/{consumer_name}:{consumer_creation_timestamp}",
        )

    @property
    def stream_type(self) -> str:
        return self.resource_id.split("/")[0]

    @property
    def stream_name(self) -> str:
        return self.resource_id.split("/")[1]

    @property
    def consumer_name(self) -> str:
        return self.resource_id.split("/")[3].split(":")[0]

    @property
    def consumer_creation_timestamp(self) -> str:
        return self.resource_id.split("/")[3].split(":")[1]


@dataclasses.dataclass
class KinesisFirehose(_SlashSeparatedRegional):
    service: str = dataclasses.field(default="firehose")


@dataclasses.dataclass
class KinesisFirehoseDeliveryStream(KinesisFirehose):
    """
    Example: arn:aws:firehose:us-east-1:111122223333:deliverystream/my_delivery_stream
    """

    resource_type: str = dataclasses.field(default="deliverystream")

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        stream_name: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=stream_name,
        )

    @property
    def stream_name(self) -> str:
        return self.resource_id


@dataclasses.dataclass
class KinesisAnalytics(_SlashSeparatedRegional):
    service: str = dataclasses.field(default="kinesisanalytics")


@dataclasses.dataclass
class KinesisAnalyticsApplication(KinesisFirehose):
    """
    Example: arn:aws:kinesisanalytics:us-east-1:111122223333:application/my_application
    """

    resource_type: str = dataclasses.field(default="application")

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        app_name: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=app_name,
        )

    @property
    def app_name(self) -> str:
        return self.resource_id


@dataclasses.dataclass
class KinesisVideo(_SlashSeparatedRegional):
    service: str = dataclasses.field(default="kinesisvideo")


@dataclasses.dataclass
class KinesisVideoChannel(KinesisVideo):
    """
    Example: arn:aws:kinesisvideo:us-east-1:414570653400:channel/my_channel_name/creation_time
    """

    resource_type: str = dataclasses.field(default="channel")

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        channel_name: str,
        creation_time: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=f"{channel_name}/{creation_time}",
        )

    @property
    def channel_name(self) -> str:
        return self.resource_id.split("/")[0]

    @property
    def creation_time(self) -> str:
        return self.resource_id.split("/")[1]


@dataclasses.dataclass
class KinesisVideoStream(KinesisVideo):
    """
    Example: arn:aws:kinesisvideo:us-east-1:414570653400:stream/my_stream_name/creation_time
    """

    resource_type: str = dataclasses.field(default="stream")

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        stream_name: str,
        creation_time: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=f"{stream_name}/{creation_time}",
        )

    @property
    def stream_name(self) -> str:
        return self.resource_id.split("/")[0]

    @property
    def creation_time(self) -> str:
        return self.resource_id.split("/")[1]
