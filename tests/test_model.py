# -*- coding: utf-8 -*-

import pytest
import itertools
from aws_arns.model import (
    Arn,
    CrossAccountGlobal,
    Global,
    Regional,
    ResourceIdOnlyRegional,
    ColonSeparatedRegional,
    SlashSeparatedRegional,
)

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

lambda_func = [
    "arn:aws:lambda:us-east-1:111122223333:function:my-func",
    "arn:aws:lambda:us-east-1:111122223333:function:my-func:LIVE",
    "arn:aws:lambda:us-east-1:111122223333:function:my-func:1",
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
        lambda_func,
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


class TestCrossAccountGlobal:
    def test(self):
        s3_bucket = CrossAccountGlobal.new(
            service="s3",
            resource_id="my-bucket",
        )
        arn = "arn:aws:s3:::my-bucket"
        assert s3_bucket.to_arn() == arn

        s3_bucket_1 = CrossAccountGlobal.from_arn(arn)
        for thing in [s3_bucket, s3_bucket_1]:
            assert thing.service == "s3"
            assert thing.region == None
            assert thing.account_id == None
            assert thing.resource_type == None
            assert thing.resource_id == "my-bucket"
            assert thing.sep == None


class TestGlobal:
    def test(self):
        iam_role = Global.new(
            service="iam",
            resource_id="my-role",
            account_id="111122223333",
        )
        arn = "arn:aws:iam::111122223333:my-role"
        assert iam_role.to_arn() == arn

        iam_role_1 = Global.from_arn(arn)
        for thing in [iam_role, iam_role_1]:
            assert thing.service == "iam"
            assert thing.region == None
            assert thing.account_id == "111122223333"
            assert thing.resource_type == None
            assert thing.resource_id == "my-role"
            assert thing.sep == None


class TestRegional:
    def test(self):
        lbd_func = Regional.new(
            service="lambda",
            resource_id="my-func",
            region="us-east-1",
            account_id="111122223333",
            resource_type="function",
            sep=":",
        )
        assert lbd_func.aws_region == "us-east-1"
        assert lbd_func.aws_account_id == "111122223333"
        arn = "arn:aws:lambda:us-east-1:111122223333:function:my-func"
        assert lbd_func.to_arn() == arn

        lbd_func_1 = Regional.from_arn(arn)
        for thing in [lbd_func, lbd_func_1]:
            assert thing.service == "lambda"
            assert thing.region == "us-east-1"
            assert thing.account_id == "111122223333"
            assert thing.resource_type == "function"
            assert thing.resource_id == "my-func"
            assert thing.sep == ":"


class TestResourceIdOnlyRegional:
    def test(self):
        sns_topic = ResourceIdOnlyRegional.new(
            service="sns",
            resource_id="my-topic",
            region="us-east-1",
            account_id="111122223333",
        )
        arn = "arn:aws:sns:us-east-1:111122223333:my-topic"
        assert sns_topic.to_arn() == arn

        sns_topic_1 = ResourceIdOnlyRegional.from_arn(arn)
        for thing in [sns_topic, sns_topic_1]:
            assert thing.service == "sns"
            assert thing.region == "us-east-1"
            assert thing.account_id == "111122223333"
            assert thing.resource_type == None
            assert thing.resource_id == "my-topic"
            assert thing.sep == None


class TestColonSeparatedRegional:
    def test(self):
        lbd_func = ColonSeparatedRegional.new(
            service="lambda",
            resource_id="my-func",
            region="us-east-1",
            account_id="111122223333",
            resource_type="function",
        )
        arn = "arn:aws:lambda:us-east-1:111122223333:function:my-func"
        assert lbd_func.to_arn() == arn

        lbd_func_1 = ColonSeparatedRegional.from_arn(arn)
        for thing in [lbd_func, lbd_func_1]:
            assert thing.service == "lambda"
            assert thing.region == "us-east-1"
            assert thing.account_id == "111122223333"
            assert thing.resource_type == "function"
            assert thing.resource_id == "my-func"
            assert thing.sep == ":"


class TestSlashSeparatedRegional:
    def test(self):
        cf_stack = SlashSeparatedRegional.new(
            service="cloudformation",
            resource_id="my-stack",
            region="us-east-1",
            account_id="111122223333",
            resource_type="stack",
        )
        arn = "arn:aws:cloudformation:us-east-1:111122223333:stack/my-stack"
        assert cf_stack.to_arn() == arn

        cf_stack_1 = SlashSeparatedRegional.from_arn(arn)
        for thing in [cf_stack, cf_stack_1]:
            assert thing.service == "cloudformation"
            assert thing.region == "us-east-1"
            assert thing.account_id == "111122223333"
            assert thing.resource_type == "stack"
            assert thing.resource_id == "my-stack"
            assert thing.sep == "/"


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.model", preview=False)
