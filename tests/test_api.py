# -*- coding: utf-8 -*-


def test():
    from aws_arns import api

    _ = api.Arn
    _ = api.AWSPartitionEnum
    _ = api.Arn
    _ = api.CrossAccountGlobal
    _ = api.Global
    _ = api.Regional
    _ = api.ResourceIdOnlyRegional
    _ = api.ColonSeparatedRegional
    _ = api.SlashSeparatedRegional
    _ = api.IamGroup
    _ = api.IamUser
    _ = api.IamRole
    _ = api.IamPolicy
    _ = api.IamInstanceProfile
    _ = api.BatchComputeEnvironment
    _ = api.BatchJobQueue
    _ = api.BatchJobDefinition
    _ = api.BatchJob
    _ = api.BatchSchedulingPolicy
    _ = api.A2IHumanReviewWorkflow
    _ = api.A2IHumanLoop
    _ = api.A2IWorkerTaskTemplate
    _ = api.CloudFormationStack
    _ = api.CloudFormationChangeSet
    _ = api.CloudFormationStackSet
    _ = api.CodeBuildProject
    _ = api.CodeBuildRun


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.api", preview=False)
