# -*- coding: utf-8 -*-
import pytest

from aws_arns.srv.efs import (
    _EFSCommon,
    EFSAccessPoint,
    EFSFileSystem,
)


def test():
    class_and_arn_pairs = [
        (
            EFSAccessPoint,
            "arn:aws:elasticfilesystem:us-east-1:111122223333:access-point/my_access_point",
        ),
    ]
    for class_, arn in class_and_arn_pairs:
        obj: _EFSCommon = class_.from_arn(arn)
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

    arn = "arn:aws:elasticfilesystem:us-east-1:111122223333:file-system/fs-1a2b3c4d"
    obj: EFSFileSystem = EFSFileSystem.from_arn(arn)
    with pytest.raises(ValueError):
        _ = obj.name


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.srv.efs", preview=False)
