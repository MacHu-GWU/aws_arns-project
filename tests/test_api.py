# -*- coding: utf-8 -*-


def test():
    from aws_arns import api

    _ = api.Arn
    _ = api.AWSPartitionEnum
    _ = api.Arn
    _ = api._CrossAccountGlobal
    _ = api._Global
    _ = api._Regional
    _ = api.ResourceIdOnlyRegional
    _ = api._ColonSeparatedRegional
    _ = api._SlashSeparatedRegional
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
    _ = api.S3Bucket
    _ = api.S3Object


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.api", preview=False)
