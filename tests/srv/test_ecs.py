# -*- coding: utf-8 -*-

from aws_arns.srv.ecs import (
    EcsCluster,
    EcsTaskDefinition,
    EcsContainerInstance,
    EcsService,
    EcsTaskRun,
)


def test():
    arn = "arn:aws:ecs:us-east-1:111122223333:cluster/my-cluster-1"
    cluster = EcsCluster.from_arn(arn)
    assert cluster.cluster_name == "my-cluster-1"
    assert (
        EcsCluster.new(
            aws_region=cluster.region,
            aws_account_id=cluster.account_id,
            cluster_name=cluster.cluster_name,
        )
        == cluster
    )

    arn = "arn:aws:ecs:us-east-1:111122223333:task-definition/my-task:1"
    task_def = EcsTaskDefinition.from_arn(arn)
    assert task_def.task_name == "my-task"
    assert task_def.version == 1
    assert (
        EcsTaskDefinition.new(
            aws_region=task_def.region,
            aws_account_id=task_def.account_id,
            task_name=task_def.task_name,
            version=task_def.version,
        )
        == task_def
    )

    arn = "arn:aws:ecs:us-east-1:111122223333:container-instance/my-cluster/container_instance_UUID"
    cont_inst = EcsContainerInstance.from_arn(arn)
    assert cont_inst.cluster_name == "my-cluster"
    assert cont_inst.container_instance_id == "container_instance_UUID"
    assert (
        EcsContainerInstance.new(
            aws_region=cont_inst.region,
            aws_account_id=cont_inst.account_id,
            cluster_name=cont_inst.cluster_name,
            container_instance_id=cont_inst.container_instance_id,
        )
        == cont_inst
    )

    arn = "arn:aws:ecs:us-east-1:111122223333:service/service_name"
    service = EcsService.from_arn(arn)
    assert service.service_name == "service_name"
    assert (
        EcsService.new(
            aws_region=service.region,
            aws_account_id=service.account_id,
            service_name=service.service_name,
        )
        == service
    )

    arn = "arn:aws:ecs:us-east-1:123456789012:task/my_cluster/a1b2c3d4-5678-90ab-ccdef-11111EXAMPLE"
    task_run = EcsTaskRun.from_arn(arn)
    assert task_run.run_id == "my_cluster/a1b2c3d4-5678-90ab-ccdef-11111EXAMPLE"
    assert task_run.cluster_name == "my_cluster"
    assert task_run.short_id == "a1b2c3d4-5678-90ab-ccdef-11111EXAMPLE"
    assert (
        EcsTaskRun.new(
            aws_region=task_run.region,
            aws_account_id=task_run.account_id,
            run_id=task_run.run_id,
        )
        == task_run
    )


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.srv.ecs", preview=False)
