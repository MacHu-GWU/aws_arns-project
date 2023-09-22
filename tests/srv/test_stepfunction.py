# -*- coding: utf-8 -*-

import pytest

from aws_arns.srv.stepfunction import (
    SfnStateMachine,
    SfnStandardStateMachineExecution,
    SfnExpressStateMachineExecution,
)


def test():
    arn = "arn:aws:states:us-east-1:111122223333:stateMachine:standard_test"
    arn_version = "arn:aws:states:us-east-1:807388292768:stateMachine:standard_test:1"
    arn_alias = "arn:aws:states:us-east-1:807388292768:stateMachine:standard_test:LIVE"

    sm = SfnStateMachine.from_arn(arn)
    assert sm.name == "standard_test"
    assert sm.version == None
    assert sm.alias == None
    assert (
        SfnStateMachine.new(
            aws_account_id=sm.account_id,
            aws_region=sm.region,
            name=sm.name,
        )
        == sm
    )

    sm_version = SfnStateMachine.from_arn(arn_version)
    assert sm_version.name == "standard_test"
    assert sm_version.version == "1"
    with pytest.raises(Exception):
        _ = sm_version.alias
    assert (
        SfnStateMachine.new(
            aws_account_id=sm_version.account_id,
            aws_region=sm_version.region,
            name=sm_version.name,
            version=sm_version.version,
        )
        == sm_version
    )

    sm_alias = SfnStateMachine.from_arn(arn_alias)
    assert sm_alias.name == "standard_test"
    with pytest.raises(Exception):
        _ = sm_alias.version
    assert sm_alias.alias == "LIVE"
    assert (
        SfnStateMachine.new(
            aws_account_id=sm_alias.account_id,
            aws_region=sm_alias.region,
            name=sm_alias.name,
            alias=sm_alias.alias,
        )
        == sm_alias
    )

    standard_exec_arn = "arn:aws:states:us-east-1:111122223333:execution:standard_test:1d858cf6-613f-4576-b94f-e0d654c23843"
    express_exec_arn = "arn:aws:states:us-east-1:111122223333:express:express_test:e935dec6-e748-4977-a2f2-32eeb83d81da:b2f7726e-9b98-4a49-a6c4-9cf23a61f180"

    exec = SfnStandardStateMachineExecution.from_arn(standard_exec_arn)
    assert exec.state_machine_name == "standard_test"
    assert exec.exec_id == "1d858cf6-613f-4576-b94f-e0d654c23843"
    assert (
        SfnStandardStateMachineExecution.new(
            aws_account_id=exec.account_id,
            aws_region=exec.region,
            state_machine_name=exec.state_machine_name,
            exec_id=exec.exec_id,
        )
        == exec
    )

    exec = SfnExpressStateMachineExecution.from_arn(express_exec_arn)
    assert exec.state_machine_name == "express_test"
    assert (
        exec.exec_id
        == "e935dec6-e748-4977-a2f2-32eeb83d81da:b2f7726e-9b98-4a49-a6c4-9cf23a61f180"
    )
    assert (
        SfnExpressStateMachineExecution.new(
            aws_account_id=exec.account_id,
            aws_region=exec.region,
            state_machine_name=exec.state_machine_name,
            exec_id=exec.exec_id,
        )
        == exec
    )


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.srv.stepfunction", preview=False)
