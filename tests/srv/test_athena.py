# -*- coding: utf-8 -*-

from aws_arns.srv.athena import (
    _AthenaCommon,
    AthenaCapacityReservation,
    AthenaDataCatalog,
    AthenaWorkgroup,
)


def test():
    class_and_arn_pairs = [
        (
            AthenaCapacityReservation,
            "arn:aws:athena:us-east-1:111122223333:capacity-reservation/my_capacity_reservation",
        ),
        (
            AthenaDataCatalog,
            "arn:aws:athena:us-east-1:111122223333:datacatalog/my_datacatalog",
        ),
        (
            AthenaWorkgroup,
            "arn:aws:athena:us-east-1:111122223333:workgroup/my_workgroup",
        ),
    ]
    for class_, arn in class_and_arn_pairs:
        obj: _AthenaCommon = class_.from_arn(arn)
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

    run_cov_test(__file__, "aws_arns.srv.athena", preview=False)
