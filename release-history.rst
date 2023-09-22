.. _release_history:

Release and Version History
==============================================================================


Backlog (TODO)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


1.2.1 (2023-09-22)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Add the ``aws_arns.res.parse_arn`` function, which can, if possible, parse the ARN string into the corresponding AWS Resource Arn object (iam role, s3 bucket, etc.). Otherwise, it returns the ``aws_arns.Arn`` object.
- Add the ``aws_arns.is_arn_instance`` function to test if an object is an Arn object.
- Add the follow curated AWS Resource ARN to public API
    - ``aws_arns.res.ApiGatewayV1Authorizer``
    - ``aws_arns.res.ApiGatewayV1Deployment``
    - ``aws_arns.res.ApiGatewayV1Integration``
    - ``aws_arns.res.ApiGatewayV1Model``
    - ``aws_arns.res.ApiGatewayV1Route``
    - ``aws_arns.res.ApiGatewayV1Stage``
    - ``aws_arns.res.ApiGatewayV2Authorizer``
    - ``aws_arns.res.ApiGatewayV2Deployment``
    - ``aws_arns.res.ApiGatewayV2Integration``
    - ``aws_arns.res.ApiGatewayV2Model``
    - ``aws_arns.res.ApiGatewayV2Route``
    - ``aws_arns.res.ApiGatewayV2Stage``

**Minor Improvements**

- add the missing ``aws_arns.res.CodeBuildBatchRun``.
- break down the ``aws_arns.res.SfnStateMachineExecution`` (this class is removed) into ``SfnStandardStateMachineExecution`` and ``SfnExpressStateMachineExecution``


1.1.1 (2023-09-21)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Add the follow curated AWS Resource ARN to public API
    - ``aws_arns.res.DynamodbTable``
    - ``aws_arns.res.DynamodbGlobalTable``
    - ``aws_arns.res.DynamodbTableIndex``
    - ``aws_arns.res.DynamodbTableStream``
    - ``aws_arns.res.DynamodbTableBackup``
    - ``aws_arns.res.DynamodbTableExport``
    - ``aws_arns.res.DynamodbTableImport``
    - ``aws_arns.res.EcrRepository``
    - ``aws_arns.res.EcsCluster``
    - ``aws_arns.res.EcsContainerInstance``
    - ``aws_arns.res.EcsService``
    - ``aws_arns.res.EcsTaskDefinition``
    - ``aws_arns.res.EcsTaskRun``
    - ``aws_arns.res.CloudWatchLogGroup``
    - ``aws_arns.res.CloudWatchLogGroupStream``
    - ``aws_arns.res.RedshiftCluster``
    - ``aws_arns.res.RedshiftDatabaseName``
    - ``aws_arns.res.RedshiftDatabaseUserGroup``
    - ``aws_arns.res.RedshiftParameterGroup``
    - ``aws_arns.res.RedshiftSecurityGroup``
    - ``aws_arns.res.RedshiftServerlessManagedVpcEndpoint``
    - ``aws_arns.res.RedshiftServerlessNamespace``
    - ``aws_arns.res.RedshiftServerlessSnapshot``
    - ``aws_arns.res.RedshiftServerlessWorkgroup``
    - ``aws_arns.res.RedshiftSnapshot``
    - ``aws_arns.res.RedshiftSnapshotSchedule``
    - ``aws_arns.res.RedshiftSubnetGroup``
    - ``aws_arns.res.OpenSearchDomain``
    - ``aws_arns.res.OpenSearchServerlessCollection``
    - ``aws_arns.res.OpenSearchServerlessDashboard``
    - ``aws_arns.res.SageMakerAction``
    - ``aws_arns.res.SageMakerAlgorithm``
    - ``aws_arns.res.SageMakerApp``
    - ``aws_arns.res.SageMakerAppImageConfig``
    - ``aws_arns.res.SageMakerAutomlJob``
    - ``aws_arns.res.SageMakerCodeRepository``
    - ``aws_arns.res.SageMakerCompilationJob``
    - ``aws_arns.res.SageMakerContext``
    - ``aws_arns.res.SageMakerDataQualityJobDefinition``
    - ``aws_arns.res.SageMakerDevice``
    - ``aws_arns.res.SageMakerDeviceFleet``
    - ``aws_arns.res.SageMakerDomain``
    - ``aws_arns.res.SageMakerEndpoint``
    - ``aws_arns.res.SageMakerEndpointConfig``
    - ``aws_arns.res.SageMakerExperiment``
    - ``aws_arns.res.SageMakerExperimentTrial``
    - ``aws_arns.res.SageMakerExperimentTrialComponent``
    - ``aws_arns.res.SageMakerFeatureGroup``
    - ``aws_arns.res.SageMakerHub``
    - ``aws_arns.res.SageMakerHubContent``
    - ``aws_arns.res.SageMakerHyperParameterTuningJob``
    - ``aws_arns.res.SageMakerImage``
    - ``aws_arns.res.SageMakerImageVersion``
    - ``aws_arns.res.SageMakerInferenceExperiment``
    - ``aws_arns.res.SageMakerInferenceRecommendationsJob``
    - ``aws_arns.res.SageMakerLabelingJob``
    - ``aws_arns.res.SageMakerModel``
    - ``aws_arns.res.SageMakerModelBiasJobDefinition``
    - ``aws_arns.res.SageMakerModelCard``
    - ``aws_arns.res.SageMakerModelCardExportJob``
    - ``aws_arns.res.SageMakerModelExplainabilityJobDefinition``
    - ``aws_arns.res.SageMakerModelPackage``
    - ``aws_arns.res.SageMakerModelPackageGroup``
    - ``aws_arns.res.SageMakerModelQualityJobDefinition``
    - ``aws_arns.res.SageMakerMonitoringSchedule``
    - ``aws_arns.res.SageMakerMonitoringScheduleAlert``
    - ``aws_arns.res.SageMakerNotebookInstance``
    - ``aws_arns.res.SageMakerPipeline``
    - ``aws_arns.res.SageMakerPipelineExecution``
    - ``aws_arns.res.SageMakerProcessingJob``
    - ``aws_arns.res.SageMakerSharedModel``
    - ``aws_arns.res.SageMakerSharedModelEvent``
    - ``aws_arns.res.SageMakerSpace``
    - ``aws_arns.res.SageMakerStudioLifecycleConfig``
    - ``aws_arns.res.SageMakerTrainingJob``
    - ``aws_arns.res.SageMakerTransformJob``
    - ``aws_arns.res.SageMakerUserProfile``
    - ``aws_arns.res.SageMakerWorkforce``
    - ``aws_arns.res.SageMakerWorkteam``


