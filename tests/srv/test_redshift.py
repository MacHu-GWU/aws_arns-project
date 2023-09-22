# -*- coding: utf-8 -*-

from aws_arns.srv.redshift import (
    RedshiftCluster,
    RedshiftDatabaseUserGroup,
    RedshiftDatabaseName,
    RedshiftSnapshot,
    RedshiftSnapshotSchedule,
    RedshiftParameterGroup,
    RedshiftSubnetGroup,
    RedshiftSecurityGroup,
    RedshiftServerlessNamespace,
    RedshiftServerlessWorkgroup,
    RedshiftServerlessSnapshot,
    RedshiftServerlessManagedVpcEndpoint,
)


def test():
    rs_cluster_arn = "arn:aws:redshift:us-east-1:111122223333:cluster:my_cluster"
    rs_dbgroup_arn = (
        "arn:aws:redshift:us-east-1:111122223333:dbgroup:my_cluster/my_db_group"
    )
    rs_dbname_arn = (
        "arn:aws:redshift:us-east-1:111122223333:dbname:my_cluster/my_database"
    )
    rs_snapshot_arn = (
        "arn:aws:redshift:us-east-1:111122223333:snapshot:my_cluster/my_snapshot"
    )
    rs_snapshot_schedule_arn = (
        "arn:aws:redshift:us-east-1:111122223333:snapshotschedule:my_snapshot_schedule"
    )
    rs_parameter_group_arn = (
        "arn:aws:redshift:us-east-1:111122223333:parametergroup:my_parameter_group"
    )
    rs_subnet_group_arn = (
        "arn:aws:redshift:us-east-1:111122223333:subnetgroup:my_subnet_group"
    )
    rs_security_group_name_arn = "arn:aws:redshift:us-east-1:111122223333:securitygroup:my_group_name/ec2securitygroup/owner_name/sg-1a2b"
    rs_svls_namespace_arn = (
        "arn:aws:redshift-serverless:us-east-1:111122223333:namespace/my_namespace"
    )
    rs_svls_workgroup_arn = (
        "arn:aws:redshift-serverless:us-east-1:111122223333:workgroup/my_workgroup"
    )
    rs_svls_snapshot_arn = (
        "arn:aws:redshift-serverless:us-east-1:111122223333:snapshot/my_snapshot"
    )
    rs_svls_vpce_arn = "arn:aws:redshift-serverless:us-east-1:111122223333:managedvpcendpoint/my_vpc_endpoint"

    rs_cluster = RedshiftCluster.from_arn(rs_cluster_arn)
    rs_dbgroup = RedshiftDatabaseUserGroup.from_arn(rs_dbgroup_arn)
    rs_dbname = RedshiftDatabaseName.from_arn(rs_dbname_arn)
    rs_snapshot = RedshiftSnapshot.from_arn(rs_snapshot_arn)
    rs_snapshot_schedule = RedshiftSnapshotSchedule.from_arn(rs_snapshot_schedule_arn)
    rs_parameter_group = RedshiftParameterGroup.from_arn(rs_parameter_group_arn)
    rs_subnet_group = RedshiftSubnetGroup.from_arn(rs_subnet_group_arn)
    rs_security_group_name = RedshiftSecurityGroup.from_arn(rs_security_group_name_arn)
    rs_svls_namespace = RedshiftServerlessNamespace.from_arn(rs_svls_namespace_arn)
    rs_svls_workgroup = RedshiftServerlessWorkgroup.from_arn(rs_svls_workgroup_arn)
    rs_svls_snapshot = RedshiftServerlessSnapshot.from_arn(rs_svls_snapshot_arn)
    rs_svls_vpce = RedshiftServerlessManagedVpcEndpoint.from_arn(rs_svls_vpce_arn)

    for obj, arn in [
        (rs_cluster, rs_cluster_arn),
        (rs_dbgroup, rs_dbgroup_arn),
        (rs_dbname, rs_dbname_arn),
        (rs_snapshot, rs_snapshot_arn),
        (rs_snapshot_schedule, rs_snapshot_schedule_arn),
        (rs_parameter_group, rs_parameter_group_arn),
        (rs_subnet_group, rs_subnet_group_arn),
        (rs_security_group_name, rs_security_group_name_arn),
        (rs_svls_namespace, rs_svls_namespace_arn),
        (rs_svls_workgroup, rs_svls_workgroup_arn),
        (rs_svls_snapshot, rs_svls_snapshot_arn),
        (rs_svls_vpce, rs_svls_vpce_arn),
    ]:
        assert obj.to_arn() == arn

    for obj in [
        rs_cluster,
        rs_dbgroup,
        rs_dbname,
        rs_snapshot,
    ]:
        assert obj.cluster_id == "my_cluster"

    for obj in [
        rs_dbgroup,
        rs_dbname,
        rs_snapshot,
    ]:
        assert (
            obj.new(
                obj.aws_account_id,
                obj.aws_region,
                obj.cluster_id,
                obj.resource_name,
            )
            == obj
        )

    _ = RedshiftDatabaseUserGroup.from_arn(rs_dbgroup_arn).user_group
    _ = RedshiftDatabaseName.from_arn(rs_dbname_arn).database_name
    _ = RedshiftSnapshot.from_arn(rs_snapshot_arn).snapshot_name
    _ = RedshiftSnapshotSchedule.from_arn(
        rs_snapshot_schedule_arn
    ).snapshot_schedule_name
    _ = RedshiftParameterGroup.from_arn(rs_parameter_group_arn).parameter_group_name
    _ = RedshiftSubnetGroup.from_arn(rs_subnet_group_arn).subnet_group_name
    rs_sg = RedshiftSecurityGroup.from_arn(rs_security_group_name_arn)
    assert rs_sg.security_group_name == "my_group_name"
    assert rs_sg.owner_name == "owner_name"
    assert rs_sg.ec2_security_group_id == "sg-1a2b"
    assert (
        RedshiftSecurityGroup.new(
            rs_sg.aws_account_id,
            rs_sg.aws_region,
            rs_sg.security_group_name,
            rs_sg.owner_name,
            rs_sg.ec2_security_group_id,
        )
        == rs_sg
    )

    assert rs_svls_namespace.namespace_id == rs_svls_namespace.resource_id
    assert rs_svls_workgroup.workgroup_id == rs_svls_workgroup.resource_id
    assert rs_svls_snapshot.snapshot_id == rs_svls_snapshot.resource_id
    assert rs_svls_vpce.resource_id == rs_svls_vpce.resource_id
    for obj in [
        rs_svls_namespace,
        rs_svls_workgroup,
        rs_svls_snapshot,
        rs_svls_vpce,
    ]:
        assert (
            obj.new(
                obj.aws_account_id,
                obj.aws_region,
                obj.resource_id,
            )
            == obj
        )


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.srv.redshift", preview=False)
