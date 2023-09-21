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
    _ = api.res.DynamodbGlobalTable
    _ = api.res.DynamodbTable
    _ = api.res.DynamodbTableBackup
    _ = api.res.DynamodbTableExport
    _ = api.res.DynamodbTableImport
    _ = api.res.DynamodbTableIndex
    _ = api.res.DynamodbTableStream
    _ = api.res.ClientVPNEndpoint
    _ = api.res.DHCPOptionSet
    _ = api.res.EbsSnapshot
    _ = api.res.EbsVolume
    _ = api.res.Ec2Image
    _ = api.res.Ec2Instance
    _ = api.res.Ec2KeyPair
    _ = api.res.Ec2NetworkInterface
    _ = api.res.ElasticIpAllocation
    _ = api.res.InternetGateway
    _ = api.res.NatGateway
    _ = api.res.NetworkACL
    _ = api.res.RouteTable
    _ = api.res.SecurityGroup
    _ = api.res.SecurityGroupRule
    _ = api.res.SiteToSiteVPNConnection
    _ = api.res.Subnet
    _ = api.res.TransitGateway
    _ = api.res.TransitGatewayAttachment
    _ = api.res.Vpc
    _ = api.res.VpcCustomGateway
    _ = api.res.VpcEndpoint
    _ = api.res.VpcPeeringConnection
    _ = api.res.VpcPrivateGateway
    _ = api.res.EcrRepository
    _ = api.res.EcsCluster
    _ = api.res.EcsContainerInstance
    _ = api.res.EcsService
    _ = api.res.EcsTaskDefinition
    _ = api.res.EcsTaskRun
    _ = api.res.GlueCrawler
    _ = api.res.GlueDatabase
    _ = api.res.GlueJob
    _ = api.res.GlueMLTransform
    _ = api.res.GlueTable
    _ = api.res.GlueTrigger
    _ = api.res.IamGroup
    _ = api.res.IamInstanceProfile
    _ = api.res.IamPolicy
    _ = api.res.IamRole
    _ = api.res.IamUser
    _ = api.res.CloudWatchLogGroup
    _ = api.res.CloudWatchLogGroupStream
    _ = api.res.RdsDBCluster
    _ = api.res.RdsDBClusterParameterGroup
    _ = api.res.RdsDBClusterSnapshot
    _ = api.res.RdsDBInstance
    _ = api.res.RdsDBInstanceSnapshot
    _ = api.res.RdsDBOptionGroup
    _ = api.res.RdsDBParameterGroup
    _ = api.res.RdsDBSecurityGroup
    _ = api.res.RdsDBSubnetGroup
    _ = api.res.RdsEventSubscription
    _ = api.res.RdsReservedDBInstance
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
    _ = api.res.SfnStateMachine
    _ = api.res.SfnStateMachineExecution


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.api", preview=False)