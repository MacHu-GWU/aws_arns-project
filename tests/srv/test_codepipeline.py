# -*- coding: utf-8 -*-

from aws_arns.srv.codepipeline import (
    CodePipelinePipeline,
)


def test():
    arn = "arn:aws:codepipeline:us-east-1:111122223333:test"
    pipeline = CodePipelinePipeline.from_arn(arn)
    assert pipeline.pipeline_name == "test"
    assert (
        CodePipelinePipeline.new(
            aws_account_id=pipeline.aws_account_id,
            aws_region=pipeline.aws_region,
            name=pipeline.pipeline_name,
        )
        == pipeline
    )


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.srv.codepipeline", preview=False)
