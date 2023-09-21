# -*- coding: utf-8 -*-

from aws_arns.srv.ecr import (
    EcrRepository,
)


def test():
    arn = "arn:aws:ecr:us-east-1:123456789012:repository/my-repo"
    repo = EcrRepository.from_arn(arn)
    assert repo.repo_name == "my-repo"
    assert (
        EcrRepository.new(
            aws_region=repo.region,
            aws_account_id=repo.account_id,
            repo_name=repo.repo_name,
        )
        == repo
    )


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.srv.ecr", preview=False)
