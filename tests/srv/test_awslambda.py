# -*- coding: utf-8 -*-

import pytest

from aws_arns.srv.awslambda import (
    LambdaFunction,
    LambdaLayer,
)


def test():
    arn = "arn:aws:lambda:us-east-1:111122223333:function:my_func"
    arn_version = "arn:aws:lambda:us-east-1:111122223333:function:my_func:1"
    arn_alias = "arn:aws:lambda:us-east-1:111122223333:function:my_func:LIVE"

    lbd = LambdaFunction.from_arn(arn)
    assert lbd.name == "my_func"
    assert lbd.function_name == "my_func"
    assert lbd.version == None
    assert lbd.alias == None
    assert (
        LambdaFunction.new(
            aws_account_id=lbd.account_id,
            aws_region=lbd.region,
            name=lbd.name,
        )
        == lbd
    )

    lbd_version = LambdaFunction.from_arn(arn_version)
    assert lbd_version.name == "my_func"
    assert lbd_version.function_name == "my_func"
    assert lbd_version.version == "1"
    with pytest.raises(Exception):
        _ = lbd_version.alias
    assert (
        LambdaFunction.new(
            aws_account_id=lbd_version.account_id,
            aws_region=lbd_version.region,
            name=lbd_version.name,
            version=lbd_version.version,
        )
        == lbd_version
    )

    lbd_alias = LambdaFunction.from_arn(arn_alias)
    assert lbd_alias.name == "my_func"
    assert lbd_alias.function_name == "my_func"
    with pytest.raises(Exception):
        _ = lbd_alias.version
    assert lbd_alias.alias == "LIVE"
    assert (
        LambdaFunction.new(
            aws_account_id=lbd_alias.account_id,
            aws_region=lbd_alias.region,
            name=lbd_alias.name,
            alias=lbd_alias.alias,
        )
        == lbd_alias
    )

    layer_arn = "arn:aws:lambda:us-east-1:111122223333:layer:my_layer:1"
    lbd_layer = LambdaLayer.from_arn(layer_arn)
    assert lbd_layer.name == "my_layer"
    assert lbd_layer.layer_name == "my_layer"
    assert lbd_layer.version == 1
    assert (
        LambdaLayer.new(
            aws_account_id=lbd_layer.account_id,
            aws_region=lbd_layer.region,
            name=lbd_layer.name,
            version=lbd_layer.version,
        )
        == lbd_layer
    )


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.srv.awslambda", preview=False)
