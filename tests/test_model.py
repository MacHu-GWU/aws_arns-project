# -*- coding: utf-8 -*-

import pytest
import itertools
from aws_arns.model import Arn

cloudformation = [
    "arn:aws:cloudformation:us-east-1:111122223333:stack/my-stack/1a2b3c",
    "arn:aws:cloudformation:us-east-1:111122223333:changeSet/my-stack-name-2000-01-01/1a2b3c",
    "arn:aws:cloudformation:us-east-1:111122223333:stackset/my-stack-set:1a2b3c",
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
    "arn:aws:ec2:us-east-1:111122223333:instance/i-1234567890abcdef0",
    "arn:aws:ec2:us-east-1:111122223333:vpc/vpc-1234567890abcdef0",
    "arn:aws:ec2:us-east-1:111122223333:subnet/subnet-1234567890abcdef0",
    "arn:aws:ec2:us-east-1:111122223333:security-group/sg-1234567890abcdef0",
]

rds = [
    "arn:aws:rds:us-east-1:111122223333:db:my-mysql-instance-1",
    "arn:aws:rds:us-east-1:111122223333:cluster:my-aurora-cluster-1",
    "arn:aws:rds:us-east-1:111122223333:es:my-subscription",
    "arn:aws:rds:us-east-1:111122223333:og:my-og",
    "arn:aws:rds:us-east-1:111122223333:cluster-pg:my-cluster-param-timezone",
    "arn:aws:rds:us-east-1:111122223333:ri:my-reserved-postgresql",
    "arn:aws:rds:us-east-1:111122223333:secgrp:my-public",
    "arn:aws:rds:us-east-1:111122223333:snapshot:rds:my-mysql-db-2020-01-01-00-00",
    "arn:aws:rds:us-east-1:111122223333:snapshot:my-mysql-db-snap",
    "arn:aws:rds:us-east-1:111122223333:cluster-snapshot:my-aurora-cluster-snap",
    "arn:aws:rds:us-east-1:111122223333:subgrp:my-subnet-10",
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
    "arn:aws:sns:us-east-1:111122223333:my_topic",
    "arn:aws:sns:us-east-1:111122223333:my_topic:a07e1034-10c0-47a6-83c2-552cfcca42db",
]

sqs = [
    "arn:aws:sqs:us-east-1:111122223333:my_queue",
]

secretmanager = [
    "arn:aws:secretsmanager:us-east-1:111122223333:secret:MyFolder/MySecret-a1b2c3",
]

batch = [
    "arn:aws:batch:us-east-1:111122223333:compute-environment/acu_e5f245a1_test",
    "arn:aws:batch:us-east-1:111122223333:job-queue/acu_e5f245a1_test",
    "arn:aws:batch:us-east-1:111122223333:job-definition/acu_e5f245a1_test:1",
    "arn:aws:batch:us-east-1:111122223333:job/b2957570-6bae-47b1-a2d8-af4f3030fc36",
]

ecs = [
    "arn:aws:ecs:us-east-1:111122223333:cluster/AWSBatch-test-a1b2c3d4-a1b2-a1b2-a1b2-a1b2c3d4a1b2",
    "arn:aws:ecs:us-east-1:111122223333:task-definition/test:1",
]

glue = [
    "arn:aws:glue:us-east-1:111122223333:catalog",
    "arn:aws:glue:us-east-1:111122223333:database/db1",
    "arn:aws:glue:us-east-1:111122223333:table/db1/tbl1",
    "arn:aws:glue:us-east-1:111122223333:crawler/mycrawler",
    "arn:aws:glue:us-east-1:111122223333:job/testjob",
    "arn:aws:glue:us-east-1:111122223333:trigger/sampletrigger",
    "arn:aws:glue:us-east-1:111122223333:devEndpoint/temporarydevendpoint",
    "arn:aws:glue:us-east-1:111122223333:mlTransform/tfm-1234567890",
]

