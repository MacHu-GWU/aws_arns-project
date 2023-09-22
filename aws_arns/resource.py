# -*- coding: utf-8 -*-

from .srv.awslambda import LambdaFunction
from .srv.awslambda import LambdaLayer
from .srv.batch import BatchComputeEnvironment
from .srv.batch import BatchJob
from .srv.batch import BatchJobDefinition
from .srv.batch import BatchJobQueue
from .srv.batch import BatchSchedulingPolicy
from .srv.cloudformation import CloudFormationChangeSet
from .srv.cloudformation import CloudFormationStack
from .srv.cloudformation import CloudFormationStackSet
from .srv.codebuild import CodeBuildBatchRun
from .srv.codebuild import CodeBuildProject
from .srv.codebuild import CodeBuildRun
from .srv.codecommit import CodeCommitRepository
from .srv.codepipeline import CodePipelinePipeline
from .srv.dynamodb import DynamodbGlobalTable
from .srv.dynamodb import DynamodbTable
from .srv.dynamodb import DynamodbTableBackup
from .srv.dynamodb import DynamodbTableExport
from .srv.dynamodb import DynamodbTableImport
from .srv.dynamodb import DynamodbTableIndex
from .srv.dynamodb import DynamodbTableStream
from .srv.ec2 import ClientVPNEndpoint
from .srv.ec2 import DHCPOptionSet
from .srv.ec2 import EbsSnapshot
from .srv.ec2 import EbsVolume
from .srv.ec2 import Ec2Image
from .srv.ec2 import Ec2Instance
from .srv.ec2 import Ec2KeyPair
from .srv.ec2 import Ec2NetworkInterface
from .srv.ec2 import ElasticIpAllocation
from .srv.ec2 import InternetGateway
from .srv.ec2 import NatGateway
from .srv.ec2 import NetworkACL
from .srv.ec2 import RouteTable
from .srv.ec2 import SecurityGroup
from .srv.ec2 import SecurityGroupRule
from .srv.ec2 import SiteToSiteVPNConnection
from .srv.ec2 import Subnet
from .srv.ec2 import TransitGateway
from .srv.ec2 import TransitGatewayAttachment
from .srv.ec2 import Vpc
from .srv.ec2 import VpcCustomGateway
from .srv.ec2 import VpcEndpoint
from .srv.ec2 import VpcPeeringConnection
from .srv.ec2 import VpcPrivateGateway
from .srv.ecr import EcrRepository
from .srv.ecs import EcsCluster
from .srv.ecs import EcsContainerInstance
from .srv.ecs import EcsService
from .srv.ecs import EcsTaskDefinition
from .srv.ecs import EcsTaskRun
from .srv.glue import GlueCrawler
from .srv.glue import GlueDatabase
from .srv.glue import GlueJob
from .srv.glue import GlueMLTransform
from .srv.glue import GlueTable
from .srv.glue import GlueTrigger
from .srv.iam import IamGroup
from .srv.iam import IamInstanceProfile
from .srv.iam import IamPolicy
from .srv.iam import IamRole
from .srv.iam import IamUser
from .srv.logs import CloudWatchLogGroup
from .srv.logs import CloudWatchLogGroupStream
from .srv.opensearch import OpenSearchDomain
from .srv.opensearch import OpenSearchServerlessCollection
from .srv.opensearch import OpenSearchServerlessDashboard
from .srv.rds import RdsDBCluster
from .srv.rds import RdsDBClusterParameterGroup
from .srv.rds import RdsDBClusterSnapshot
from .srv.rds import RdsDBInstance
from .srv.rds import RdsDBInstanceSnapshot
from .srv.rds import RdsDBOptionGroup
from .srv.rds import RdsDBParameterGroup
from .srv.rds import RdsDBSecurityGroup
from .srv.rds import RdsDBSubnetGroup
from .srv.rds import RdsEventSubscription
from .srv.rds import RdsReservedDBInstance
from .srv.redshift import RedshiftCluster
from .srv.redshift import RedshiftDatabaseName
from .srv.redshift import RedshiftDatabaseUserGroup
from .srv.redshift import RedshiftParameterGroup
from .srv.redshift import RedshiftSecurityGroup
from .srv.redshift import RedshiftServerlessManagedVpcEndpoint
from .srv.redshift import RedshiftServerlessNamespace
from .srv.redshift import RedshiftServerlessSnapshot
from .srv.redshift import RedshiftServerlessWorkgroup
from .srv.redshift import RedshiftSnapshot
from .srv.redshift import RedshiftSnapshotSchedule
from .srv.redshift import RedshiftSubnetGroup
from .srv.s3 import S3Bucket
from .srv.s3 import S3Object
from .srv.sagemaker import SageMakerAction
from .srv.sagemaker import SageMakerAlgorithm
from .srv.sagemaker import SageMakerApp
from .srv.sagemaker import SageMakerAppImageConfig
from .srv.sagemaker import SageMakerAutomlJob
from .srv.sagemaker import SageMakerCodeRepository
from .srv.sagemaker import SageMakerCompilationJob
from .srv.sagemaker import SageMakerContext
from .srv.sagemaker import SageMakerDataQualityJobDefinition
from .srv.sagemaker import SageMakerDevice
from .srv.sagemaker import SageMakerDeviceFleet
from .srv.sagemaker import SageMakerDomain
from .srv.sagemaker import SageMakerEndpoint
from .srv.sagemaker import SageMakerEndpointConfig
from .srv.sagemaker import SageMakerExperiment
from .srv.sagemaker import SageMakerExperimentTrial
from .srv.sagemaker import SageMakerExperimentTrialComponent
from .srv.sagemaker import SageMakerFeatureGroup
from .srv.sagemaker import SageMakerHub
from .srv.sagemaker import SageMakerHubContent
from .srv.sagemaker import SageMakerHyperParameterTuningJob
from .srv.sagemaker import SageMakerImage
from .srv.sagemaker import SageMakerImageVersion
from .srv.sagemaker import SageMakerInferenceExperiment
from .srv.sagemaker import SageMakerInferenceRecommendationsJob
from .srv.sagemaker import SageMakerLabelingJob
from .srv.sagemaker import SageMakerModel
from .srv.sagemaker import SageMakerModelBiasJobDefinition
from .srv.sagemaker import SageMakerModelCard
from .srv.sagemaker import SageMakerModelCardExportJob
from .srv.sagemaker import SageMakerModelExplainabilityJobDefinition
from .srv.sagemaker import SageMakerModelPackage
from .srv.sagemaker import SageMakerModelPackageGroup
from .srv.sagemaker import SageMakerModelQualityJobDefinition
from .srv.sagemaker import SageMakerMonitoringSchedule
from .srv.sagemaker import SageMakerMonitoringScheduleAlert
from .srv.sagemaker import SageMakerNotebookInstance
from .srv.sagemaker import SageMakerPipeline
from .srv.sagemaker import SageMakerPipelineExecution
from .srv.sagemaker import SageMakerProcessingJob
from .srv.sagemaker import SageMakerSharedModel
from .srv.sagemaker import SageMakerSharedModelEvent
from .srv.sagemaker import SageMakerSpace
from .srv.sagemaker import SageMakerStudioLifecycleConfig
from .srv.sagemaker import SageMakerTrainingJob
from .srv.sagemaker import SageMakerTransformJob
from .srv.sagemaker import SageMakerUserProfile
from .srv.sagemaker import SageMakerWorkforce
from .srv.sagemaker import SageMakerWorkteam
from .srv.sagemaker_a2i import A2IHumanLoop
from .srv.sagemaker_a2i import A2IHumanReviewWorkflow
from .srv.sagemaker_a2i import A2IWorkerTaskTemplate
from .srv.secretmanager import SecretManagerSecret
from .srv.sns import SnsSubscription
from .srv.sns import SnsTopic
from .srv.sqs import SqsQueue
from .srv.ssm import SSMParameter
from .srv.stepfunction import SfnExpressStateMachineExecution
from .srv.stepfunction import SfnStandardStateMachineExecution
from .srv.stepfunction import SfnStateMachine