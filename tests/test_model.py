# -*- coding: utf-8 -*-

import pytest

from aws_arns.model import Arn
from aws_arns.tests.test_arns import arns


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

        arn.with_cn_partition()
        assert arn.partition == "aws-cn"

        arn.with_us_gov_partition()
        assert arn.partition == "aws-us-gov"

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

        arn = Arn.from_arn(
            "arn:aws:sns:us-east-1:111122223333:my_topic:a07e1034-10c0-47a6-83c2-552cfcca42db"
        )
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

        with pytest.raises(ValueError):
            Arn()


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.model", preview=False)
