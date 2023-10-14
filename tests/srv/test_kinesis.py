# -*- coding: utf-8 -*-

from aws_arns.srv.kinesis import (
    KinesisStream,
    KinesisStreamConsumer,
    KinesisFirehoseDeliveryStream,
    KinesisAnalyticsApplication,
    KinesisVideoChannel,
    KinesisVideoStream,
)


def test():
    arn = "arn:aws:kinesis:us-east-1:111122223333:stream/my_stream"
    obj = KinesisStream.from_arn(arn)
    assert obj.stream_name == "my_stream"
    assert (
        KinesisStream.new(
            aws_account_id=obj.aws_account_id,
            aws_region=obj.aws_region,
            stream_name=obj.stream_name,
        )
        == obj
    )

    arn = "arn:aws:kinesis:us-east-1:111122223333:my_stream_type/my_stream_name/consumer/my_consumer_name:my_consumer_creation_timestamp"
    obj = KinesisStreamConsumer.from_arn(arn)
    assert obj.stream_type == "my_stream_type"
    assert obj.stream_name == "my_stream_name"
    assert obj.consumer_name == "my_consumer_name"
    assert obj.consumer_creation_timestamp == "my_consumer_creation_timestamp"
    assert (
        KinesisStreamConsumer.new(
            aws_account_id=obj.aws_account_id,
            aws_region=obj.aws_region,
            stream_type=obj.stream_type,
            stream_name=obj.stream_name,
            consumer_name=obj.consumer_name,
            consumer_creation_timestamp=obj.consumer_creation_timestamp,
        )
        == obj
    )

    arn = "arn:aws:firehose:us-east-1:111122223333:deliverystream/my_delivery_stream"
    obj = KinesisFirehoseDeliveryStream.from_arn(arn)
    assert obj.stream_name == "my_delivery_stream"
    assert (
        KinesisFirehoseDeliveryStream.new(
            aws_account_id=obj.aws_account_id,
            aws_region=obj.aws_region,
            stream_name=obj.stream_name,
        )
        == obj
    )

    arn = "arn:aws:kinesisanalytics:us-east-1:111122223333:application/my_application"
    obj = KinesisAnalyticsApplication.from_arn(arn)
    assert obj.app_name == "my_application"
    assert (
        KinesisAnalyticsApplication.new(
            aws_account_id=obj.aws_account_id,
            aws_region=obj.aws_region,
            app_name=obj.app_name,
        )
        == obj
    )

    arn = "arn:aws:kinesisvideo:us-east-1:111122223333:channel/my_channel_name/creation_time"
    obj = KinesisVideoChannel.from_arn(arn)
    assert obj.channel_name == "my_channel_name"
    assert obj.creation_time == "creation_time"
    assert (
        KinesisVideoChannel.new(
            aws_account_id=obj.aws_account_id,
            aws_region=obj.aws_region,
            channel_name=obj.channel_name,
            creation_time=obj.creation_time,
        )
        == obj
    )

    arn = "arn:aws:kinesisvideo:us-east-1:111122223333:stream/my_stream_name/creation_time"
    obj = KinesisVideoStream.from_arn(arn)
    assert obj.stream_name == "my_stream_name"
    assert obj.creation_time == "creation_time"
    assert (
        KinesisVideoStream.new(
            aws_account_id=obj.aws_account_id,
            aws_region=obj.aws_region,
            stream_name=obj.stream_name,
            creation_time=obj.creation_time,
        )
        == obj
    )


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.srv.kinesis", preview=False)
