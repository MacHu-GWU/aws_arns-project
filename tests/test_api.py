# -*- coding: utf-8 -*-


def test():
    from aws_arns import api

    _ = api.Arn
    _ = api.BaseArn
    _ = api.is_arn_instance
    _ = api.parse_arn
    _ = api.AwsPartitionEnum
    _ = api.res.ApiGatewayV1Authorizer
    _ = api.res.ApiGatewayV1Deployment
    _ = api.res.ApiGatewayV1Integration
    _ = api.res.ApiGatewayV1Model
    _ = api.res.ApiGatewayV1Route
    _ = api.res.ApiGatewayV1Stage
    _ = api.res.ApiGatewayV2Authorizer
    _ = api.res.ApiGatewayV2Deployment
    _ = api.res.ApiGatewayV2Integration
    _ = api.res.ApiGatewayV2Model
    _ = api.res.ApiGatewayV2Route
    _ = api.res.ApiGatewayV2Stage
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
    _ = api.res.CodeBuildBatchRun
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
    _ = api.res.KmsAlias
    _ = api.res.KmsKey
    _ = api.res.CloudWatchLogGroup
    _ = api.res.CloudWatchLogGroupStream
    _ = api.res.OpenSearchDomain
    _ = api.res.OpenSearchServerlessCollection
    _ = api.res.OpenSearchServerlessDashboard
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
    _ = api.res.RedshiftCluster
    _ = api.res.RedshiftDatabaseName
    _ = api.res.RedshiftDatabaseUserGroup
    _ = api.res.RedshiftParameterGroup
    _ = api.res.RedshiftSecurityGroup
    _ = api.res.RedshiftServerlessManagedVpcEndpoint
    _ = api.res.RedshiftServerlessNamespace
    _ = api.res.RedshiftServerlessSnapshot
    _ = api.res.RedshiftServerlessWorkgroup
    _ = api.res.RedshiftSnapshot
    _ = api.res.RedshiftSnapshotSchedule
    _ = api.res.RedshiftSubnetGroup
    _ = api.res.S3Bucket
    _ = api.res.S3Object
    _ = api.res.SageMakerAction
    _ = api.res.SageMakerAlgorithm
    _ = api.res.SageMakerApp
    _ = api.res.SageMakerAppImageConfig
    _ = api.res.SageMakerAutomlJob
    _ = api.res.SageMakerCodeRepository
    _ = api.res.SageMakerCompilationJob
    _ = api.res.SageMakerContext
    _ = api.res.SageMakerDataQualityJobDefinition
    _ = api.res.SageMakerDevice
    _ = api.res.SageMakerDeviceFleet
    _ = api.res.SageMakerDomain
    _ = api.res.SageMakerEndpoint
    _ = api.res.SageMakerEndpointConfig
    _ = api.res.SageMakerExperiment
    _ = api.res.SageMakerExperimentTrial
    _ = api.res.SageMakerExperimentTrialComponent
    _ = api.res.SageMakerFeatureGroup
    _ = api.res.SageMakerHub
    _ = api.res.SageMakerHubContent
    _ = api.res.SageMakerHyperParameterTuningJob
    _ = api.res.SageMakerImage
    _ = api.res.SageMakerImageVersion
    _ = api.res.SageMakerInferenceExperiment
    _ = api.res.SageMakerInferenceRecommendationsJob
    _ = api.res.SageMakerLabelingJob
    _ = api.res.SageMakerModel
    _ = api.res.SageMakerModelBiasJobDefinition
    _ = api.res.SageMakerModelCard
    _ = api.res.SageMakerModelCardExportJob
    _ = api.res.SageMakerModelExplainabilityJobDefinition
    _ = api.res.SageMakerModelPackage
    _ = api.res.SageMakerModelPackageGroup
    _ = api.res.SageMakerModelQualityJobDefinition
    _ = api.res.SageMakerMonitoringSchedule
    _ = api.res.SageMakerMonitoringScheduleAlert
    _ = api.res.SageMakerNotebookInstance
    _ = api.res.SageMakerPipeline
    _ = api.res.SageMakerPipelineExecution
    _ = api.res.SageMakerProcessingJob
    _ = api.res.SageMakerSharedModel
    _ = api.res.SageMakerSharedModelEvent
    _ = api.res.SageMakerSpace
    _ = api.res.SageMakerStudioLifecycleConfig
    _ = api.res.SageMakerTrainingJob
    _ = api.res.SageMakerTransformJob
    _ = api.res.SageMakerUserProfile
    _ = api.res.SageMakerWorkforce
    _ = api.res.SageMakerWorkteam
    _ = api.res.A2IHumanLoop
    _ = api.res.A2IHumanReviewWorkflow
    _ = api.res.A2IWorkerTaskTemplate
    _ = api.res.SecretManagerSecret
    _ = api.res.SnsSubscription
    _ = api.res.SnsTopic
    _ = api.res.SqsQueue
    _ = api.res.SSMParameter
    _ = api.res.SfnExpressStateMachineExecution
    _ = api.res.SfnStandardStateMachineExecution
    _ = api.res.SfnStateMachine


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.api", preview=False)