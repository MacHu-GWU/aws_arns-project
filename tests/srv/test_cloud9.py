# -*- coding: utf-8 -*-

from aws_arns.srv.cloud9 import (
    _Cloud9Common,
    Cloud9Environment,
)


def test():
    class_and_arn_pairs = [
        (
            Cloud9Environment,
            "arn:aws:cloud9:us-east-1:111122223333:environment:my_environment",
        ),
    ]
    for class_, arn in class_and_arn_pairs:
        obj: _Cloud9Common = class_.from_arn(arn)
        assert obj.to_arn() == arn
        assert (
            class_.new(
                aws_account_id=obj.aws_account_id,
                aws_region=obj.aws_region,
                resource_id=obj.resource_id,
            )
            == obj
        )
        assert obj.name == obj.resource_id


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.srv.cloud9", preview=False)
