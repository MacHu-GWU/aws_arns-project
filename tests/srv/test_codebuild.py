# -*- coding: utf-8 -*-

from aws_arns.srv.codebuild import (
    CodeBuildProject,
    CodeBuildRun,
    CodeBuildBatchRun,
)


def test():
    arn = "arn:aws:codebuild:us-east-1:111122223333:project/my-project"
    project = CodeBuildProject.from_arn(arn)
    assert project.codebuild_project_name == "my-project"
    assert (
        CodeBuildProject.new(
            aws_region=project.region,
            aws_account_id=project.account_id,
            name=project.codebuild_project_name,
        )
        == project
    )

    arn = "arn:aws:codebuild:us-east-1:111122223333:build/my-project:a1b2c3d4"
    run = CodeBuildRun.from_arn(arn)
    assert run.codebuild_run_fullname == "my-project:a1b2c3d4"
    assert run.codebuild_project_name == "my-project"
    assert run.codebuild_run_id == "a1b2c3d4"
    assert (
        CodeBuildRun.new(
            aws_region=run.region,
            aws_account_id=run.account_id,
            fullname=run.codebuild_run_fullname,
        )
        == run
    )

    arn = "arn:aws:codebuild:us-east-1:111122223333:build-batch/my-project:a1b2c3d4"
    run = CodeBuildBatchRun.from_arn(arn)
    assert run.codebuild_run_fullname == "my-project:a1b2c3d4"
    assert run.codebuild_project_name == "my-project"
    assert run.codebuild_run_id == "a1b2c3d4"
    assert (
        CodeBuildBatchRun.new(
            aws_region=run.region,
            aws_account_id=run.account_id,
            fullname=run.codebuild_run_fullname,
        )
        == run
    )


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.srv.codebuild", preview=False)
