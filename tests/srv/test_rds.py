# -*- coding: utf-8 -*-

from aws_arns.srv.rds import (
    _RdsCommon,
    RdsDBInstance,
    RdsDBCluster,
    RdsEventSubscription,
    RdsDBOptionGroup,
    RdsDBParameterGroup,
    RdsDBClusterParameterGroup,
    RdsReservedDBInstance,
    RdsDBSecurityGroup,
    RdsDBInstanceSnapshot,
    RdsDBClusterSnapshot,
    RdsDBSubnetGroup,
)

def test():
    class_and_arn_pairs = [
        (RdsDBInstance, "arn:aws:rds:us-east-1:111122223333:db:my-mysql-instance-1"),
        (RdsDBCluster, "arn:aws:rds:us-east-1:111122223333:cluster:my-aurora-cluster-1"),
        (RdsEventSubscription, "arn:aws:rds:us-east-1:111122223333:es:my-subscription"),
        (RdsDBOptionGroup, "arn:aws:rds:us-east-1:111122223333:og:my-og"),
        (RdsDBParameterGroup, "arn:aws:rds:us-east-2:123456789012:pg:my-param-enable-logs"),
        (RdsDBClusterParameterGroup, "arn:aws:rds:us-east-1:111122223333:cluster-pg:my-cluster-param-timezone"),
        (RdsReservedDBInstance, "arn:aws:rds:us-east-1:111122223333:ri:my-reserved-postgresql"),
        (RdsDBSecurityGroup, "arn:aws:rds:us-east-1:111122223333:secgrp:my-public"),
        (RdsDBInstanceSnapshot, "arn:aws:rds:us-east-1:111122223333:snapshot:rds:my-mysql-db-2020-01-01-00-00"),
        (RdsDBClusterSnapshot, "arn:aws:rds:us-east-2:111122223333:cluster-snapshot:rds:my-aurora-cluster-2020-01-01-00-00"),
        (RdsDBInstanceSnapshot, "arn:aws:rds:us-east-2:111122223333:snapshot:my-mysql-db-snap"),
        (RdsDBClusterSnapshot, "arn:aws:rds:us-east-2:111122223333:cluster-snapshot:my-aurora-cluster-snap"),
        (RdsDBSubnetGroup, "arn:aws:rds:us-east-1:111122223333:subgrp:my-subnet-10"),
    ]
    for class_, arn in class_and_arn_pairs:
        obj: _RdsCommon = class_.from_arn(arn)
        assert obj.to_arn() == arn
        assert (
            class_.new(
                aws_account_id=obj.aws_account_id,
                aws_region=obj.aws_region,
                resource_id=obj.resource_id,
            )
            == obj
        )

    assert RdsDBInstanceSnapshot.from_arn("arn:aws:rds:us-east-1:111122223333:snapshot:rds:my-mysql-db-2020-01-01-00-00").is_system_managed() is True
    assert RdsDBClusterSnapshot.from_arn("arn:aws:rds:us-east-2:111122223333:cluster-snapshot:rds:my-aurora-cluster-2020-01-01-00-00").is_system_managed() is True
    assert RdsDBInstanceSnapshot.from_arn("arn:aws:rds:us-east-2:111122223333:snapshot:my-mysql-db-snap").is_system_managed() is False
    assert RdsDBClusterSnapshot.from_arn("arn:aws:rds:us-east-2:111122223333:cluster-snapshot:my-aurora-cluster-snap").is_system_managed() is False


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.srv.rds", preview=False)
