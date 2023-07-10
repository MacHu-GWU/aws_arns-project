# -*- coding: utf-8 -*-

import pytest
import itertools
from aws_arns.model import Arn

cloudformation = [
    "arn:aws:cloudformation:us-east-1:111122223333:stack/stack-name/8e6db190-bd6a-11ed-b80d-12cc1b6777a1",
    "arn:aws:cloudformation:us-east-1:111122223333:changeSet/stack-name-2023-03-08-04-42-38-564/5be009b1-f057-44b0-a5e3-cd9bf4a24b9e",
    "arn:aws:cloudformation:us-east-1:111122223333:stackset/stack-name:08af3d48-ec8e-45ad-b109-363d27fcf851",
]

kinesis = [
    "arn:aws:kinesisvideo:us-east-1:111122223333:stream/kinesis-stream-name/111122223333",
]

cloudwatch_logs = [
    "arn:aws:logs:us-east-1:111122223333:log-group:/aws/lambda/my-func:*",
    "arn:aws:logs:us-east-1:111122223333:log-group:my-log-group*:log-stream:my-log-stream*",
]

macie = [
    "arn:aws:macie:us-east-1:111122223333:trigger/example0954663fda0f652e304dcc21323508db/alert/example09214d3e70fb6092cc93cee96dbc4de6",
]

s3 = [
    "arn:aws:s3:::my-bucket",
    "arn:aws:s3:::my-bucket/cloudformation/upload/10f3db7bcfa62c69e5a71fef595fac84.json",
]

ec2 = [
    "arn:aws:ec2:us-east-1:111122223333:instance/*",
]

apigateway = [
    "arn:aws:apigateway:us-east-1::7540694639748281fa84fabba58e57c0:/test/mydemoresource/*",
]

sns = [
    "arn:aws:sns:*:111122223333:my_topic",
]

secretmanager = [
    "arn:aws:secretsmanager:us-east-1:111122223333:secret:MyFolder/MySecret-a1b2c3",
]

batch = [
    "arn:aws:batch:us-east-1:111122223333:job-definition/my-job:1",
]

arns = list(
    itertools.chain(
        cloudformation,
        kinesis,
        cloudwatch_logs,
        macie,
        s3,
        ec2,
        apigateway,
        sns,
        secretmanager,
        batch,
    )
)


def test_from_and_to():
    for arn_str in arns:
        arn = Arn.from_arn(arn_str)
        assert arn.to_arn() == arn_str


def test_error():
    with pytest.raises(ValueError):
        Arn.from_arn("hello")


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.model", preview=False)