arns = list(
    itertools.chain(
        cloudformation,
        kinesis,
        cloudwatch_logs,
        macie,
        s3,
        ec2,
        rds,
        lambda_func,
        apigateway,
        sns,
        sqs,
        secretmanager,
        batch,
        ecs,
        glue,
    )
)


class TestArn:
    def test_specific(self):
        arn = Arn.from_arn("arn:aws:s3:::my-bucket")
        assert arn.partition == "aws"
        assert arn.service == "s3"
        assert arn.region == None
        assert arn.account_id == None
        assert arn.resource_type == None
        assert arn.resource_id == "my-bucket"
        assert arn.sep == None

        arn = Arn.from_arn("arn:aws:s3:::my-bucket/file.txt")
        assert arn.partition == "aws"
        assert arn.service == "s3"
        assert arn.region == None
        assert arn.account_id == None
        assert arn.resource_type == None
        assert arn.resource_id == "my-bucket/file.txt"
        assert arn.sep == None

        arn = Arn.from_arn("arn:aws:iam::111122223333:my-role")
        assert arn.partition == "aws"
        assert arn.service == "iam"
        assert arn.region == None
        assert arn.account_id == "111122223333"
        assert arn.resource_type == None
        assert arn.resource_id == "my-role"
        assert arn.sep == None

        arn = Arn.from_arn("arn:aws:sns:us-east-1:111122223333:my_topic:a07e1034-10c0-47a6-83c2-552cfcca42db")
        assert arn.partition == "aws"
        assert arn.service == "sns"
        assert arn.region == "us-east-1"
        assert arn.account_id == "111122223333"
        assert arn.resource_type == None
        assert arn.resource_id == "my_topic:a07e1034-10c0-47a6-83c2-552cfcca42db"
        assert arn.sep == None

        arn = Arn.from_arn("arn:aws:lambda:us-east-1:111122223333:function:my-func")
        assert arn.partition == "aws"
        assert arn.service == "lambda"
        assert arn.region == "us-east-1"
        assert arn.account_id == "111122223333"
        assert arn.resource_type == "function"
        assert arn.resource_id == "my-func"
        assert arn.sep == ":"

        arn = Arn.from_arn(
            "arn:aws:cloudformation:us-east-1:111122223333:stack/my-stack/1a2b3c"
        )
        assert arn.partition == "aws"
        assert arn.service == "cloudformation"
        assert arn.region == "us-east-1"
        assert arn.account_id == "111122223333"
        assert arn.resource_type == "stack"
        assert arn.resource_id == "my-stack/1a2b3c"
        assert arn.sep == "/"

        arn = Arn.from_arn(
            "arn:aws:cloudformation:us-east-1:111122223333:stackset/my-stack-set:1a2b3c",
        )
        assert arn.partition == "aws"
        assert arn.service == "cloudformation"
        assert arn.region == "us-east-1"
        assert arn.account_id == "111122223333"
        assert arn.resource_type == "stackset"
        assert arn.resource_id == "my-stack-set:1a2b3c"
        assert arn.sep == "/"


    def test_from_and_to(self):
        for arn_str in arns:
            arn = Arn.from_arn(arn_str)
            assert arn.to_arn() == arn_str

    def test_error(self):
        with pytest.raises(ValueError):
            Arn.from_arn("hello")