1.0.1 (2023-09-21)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Rework the data model class implementation.
- 💥 First production ready release.
- 💥 Use the new import style ``import aws_arns.api as aws_arns``
- 💥 Add ``aws_arns.Arn`` and ``aws_arns.AwsPartitionEnum``
- 💥 Add the follow curated AWS Resource ARN to public API
    - ``aws_arns.res.LambdaFunction``
    - ``aws_arns.res.LambdaLayer``
    - ``aws_arns.res.BatchComputeEnvironment``
    - ``aws_arns.res.BatchJob``
    - ``aws_arns.res.BatchJobDefinition``
    - ``aws_arns.res.BatchJobQueue``
    - ``aws_arns.res.BatchSchedulingPolicy``
    - ``aws_arns.res.CloudFormationChangeSet``
    - ``aws_arns.res.CloudFormationStack``
    - ``aws_arns.res.CloudFormationStackSet``
    - ``aws_arns.res.CodeBuildProject``
    - ``aws_arns.res.CodeBuildRun``
    - ``aws_arns.res.CodeCommitRepository``
    - ``aws_arns.res.CodePipelinePipeline``
    - ``aws_arns.res.ClientVPNEndpoint``
    - ``aws_arns.res.DHCPOptionSet``
    - ``aws_arns.res.EbsSnapshot``
    - ``aws_arns.res.EbsVolume``
    - ``aws_arns.res.Ec2Image``
    - ``aws_arns.res.Ec2Instance``
    - ``aws_arns.res.Ec2KeyPair``
    - ``aws_arns.res.Ec2NetworkInterface``
    - ``aws_arns.res.ElasticIpAllocation``
    - ``aws_arns.res.InternetGateway``
    - ``aws_arns.res.NatGateway``
    - ``aws_arns.res.NetworkACL``
    - ``aws_arns.res.RouteTable``
    - ``aws_arns.res.SecurityGroup``
    - ``aws_arns.res.SecurityGroupRule``
    - ``aws_arns.res.SiteToSiteVPNConnection``
    - ``aws_arns.res.Subnet``
    - ``aws_arns.res.TransitGateway``
    - ``aws_arns.res.TransitGatewayAttachment``
    - ``Vpcaws_arns.res.``
    - ``aws_arns.res.VpcCustomGateway``
    - ``aws_arns.res.VpcEndpoint``
    - ``aws_arns.res.VpcPeeringConnection``
    - ``aws_arns.res.VpcPrivateGateway``
    - ``aws_arns.res.GlueCrawler``
    - ``aws_arns.res.GlueDatabase``
    - ``aws_arns.res.GlueJob``
    - ``aws_arns.res.GlueMLTransform``
    - ``aws_arns.res.GlueTable``
    - ``aws_arns.res.GlueTrigger``
    - ``aws_arns.res.IamGroup``
    - ``aws_arns.res.IamInstanceProfile``
    - ``aws_arns.res.IamPolicy``
    - ``aws_arns.res.IamRole``
    - ``aws_arns.res.IamUser``
    - ``aws_arns.res.RdsDBCluster``
    - ``aws_arns.res.RdsDBClusterParameterGroup``
    - ``aws_arns.res.RdsDBClusterSnapshot``
    - ``aws_arns.res.RdsDBInstance``
    - ``aws_arns.res.RdsDBInstanceSnapshot``
    - ``aws_arns.res.RdsDBOptionGroup``
    - ``aws_arns.res.RdsDBParameterGroup``
    - ``aws_arns.res.RdsDBSecurityGroup``
    - ``aws_arns.res.RdsDBSubnetGroup``
    - ``aws_arns.res.RdsEventSubscription``
    - ``aws_arns.res.RdsReservedDBInstance``
    - ``aws_arns.res.S3Bucket``
    - ``aws_arns.res.S3Object``
    - ``aws_arns.res.A2IHumanLoop``
    - ``aws_arns.res.A2IHumanReviewWorkflow``
    - ``aws_arns.res.A2IWorkerTaskTemplate``
    - ``aws_arns.res.SecretManagerSecret``
    - ``aws_arns.res.SnsSubscription``
    - ``aws_arns.res.SnsTopic``
    - ``aws_arns.res.SqsQueue``
    - ``aws_arns.res.SSMParameter``
    - ``aws_arns.res.SfnStateMachine``
    - ``aws_arns.res.SfnStateMachineExecution``

