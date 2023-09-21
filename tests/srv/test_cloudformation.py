# -*- coding: utf-8 -*-

from aws_arns.srv.cloudformation import (
    CloudFormationStack,
    CloudFormationChangeSet,
    CloudFormationStackSet,
)


def test():
    arn = "arn:aws:cloudformation:us-east-1:111122223333:stack/my-stack/a1b2c3d4"
    stack = CloudFormationStack.from_arn(arn)
    assert stack.stack_name == "my-stack"
    assert stack.short_id == "a1b2c3d4"
    assert stack.stack_fullname == "my-stack/a1b2c3d4"
    assert stack.stack_id == stack.to_arn()
    assert (
        CloudFormationStack.new(
            aws_region=stack.region,
            aws_account_id=stack.account_id,
            stack_name=stack.stack_name,
            short_id=stack.short_id,
        )
        == stack
    )

    arn = (
        "arn:aws:cloudformation:us-east-1:111122223333:changeSet/my-change-set/a1b2c3d4"
    )
    changeset = CloudFormationChangeSet.from_arn(arn)
    assert changeset.changeset_fullname == "my-change-set/a1b2c3d4"
    assert (
        CloudFormationChangeSet.new(
            aws_region=changeset.region,
            aws_account_id=changeset.account_id,
            fullname=changeset.changeset_fullname,
        )
        == changeset
    )

    arn = "arn:aws:cloudformation:us-east-1:111122223333:stackset/my-stackset:a1b2c3d4"
    stackset = CloudFormationStackSet.from_arn(arn)
    assert stackset.stackset_name == "my-stackset"
    assert stackset.stackset_id == "a1b2c3d4"
    assert stackset.stackset_fullname == "my-stackset:a1b2c3d4"
    assert (
        CloudFormationStackSet.new(
            aws_region=stackset.region,
            aws_account_id=stackset.account_id,
            fullname=stackset.stackset_fullname,
        )
        == stackset
    )


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.srv.cloudformation", preview=False)
