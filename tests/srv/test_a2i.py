# -*- coding: utf-8 -*-

from aws_arns.srv.sagemaker_a2i import (
    A2IHumanReviewWorkflow,
    A2IHumanLoop,
    A2IWorkerTaskTemplate,
)


def test():
    arn = "arn:aws:sagemaker:us-east-1:111122223333:flow-definition/my-flow"
    a2i_human_review_workflow = A2IHumanReviewWorkflow.from_arn(arn)
    assert a2i_human_review_workflow.name == "my-flow"
    assert a2i_human_review_workflow.a2i_human_review_workflow_name == "my-flow"
    assert (
        A2IHumanReviewWorkflow.new(
            aws_region=a2i_human_review_workflow.region,
            aws_account_id=a2i_human_review_workflow.account_id,
            name=a2i_human_review_workflow.a2i_human_review_workflow_name,
        )
        == a2i_human_review_workflow
    )

    arn = "arn:aws:sagemaker:us-east-1:111122223333:human-loop/a1b2"
    a2i_human_loop = A2IHumanLoop.from_arn(arn)
    assert a2i_human_loop.a2i_human_loop_name == "a1b2"
    assert (
        A2IHumanLoop.new(
            aws_region=a2i_human_loop.region,
            aws_account_id=a2i_human_loop.account_id,
            name=a2i_human_loop.a2i_human_loop_name,
        )
        == a2i_human_loop
    )

    arn = "arn:aws:sagemaker:us-east-1:111122223333:human-task-ui/my-template"
    a2i_task_template = A2IWorkerTaskTemplate.from_arn(arn)
    assert a2i_task_template.a2i_worker_task_template_name == "my-template"
    assert (
        A2IWorkerTaskTemplate.new(
            aws_region=a2i_task_template.region,
            aws_account_id=a2i_task_template.account_id,
            name=a2i_task_template.a2i_worker_task_template_name,
        )
        == a2i_task_template
    )


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.srv.sagemaker_a2i", preview=False)