**Minor Improvements**

- Improve usage example jupyter notebook.


0.3.1 (2023-07-11)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Add the following AWS Resources to public API:
    - ``aws_arns.api.IamGroup``
    - ``aws_arns.api.IamUser``
    - ``aws_arns.api.IamRole``
    - ``aws_arns.api.IamPolicy``
    - ``aws_arns.api.IamInstanceProfile``
    - ``aws_arns.api.BatchComputeEnvironment``
    - ``aws_arns.api.BatchJobQueue``
    - ``aws_arns.api.BatchJobDefinition``
    - ``aws_arns.api.BatchJob``
    - ``aws_arns.api.BatchSchedulingPolicy``
    - ``aws_arns.api.A2IHumanReviewWorkflow``
    - ``aws_arns.api.A2IHumanLoop``
    - ``aws_arns.api.A2IWorkerTaskTemplate``
    - ``aws_arns.api.CloudFormationStack``
    - ``aws_arns.api.CloudFormationChangeSet``
    - ``aws_arns.api.CloudFormationStackSet``
    - ``aws_arns.api.CodeBuildProject``
    - ``aws_arns.api.CodeBuildRun``
    - ``aws_arns.api.S3Bucket``
    - ``aws_arns.api.S3Object``


0.2.1 (2023-07-11)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Breaking changes**

- Redesign the API, now we should do ``from aws_arns import api`` instead of ``from aws_arns import ...``.
- Redesign the data class, add ``CrossAccountGlobal``, ``Global``, ``Regional``, ``ResourceIdOnlyRegional``, ``ColonSeparatedRegional``, ``SlashSeparatedRegional``.

**Features and Improvements**

- Add ``iam``, ``batch`` modules.

**Miscellaneous**

- Redesign the testing strategy.


0.1.1 (2023-03-15)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- First release.
- Add ``ARN`` class.
