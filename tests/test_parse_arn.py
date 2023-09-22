# -*- coding: utf-8 -*-

from aws_arns.tests.test_arns import arns
from aws_arns.model import is_arn_instance
from aws_arns.parse_arn import parse_arn

def test():
    for arn in arns:
        obj = parse_arn(arn)
        assert is_arn_instance(obj) is True


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.parse_arn", preview=False)