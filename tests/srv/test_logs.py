# -*- coding: utf-8 -*-

from aws_arns.srv.logs import (
    CloudWatchLogGroup,
    CloudWatchLogGroupStream,
)


def test():
    arn = "arn:aws:logs:us-east-1:111122223333:log-group:/aws/lambda/my-func:*"
    log_group = CloudWatchLogGroup.from_arn(arn)
    assert log_group.log_group_name == "/aws/lambda/my-func:*"
    assert (
        CloudWatchLogGroup.new(
            aws_region=log_group.region,
            aws_account_id=log_group.account_id,
            log_group_name=log_group.log_group_name,
        )
        == log_group
    )

    arn = "arn:aws:logs:us-east-1:111122223333:log-group:my-log-group*:log-stream:my-log-stream*"
    log_stream = CloudWatchLogGroupStream.from_arn(arn)
    assert log_stream.log_group_name == "my-log-group*"
    assert log_stream.stream_name == "my-log-stream*"
    assert (
        CloudWatchLogGroupStream.new(
            aws_region=log_stream.region,
            aws_account_id=log_stream.account_id,
            log_group_name=log_stream.log_group_name,
            stream_name=log_stream.stream_name,
        )
        == log_stream
    )


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.srv.logs", preview=False)
