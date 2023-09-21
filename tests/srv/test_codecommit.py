# -*- coding: utf-8 -*-

from aws_arns.srv.codecommit import (
    CodeCommitRepository,
)


def test():
    arn = "arn:aws:codecommit:us-east-1:111122223333:test"
    repo = CodeCommitRepository.from_arn(arn)
    assert repo.repo_name == "test"
    assert (
        CodeCommitRepository.new(
            aws_account_id=repo.aws_account_id,
            aws_region=repo.aws_region,
            name=repo.repo_name,
        )
        == repo
    )


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.srv.codecommit", preview=False)
