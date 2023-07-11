# -*- coding: utf-8 -*-

from aws_arns.srv.batch import (
    BatchComputeEnvironment,
    BatchJobQueue,
    BatchJobDefinition,
    BatchJob,
    BatchSchedulingPolicy,
)


def test():
    arn = "arn:aws:batch:us-east-1:111122223333:compute-environment/my-ce"
    batch_ce = BatchComputeEnvironment.from_arn(arn)
    assert batch_ce.name == "my-ce"
    assert batch_ce.batch_compute_environment_name == "my-ce"
    assert (
        BatchComputeEnvironment.new(
            aws_region=batch_ce.region,
            aws_account_id=batch_ce.account_id,
            name=batch_ce.batch_compute_environment_name,
        )
        == batch_ce
    )

    arn = "arn:aws:batch:us-east-1:111122223333:job-queue/my-queue"
    batch_q = BatchJobQueue.from_arn(arn)
    assert batch_q.batch_job_queue_name == "my-queue"
    assert (
        BatchJobQueue.new(
            aws_region=batch_ce.region,
            aws_account_id=batch_ce.account_id,
            name=batch_q.batch_job_queue_name,
        )
        == batch_q
    )

    arn = "arn:aws:batch:us-east-1:111122223333:job-definition/my-job-def:1"
    batch_jd = BatchJobDefinition.from_arn(arn)
    assert batch_jd.batch_job_definition_fullname == "my-job-def:1"
    assert batch_jd.batch_job_definition_name == "my-job-def"
    assert batch_jd.batch_job_definition_revision == 1
    assert (
        BatchJobDefinition.new(
            aws_region=batch_jd.region,
            aws_account_id=batch_jd.account_id,
            name=batch_jd.batch_job_definition_name,
            revision=batch_jd.batch_job_definition_revision,
        )
        == batch_jd
    )

    arn = (
        "arn:aws:batch:us-east-1:111122223333:job/a974ee84-1da8-40bf-bca9-ef4253fac3c6"
    )
    batch_job = BatchJob.from_arn(arn)
    assert batch_job.batch_job_id == "a974ee84-1da8-40bf-bca9-ef4253fac3c6"
    assert (
        BatchJob.new(
            aws_region=batch_ce.region,
            aws_account_id=batch_ce.account_id,
            job_id=batch_job.batch_job_id,
        )
        == batch_job
    )

    arn = "arn:aws:batch:us-east-1:111122223333:scheduling-policy/my-policy"
    batch_scheduling_policy = BatchSchedulingPolicy.from_arn(arn)
    assert batch_scheduling_policy.batch_scheduling_policy_name == "my-policy"
    assert (
        BatchSchedulingPolicy.new(
            aws_region=batch_ce.region,
            aws_account_id=batch_ce.account_id,
            name=batch_scheduling_policy.batch_scheduling_policy_name,
        )
        == batch_scheduling_policy
    )


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.srv.batch", preview=False)
