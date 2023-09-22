# -*- coding: utf-8 -*-

import itertools

a2i = [
    "arn:aws:sagemaker:us-east-1:111122223333:flow-definition/my_flow",
    "arn:aws:sagemaker:us-east-1:111122223333:human-loop/1a2b3c",
    "arn:aws:sagemaker:us-east-1:111122223333:human-task-ui/my-ui",
]
apigateway = [
    "arn:aws:apigateway:us-east-1::/restapis/my_rest_api/stages/my_stage/path/to/resource",
    "arn:aws:apigateway:us-east-1::/restapis/my_rest_api/deployments/my_deployment",
    "arn:aws:apigateway:us-east-1::/restapis/my_rest_api/authorizers/my_authorizer",
    "arn:aws:apigateway:us-east-1::/restapis/my_rest_api/models/my_model",
    "arn:aws:apigateway:us-east-1::/restapis/my_api/routes/my_route",
    "arn:aws:apigateway:us-east-1::/restapis/my_api/integrations/my_integration",
    "arn:aws:apigateway:us-east-1::/apis/my_api/stages/my_stage/path/to/resource",
    "arn:aws:apigateway:us-east-1::/apis/my_api/deployments/my_deployment",
    "arn:aws:apigateway:us-east-1::/apis/my_api/authorizers/my_authorizer",
    "arn:aws:apigateway:us-east-1::/apis/my_api/models/my_model",
    "arn:aws:apigateway:us-east-1::/apis/my_api/routes/my_route",
    "arn:aws:apigateway:us-east-1::/apis/my_api/integrations/my_integration",
]
batch = [
    "arn:aws:batch:us-east-1:111122223333:compute-environment/test",
    "arn:aws:batch:us-east-1:111122223333:job-queue/test",
    "arn:aws:batch:us-east-1:111122223333:job-definition/test:1",
    "arn:aws:batch:us-east-1:111122223333:job/b2957570-6bae-47b1-a2d8-af4f3030fc36",
]
cloudformation = [
    "arn:aws:cloudformation:us-east-1:111122223333:stack/my-stack/1a2b3c",
    "arn:aws:cloudformation:us-east-1:111122223333:changeSet/my-stack-name-2000-01-01/1a2b3c",
    "arn:aws:cloudformation:us-east-1:111122223333:stackset/my-stack-set:1a2b3c",
]
cloudwatch_logs = [
    "arn:aws:logs:us-east-1:111122223333:log-group:/aws/lambda/my-func:*",
    "arn:aws:logs:us-east-1:111122223333:log-group:my-log-group*:log-stream:my-log-stream*",
]
codecommit = [
    "arn:aws:codecommit:us-east-1:111122223333:test",
    "arn:aws:codebuild:us-east-1:111122223333:project/test",
    "arn:aws:codebuild:us-east-1:111122223333:build/test:08805851-8a0a-4968-9d08-c7cc0623db7b",
    "arn:aws:codebuild:us-east-1:111122223333:build-batch/test:08805851-8a0a-4968-9d08-c7cc0623db7b",
    "arn:aws:codepipeline:us-east-1:111122223333:test",
]
dynamodb = [
    "arn:aws:dynamodb:us-east-1:111122223333:table/my_table",
    "arn:aws:dynamodb::111122223333:global-table/my_global_table_name",
    "arn:aws:dynamodb:us-east-1:111122223333:table/my_table/index/my_index",
    "arn:aws:dynamodb:us-east-1:111122223333:table/my_table/stream/my_stream_label",
    "arn:aws:dynamodb:us-east-1:111122223333:table/my_table/backup/my_backup_name",
    "arn:aws:dynamodb:us-east-1:111122223333:table/my_table/export/my_export_name",
    "arn:aws:dynamodb:us-east-1:111122223333:table/my_table/import/my_import_name",
]
ec2 = [
    "arn:aws:ec2:us-east-1:111122223333:instance/*",
    "arn:aws:ec2:us-east-1:123456789012:instance/i-1234567890abcdef0",
    "arn:aws:ec2:us-east-1:123456789012:key-pair/key-1234567890abcdef0",
    "arn:aws:ec2:us-east-1:123456789012:volume/vol-1234567890abcdef0",
    "arn:aws:ec2:us-east-1:123456789012:snapshot/snap-1234567890abcdef0",
    "arn:aws:ec2:us-east-1:123456789012:network-interface/eni-1234567890abcdef0",
    "arn:aws:ec2:us-east-1:123456789012:vpc/vpc-1234567890abcdef0",
    "arn:aws:ec2:us-east-1:123456789012:subnet/subnet-1234567890abcdef0",
    "arn:aws:ec2:us-east-1:123456789012:route-table/rtb-1234567890abcdef0",
    "arn:aws:ec2:us-east-1:123456789012:internet-gateway/igw-1234567890abcdef0",
    "arn:aws:ec2:us-east-1:123456789012:natgateway/nat-1234567890abcdef0",
    "arn:aws:ec2:us-east-1:123456789012:dhcp-options/dopt-1234567890abcdef0",
    "arn:aws:ec2:us-east-1:123456789012:vpc-peering-connection/pcx-1234567890abcdef0",
    "arn:aws:ec2:us-east-1:123456789012:network-acl/acl-1234567890abcdef0",
    "arn:aws:ec2:us-east-1:123456789012:security-group/sg-1234567890abcdef0",
    "arn:aws:ec2:us-east-1:123456789012:security-group-rule/sgr-1234567890abcdef0",
    "arn:aws:ec2:us-east-1:123456789012:vpc-endpoint/vpce-1234567890abcdef0",
    "arn:aws:ec2:us-east-1:123456789012:ipv4pool-ec2/eipalloc-1234567890abcdef0",
    "arn:aws:ec2:us-east-1:123456789012:customer-gateway/cgw-1234567890abcdef0",
    "arn:aws:ec2:us-east-1:123456789012:vpn-gateway/vgw-1234567890abcdef0",
    "arn:aws:ec2:us-east-1:123456789012:vpn-connection/vpn-1234567890abcdef0",
    "arn:aws:ec2:us-east-1:123456789012:client-vpn-endpoint/cvpn-endpoint-1234567890abcdef0",
    "arn:aws:ec2:us-east-1:123456789012:transit-gateway/tgw-1234567890abcdef0",
    "arn:aws:ec2:us-east-1:123456789012:transit-gateway-attachment/tgw-attach-1234567890abcdef0",
    "arn:aws:ec2:us-east-1::image/ami-1234567890abcdef0",
]
ecr = [
    "arn:aws:ecr:us-east-1:123456789012:repository/my-repo",
]
ecs = [
    "arn:aws:ecs:us-east-1:111122223333:cluster/my-cluster-1",
    "arn:aws:ecs:us-east-1:111122223333:task-definition/my-task:1",
    "arn:aws:ecs:us-east-1:111122223333:container-instance/my-cluster/container_instance_UUID",
    "arn:aws:ecs:us-east-1:111122223333:service/service_name",
]
glue = [
    "arn:aws:glue:us-east-1:111122223333:catalog",
    "arn:aws:glue:us-east-1:111122223333:database/db1",
    "arn:aws:glue:us-east-1:111122223333:table/db1/tbl",
    "arn:aws:glue:us-east-1:111122223333:crawler/mycrawler",
    "arn:aws:glue:us-east-1:111122223333:job/testjob",
    "arn:aws:glue:us-east-1:111122223333:trigger/sampletrigger",
    "arn:aws:glue:us-east-1:111122223333:devEndpoint/temporarydevendpoint",
    "arn:aws:glue:us-east-1:111122223333:mlTransform/tfm-1234567890",
]
kinesis = [
    "arn:aws:kinesisvideo:us-east-1:111122223333:stream/kinesis-stream-name/111122223333",
]
kms = [
    "arn:aws:kms:us-east-1:111122223333:key/1a2b3c",
    "arn:aws:kms:us-east-1:111122223333:alias/my_key",
]
lambda_func = [
    "arn:aws:lambda:us-east-1:111122223333:function:my-func",
    "arn:aws:lambda:us-east-1:111122223333:function:my-func:LIVE",
    "arn:aws:lambda:us-east-1:111122223333:function:my-func:1",
    "arn:aws:lambda:us-east-1:111122223333:layer:my-layer:1",
]
macie = [
    "arn:aws:macie:us-east-1:111122223333:trigger/example0954663fda0f652e304dcc21323508db/alert/example09214d3e70fb6092cc93cee96dbc4de6",
]
opensearch = [
    "arn:aws:es:us-east-1:111122223333:domain/my_domain",
]
opensearch_serverless = [
    "arn:aws:aoss:us-east-1:111122223333:collection/collection_id",
    "arn:aws:aoss:us-east-1:111122223333:dashboards/default",
]
rds = [
    "arn:aws:rds:us-east-1:111122223333:db:my-mysql-instance-1",
    "arn:aws:rds:us-east-1:111122223333:cluster:my-aurora-cluster-1",
    "arn:aws:rds:us-east-1:111122223333:es:my-subscription",
    "arn:aws:rds:us-east-1:111122223333:og:my-og",
    "arn:aws:rds:us-east-1:123456789012:pg:my-param-enable-logs",
    "arn:aws:rds:us-east-1:111122223333:cluster-pg:my-cluster-param-timezone",
    "arn:aws:rds:us-east-1:111122223333:ri:my-reserved-postgresql",
    "arn:aws:rds:us-east-1:111122223333:secgrp:my-public",
    "arn:aws:rds:us-east-1:111122223333:snapshot:rds:my-mysql-db-2020-01-01-00-00",
    "arn:aws:rds:us-east-1:111122223333:cluster-snapshot:rds:my-aurora-cluster-2020-01-01-00-00",
    "arn:aws:rds:us-east-1:111122223333:snapshot:my-mysql-db-snap",
    "arn:aws:rds:us-east-1:111122223333:cluster-snapshot:my-aurora-cluster-snap",
    "arn:aws:rds:us-east-1:111122223333:subgrp:my-subnet-10",
]
redshift = [
    "arn:aws:redshift:us-east-1:111122223333:cluster:my_cluster",
    "arn:aws:redshift:us-east-1:111122223333:dbgroup:my_cluster/my_db_group",
    "arn:aws:redshift:us-east-1:111122223333:dbname:my_cluster/my_database",
    "arn:aws:redshift:us-east-1:111122223333:snapshot:my_cluster/my_snapshot",
    "arn:aws:redshift:us-east-1:111122223333:snapshotschedule:my_snapshot_schedule",
    "arn:aws:redshift:us-east-1:111122223333:parametergroup:my_parameter_group",
    "arn:aws:redshift:us-east-1:111122223333:subnetgroup:my_subnet_group",
    "arn:aws:redshift:us-east-1:111122223333:securitygroup:my_group_name/ec2securitygroup/owner_name/sg-1a2b",
]
redshift_serverless = [
    "arn:aws:redshift-serverless:us-east-1:111122223333:namespace/my_namespace",
    "arn:aws:redshift-serverless:us-east-1:111122223333:workgroup/my_workgroup",
    "arn:aws:redshift-serverless:us-east-1:111122223333:snapshot/my_snapshot",
    "arn:aws:redshift-serverless:us-east-1:111122223333:managedvpcendpoint/my_vpc_endpoint",
]
s3 = [
    "arn:aws:s3:::my-bucket",
    "arn:aws:s3:::my-bucket/cloudformation/upload/10f3db7bcfa62c69e5a71fef595fac84.json",
]
sagemaker = [
    "arn:aws:sagemaker:us-east-1:111122223333:action/my_action",
    "arn:aws:sagemaker:us-east-1:111122223333:algorithm/my_algorithm",
    "arn:aws:sagemaker:us-east-1:111122223333:app-image-config/my_app_image_config",
    "arn:aws:sagemaker:us-east-1:111122223333:automl-job/my_automl_job",
    "arn:aws:sagemaker:us-east-1:111122223333:code-repository/my_code_repository",
    "arn:aws:sagemaker:us-east-1:111122223333:compilation-job/my_compilation_job",
    "arn:aws:sagemaker:us-east-1:111122223333:context/my_context",
    "arn:aws:sagemaker:us-east-1:111122223333:data-quality-job-definition/my_data_quality_job_definition",
    "arn:aws:sagemaker:us-east-1:111122223333:endpoint/my_endpoint",
    "arn:aws:sagemaker:us-east-1:111122223333:endpoint-config/my_endpoint_config",
    "arn:aws:sagemaker:us-east-1:111122223333:experiment/my_experiment",
    "arn:aws:sagemaker:us-east-1:111122223333:experiment-trial/",
    "arn:aws:sagemaker:us-east-1:111122223333:experiment-trial-component/",
    "arn:aws:sagemaker:us-east-1:111122223333:feature-group/",
    "arn:aws:sagemaker:us-east-1:111122223333:hub/my_hub",
    "arn:aws:sagemaker:us-east-1:111122223333:hub-content/my_hub/my_hub_content_type/my_hub_content_name",
    "arn:aws:sagemaker:us-east-1:111122223333:hyper-parameter-tuning-job/my_hyper_parameter_tuning_job",
    "arn:aws:sagemaker:us-east-1:111122223333:image/my_image",
    "arn:aws:sagemaker:us-east-1:111122223333:image-version/my_image/1",
    "arn:aws:sagemaker:us-east-1:111122223333:inference-experiment/my_inference_experiment",
    "arn:aws:sagemaker:us-east-1:111122223333:inference-recommendations-job/my_inference_recommendations_job",
    "arn:aws:sagemaker:us-east-1:111122223333:labeling-job/my_labeling_job",
    "arn:aws:sagemaker:us-east-1:111122223333:model/my_model",
    "arn:aws:sagemaker:us-east-1:111122223333:model-bias-job-definition/my_model_bias_job_definition",
    "arn:aws:sagemaker:us-east-1:111122223333:model-card/my_model_card",
    "arn:aws:sagemaker:us-east-1:111122223333:model-card/my_model_card/export-job/my_export_job_name",
    "arn:aws:sagemaker:us-east-1:111122223333:model-explainability-job-definition/my_model_explainability_job_definition",
    "arn:aws:sagemaker:us-east-1:111122223333:model-package/my_model_package",
    "arn:aws:sagemaker:us-east-1:111122223333:model-package-group/my_model_package_group",
    "arn:aws:sagemaker:us-east-1:111122223333:model-quality-job-definition/my_model_quality_job_definition",
    "arn:aws:sagemaker:us-east-1:111122223333:monitoring-schedule/my_monitoring_schedule",
    "arn:aws:sagemaker:us-east-1:111122223333:monitoring-schedule/my_monitoring_schedule/alert/my_monitoring_schedule_alert_name",
    "arn:aws:sagemaker:us-east-1:111122223333:notebook-instance/my_notebook_instance",
    "arn:aws:sagemaker:us-east-1:111122223333:pipeline/my_pipeline",
    "arn:aws:sagemaker:us-east-1:111122223333:pipeline/my_pipeline/execution/1a2b3c",
    "arn:aws:sagemaker:us-east-1:111122223333:processing-job/my_processing_job",
    "arn:aws:sagemaker:us-east-1:111122223333:shared-model/share_model_id",
    "arn:aws:sagemaker:us-east-1:111122223333:shared-model-event/share_model_event_id",
    "arn:aws:sagemaker:us-east-1:111122223333:training-job/my_training_job",
    "arn:aws:sagemaker:us-east-1:111122223333:transform-job/my_transform_job",
    "arn:aws:sagemaker:us-east-1:111122223333:workforce/my_workforce",
    "arn:aws:sagemaker:us-east-1:111122223333:workteam/my_workteam",
    "arn:aws:sagemaker:us-east-1:111122223333:domain/domain_id",
    "arn:aws:sagemaker:us-east-1:111122223333:user-profile/domain_id/my_user_profile",
    "arn:aws:sagemaker:us-east-1:111122223333:space/domain_id/my_space",
    "arn:aws:sagemaker:us-east-1:111122223333:app/domain_id/my_user_profile/my_app_type/my_app_name",
    "arn:aws:sagemaker:us-east-1:111122223333:studio-lifecycle-config/my_studio_lifecycle_config",
    "arn:aws:sagemaker:us-east-1:111122223333:device-fleet/fleet_name/device/device_name",
    "arn:aws:sagemaker:us-east-1:111122223333:device-fleet/fleet_name",
]
secretmanager = [
    "arn:aws:secretsmanager:us-east-1:111122223333:secret:MyFolder/MySecret-a1b2c3",
]
sfn = [
    "arn:aws:states:us-east-1:111122223333:stateMachine:standard_test",
    "arn:aws:states:us-east-1:111122223333:stateMachine:express_test",
    "arn:aws:states:us-east-1:807388292768:stateMachine:standard_test:1",
    "arn:aws:states:us-east-1:807388292768:stateMachine:standard_test:LIVE",
    "arn:aws:states:us-east-1:111122223333:execution:standard_test:1d858cf6-613f-4576-b94f-e0d654c23843",
    "arn:aws:states:us-east-1:111122223333:express:express_test:e935dec6-e748-4977-a2f2-32eeb83d81da:b2f7726e-9b98-4a49-a6c4-9cf23a61f180",
]
sns = [
    "arn:aws:sns:us-east-1:111122223333:my_topic",
    "arn:aws:sns:us-east-1:111122223333:my_topic:a07e1034-10c0-47a6-83c2-552cfcca42db",
]
sqs = [
    "arn:aws:sqs:us-east-1:111122223333:my_queue",
]
ssm = [
    "arn:aws:ssm:us-east-1:111122223333:parameter/my_param",
    "arn:aws:ssm:us-east-1:111122223333:parameter/path/to/my_param",
]

arns = list(
    itertools.chain(
        a2i,
        apigateway,
        batch,
        cloudformation,
        cloudwatch_logs,
        codecommit,
        dynamodb,
        ec2,
        ecr,
        ecs,
        glue,
        kinesis,
        kms,
        lambda_func,
        macie,
        opensearch,
        opensearch_serverless,
        rds,
        redshift,
        redshift_serverless,
        s3,
        sagemaker,
        secretmanager,
        sfn,
        sns,
        sqs,
        ssm,
    )
)
