# -*- coding: utf-8 -*-


def test():
    from aws_arns import api

    _ = api.Arn
    _ = api.AwsPartitionEnum
    _ = api.res.LambdaFunction
    _ = api.res.LambdaLayer
    _ = api.res.BatchComputeEnvironment
    _ = api.res.BatchJob
    _ = api.res.BatchJobDefinition
    _ = api.res.BatchJobQueue
    _ = api.res.BatchSchedulingPolicy
    _ = api.res.CloudFormationChangeSet
    _ = api.res.CloudFormationStack
    _ = api.res.CloudFormationStackSet
    _ = api.res.CodeBuildProject
    _ = api.res.CodeBuildRun
    _ = api.res.CodeCommitRepository
    _ = api.res.CodePipelinePipeline
    _ = api.res.IamGroup
    _ = api.res.IamInstanceProfile
    _ = api.res.IamPolicy
    _ = api.res.IamRole
    _ = api.res.IamUser
    _ = api.res.S3Bucket
    _ = api.res.S3Object
    _ = api.res.A2IHumanLoop
    _ = api.res.A2IHumanReviewWorkflow
    _ = api.res.A2IWorkerTaskTemplate
    _ = api.res.SecretManagerSecret
    _ = api.res.SnsSubscription
    _ = api.res.SnsTopic
    _ = api.res.SqsQueue
    _ = api.res.SSMParameter


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.api", preview=False)