# class TestCrossAccountGlobal:
#     def test(self):
#         s3_bucket = CrossAccountGlobal.new(
#             service="s3",
#             resource_id="my-bucket",
#         )
#         arn = "arn:aws:s3:::my-bucket"
#         assert s3_bucket.to_arn() == arn
#
#         s3_bucket_1 = CrossAccountGlobal.from_arn(arn)
#         for thing in [s3_bucket, s3_bucket_1]:
#             assert thing.service == "s3"
#             assert thing.region == None
#             assert thing.account_id == None
#             assert thing.resource_type == None
#             assert thing.resource_id == "my-bucket"
#             assert thing.sep == None
#
#
# class TestGlobal:
#     def test(self):
#         iam_role = Global.new(
#             service="iam",
#             resource_id="my-role",
#             account_id="111122223333",
#         )
#         arn = "arn:aws:iam::111122223333:my-role"
#         assert iam_role.to_arn() == arn
#
#         iam_role_1 = Global.from_arn(arn)
#         for thing in [iam_role, iam_role_1]:
#             assert thing.service == "iam"
#             assert thing.region == None
#             assert thing.account_id == "111122223333"
#             assert thing.resource_type == None
#             assert thing.resource_id == "my-role"
#             assert thing.sep == None
#
#
# class TestRegional:
#     def test(self):
#         lbd_func = _Regional.new(
#             service="lambda",
#             resource_id="my-func",
#             region="us-east-1",
#             account_id="111122223333",
#             resource_type="function",
#             sep=":",
#         )
#         assert lbd_func.aws_region == "us-east-1"
#         assert lbd_func.aws_account_id == "111122223333"
#         arn = "arn:aws:lambda:us-east-1:111122223333:function:my-func"
#         assert lbd_func.to_arn() == arn
#
#         lbd_func_1 = _Regional.from_arn(arn)
#         for thing in [lbd_func, lbd_func_1]:
#             assert thing.service == "lambda"
#             assert thing.region == "us-east-1"
#             assert thing.account_id == "111122223333"
#             assert thing.resource_type == "function"
#             assert thing.resource_id == "my-func"
#             assert thing.sep == ":"
#
#
# class TestResourceIdOnlyRegional:
#     def test(self):
#         sns_topic = ResourceIdOnlyRegional.new(
#             service="sns",
#             resource_id="my-topic",
#             region="us-east-1",
#             account_id="111122223333",
#         )
#         arn = "arn:aws:sns:us-east-1:111122223333:my-topic"
#         assert sns_topic.to_arn() == arn
#
#         sns_topic_1 = ResourceIdOnlyRegional.from_arn(arn)
#         for thing in [sns_topic, sns_topic_1]:
#             assert thing.service == "sns"
#             assert thing.region == "us-east-1"
#             assert thing.account_id == "111122223333"
#             assert thing.resource_type == None
#             assert thing.resource_id == "my-topic"
#             assert thing.sep == None
#
#
# class TestColonSeparatedRegional:
#     def test(self):
#         lbd_func = ColonSeparatedRegional.new(
#             service="lambda",
#             resource_id="my-func",
#             region="us-east-1",
#             account_id="111122223333",
#             resource_type="function",
#         )
#         arn = "arn:aws:lambda:us-east-1:111122223333:function:my-func"
#         assert lbd_func.to_arn() == arn
#
#         lbd_func_1 = ColonSeparatedRegional.from_arn(arn)
#         for thing in [lbd_func, lbd_func_1]:
#             assert thing.service == "lambda"
#             assert thing.region == "us-east-1"
#             assert thing.account_id == "111122223333"
#             assert thing.resource_type == "function"
#             assert thing.resource_id == "my-func"
#             assert thing.sep == ":"
#
#
# class TestSlashSeparatedRegional:
#     def test(self):
#         cf_stack = SlashSeparatedRegional.new(
#             service="cloudformation",
#             resource_id="my-stack",
#             region="us-east-1",
#             account_id="111122223333",
#             resource_type="stack",
#         )
#         arn = "arn:aws:cloudformation:us-east-1:111122223333:stack/my-stack"
#         assert cf_stack.to_arn() == arn
#
#         cf_stack_1 = SlashSeparatedRegional.from_arn(arn)
#         for thing in [cf_stack, cf_stack_1]:
#             assert thing.service == "cloudformation"
#             assert thing.region == "us-east-1"
#             assert thing.account_id == "111122223333"
#             assert thing.resource_type == "stack"
#             assert thing.resource_id == "my-stack"
#             assert thing.sep == "/"


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.model", preview=False)
