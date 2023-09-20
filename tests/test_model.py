# -*- coding: utf-8 -*-

import pytest
import itertools
from aws_arns.model import Arn

a2i = [
    "arn:aws:sagemaker:us-east-1:111122223333:flow-definition/my_flow",
    "arn:aws:sagemaker:us-east-1:111122223333:human-loop/1a2b3c",
    "arn:aws:sagemaker:us-east-1:111122223333:human-task-ui/my-ui",
]

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
    "arn:aws:lambda:us-east-1:111122223333:layer:my-layer:1",
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
    "arn:aws:batch:us-east-1:111122223333:compute-environment/test",
    "arn:aws:batch:us-east-1:111122223333:job-queue/test",
    "arn:aws:batch:us-east-1:111122223333:job-definition/test:1",
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

codecommit = [
    "arn:aws:codecommit:us-east-1:111122223333:test",
    "arn:aws:codebuild:us-east-1:111122223333:project/test",
    "arn:aws:codebuild:us-east-1:111122223333:build/test:08805851-8a0a-4968-9d08-c7cc0623db7b",
    "arn:aws:codepipeline:us-east-1:111122223333:test",
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


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.model", preview=False)
