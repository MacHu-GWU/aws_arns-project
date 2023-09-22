# -*- coding: utf-8 -*-

from aws_arns.srv.kms import (
    KmsKey,
    KmsAlias,
)


def test():
    key_arn = "arn:aws:kms:us-east-1:111122223333:key/1a2b3c"
    alias_arn = "arn:aws:kms:us-east-1:111122223333:alias/my_key"
    key = KmsKey.from_arn(key_arn)
    alias = KmsAlias.from_arn(alias_arn)

    assert (
        KmsKey.new(
            aws_account_id=key.account_id,
            aws_region=key.region,
            key_id=key.key_id,
        )
        == key
    )
    assert (
        KmsAlias.new(
            aws_account_id=alias.account_id,
            aws_region=alias.region,
            alias=alias.alias,
        )
        == alias
    )


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.srv.kms", preview=False)
