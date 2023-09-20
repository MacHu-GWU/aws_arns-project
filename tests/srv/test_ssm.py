# -*- coding: utf-8 -*-

from aws_arns.srv.ssm import (
    SSMParameter,
)


def test():
    arn1 = "arn:aws:ssm:us-east-1:807388292768:parameter/my_param"
    arn2 = "arn:aws:ssm:us-east-1:807388292768:parameter/path/to/my_param"
    param1 = SSMParameter.from_arn(arn1)
    assert param1.parameter_name == "my_param"
    param2 = SSMParameter.from_arn(arn2)
    assert param2.parameter_name == "/path/to/my_param"

    assert (
        SSMParameter.new(
            aws_account_id=param1.account_id,
            aws_region=param1.region,
            name=param1.parameter_name,
        )
        == param1
    )
    assert (
        SSMParameter.new(
            aws_account_id=param2.account_id,
            aws_region=param2.region,
            name=param2.parameter_name,
        )
        == param2
    )


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.srv.ssm", preview=False)
