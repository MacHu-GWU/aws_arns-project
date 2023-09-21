# -*- coding: utf-8 -*-

from aws_arns.srv.secretmanager import (
    SecretManagerSecret,
)


def test():
    arn = "arn:aws:secretsmanager:us-east-1:111122223333:secret:MyFolder/MySecret-a1b2c3"
    secret = SecretManagerSecret.from_arn(arn)
    assert secret.secret_name == "MyFolder/MySecret"
    assert secret.long_name == "MyFolder/MySecret-a1b2c3"
    assert secret.resource_id == "MyFolder/MySecret-a1b2c3"
    assert (
        SecretManagerSecret.new(
            aws_account_id=secret.account_id,
            aws_region=secret.region,
            long_name=secret.long_name,
        )
        == secret
    )

if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.srv.secretmanager", preview=False)
