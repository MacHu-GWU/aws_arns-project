# -*- coding: utf-8 -*-

from aws_arns.srv.sagemaker import (
    _SageMakerCommon,
    SageMakerAction,
    SageMakerAlgorithm,
    SageMakerAppImageConfig,
    SageMakerAutomlJob,
    SageMakerCodeRepository,
    SageMakerCompilationJob,
    SageMakerContext,
    SageMakerDataQualityJobDefinition,
    SageMakerEndpoint,
    SageMakerEndpointConfig,
    SageMakerExperiment,
    SageMakerExperimentTrial,
    SageMakerExperimentTrialComponent,
    SageMakerFeatureGroup,
    SageMakerHub,
    SageMakerHubContent,
    SageMakerHyperParameterTuningJob,
    SageMakerImage,
    SageMakerImageVersion,
    SageMakerInferenceExperiment,
    SageMakerInferenceRecommendationsJob,
    SageMakerLabelingJob,
    SageMakerModel,
    SageMakerModelBiasJobDefinition,
    SageMakerModelCard,
    SageMakerModelCardExportJob,
    SageMakerModelExplainabilityJobDefinition,
    SageMakerModelPackage,
    SageMakerModelPackageGroup,
    SageMakerModelQualityJobDefinition,
    SageMakerMonitoringSchedule,
    SageMakerMonitoringScheduleAlert,
    SageMakerNotebookInstance,
    SageMakerPipeline,
    SageMakerPipelineExecution,
    SageMakerProcessingJob,
    SageMakerSharedModel,
    SageMakerSharedModelEvent,
    SageMakerTrainingJob,
    SageMakerTransformJob,
    SageMakerWorkforce,
    SageMakerWorkteam,
    SageMakerDomain,
    SageMakerUserProfile,
    SageMakerSpace,
    SageMakerApp,
    SageMakerStudioLifecycleConfig,
    SageMakerDevice,
    SageMakerDeviceFleet,
)


def test():
    class_and_arn_pairs = [
        (SageMakerAction, "arn:aws:sagemaker:us-east-1:111122223333:action/my_action"),
        (SageMakerAlgorithm, "arn:aws:sagemaker:us-east-1:111122223333:algorithm/my_algorithm"),
        (SageMakerAppImageConfig, "arn:aws:sagemaker:us-east-1:111122223333:app-image-config/my_app_image_config"),
        (SageMakerAutomlJob, "arn:aws:sagemaker:us-east-1:111122223333:automl-job/my_automl_job"),
        (SageMakerCodeRepository, "arn:aws:sagemaker:us-east-1:111122223333:code-repository/my_code_repository"),
        (SageMakerCompilationJob, "arn:aws:sagemaker:us-east-1:111122223333:compilation-job/my_compilation_job"),
        (SageMakerContext, "arn:aws:sagemaker:us-east-1:111122223333:context/my_context"),
        (SageMakerDataQualityJobDefinition, "arn:aws:sagemaker:us-east-1:111122223333:data-quality-job-definition/my_data_quality_job_definition"),
        (SageMakerEndpoint, "arn:aws:sagemaker:us-east-1:111122223333:endpoint/my_endpoint"),
        (SageMakerEndpointConfig, "arn:aws:sagemaker:us-east-1:111122223333:endpoint-config/my_endpoint_config"),
        (SageMakerExperiment, "arn:aws:sagemaker:us-east-1:111122223333:experiment/my_experiment"),
        (SageMakerExperimentTrial, "arn:aws:sagemaker:us-east-1:111122223333:experiment-trial/"),
        (SageMakerExperimentTrialComponent, "arn:aws:sagemaker:us-east-1:111122223333:experiment-trial-component/"),
        (SageMakerFeatureGroup, "arn:aws:sagemaker:us-east-1:111122223333:feature-group/"),
        (SageMakerHub, "arn:aws:sagemaker:us-east-1:111122223333:hub/my_hub"),
        (SageMakerHubContent, "arn:aws:sagemaker:us-east-1:111122223333:hub-content/my_hub/my_hub_content_type/my_hub_content_name"),
        (SageMakerHyperParameterTuningJob, "arn:aws:sagemaker:us-east-1:111122223333:hyper-parameter-tuning-job/my_hyper_parameter_tuning_job"),
        (SageMakerImage, "arn:aws:sagemaker:us-east-1:111122223333:image/my_image"),
        (SageMakerImageVersion, "arn:aws:sagemaker:us-east-1:111122223333:image-version/my_image/1"),
        (SageMakerInferenceExperiment, "arn:aws:sagemaker:us-east-1:111122223333:inference-experiment/my_inference_experiment"),
        (SageMakerInferenceRecommendationsJob, "arn:aws:sagemaker:us-east-1:111122223333:inference-recommendations-job/my_inference_recommendations_job"),
        (SageMakerLabelingJob, "arn:aws:sagemaker:us-east-1:111122223333:labeling-job/my_labeling_job"),
        (SageMakerModel, "arn:aws:sagemaker:us-east-1:111122223333:model/my_model"),
        (SageMakerModelBiasJobDefinition, "arn:aws:sagemaker:us-east-1:111122223333:model-bias-job-definition/my_model_bias_job_definition"),
        (SageMakerModelCard, "arn:aws:sagemaker:us-east-1:111122223333:model-card/my_model_card"),
        (SageMakerModelCardExportJob, "arn:aws:sagemaker:us-east-1:111122223333:model-card/my_model_card/export-job/my_export_job_name"),
        (SageMakerModelExplainabilityJobDefinition, "arn:aws:sagemaker:us-east-1:111122223333:model-explainability-job-definition/my_model_explainability_job_definition"),
        (SageMakerModelPackage, "arn:aws:sagemaker:us-east-1:111122223333:model-package/my_model_package"),
        (SageMakerModelPackageGroup, "arn:aws:sagemaker:us-east-1:111122223333:model-package-group/my_model_package_group"),
        (SageMakerModelQualityJobDefinition, "arn:aws:sagemaker:us-east-1:111122223333:model-quality-job-definition/my_model_quality_job_definition"),
        (SageMakerMonitoringSchedule, "arn:aws:sagemaker:us-east-1:111122223333:monitoring-schedule/my_monitoring_schedule"),
        (SageMakerMonitoringScheduleAlert, "arn:aws:sagemaker:us-east-1:111122223333:monitoring-schedule/my_monitoring_schedule/alert/my_monitoring_schedule_alert_name"),
        (SageMakerNotebookInstance, "arn:aws:sagemaker:us-east-1:111122223333:notebook-instance/my_notebook_instance"),
        (SageMakerPipeline, "arn:aws:sagemaker:us-east-1:111122223333:pipeline/my_pipeline"),
        (SageMakerPipelineExecution, "arn:aws:sagemaker:us-east-1:111122223333:pipeline/my_pipeline/execution/1a2b3c"),
        (SageMakerProcessingJob, "arn:aws:sagemaker:us-east-1:111122223333:processing-job/my_processing_job"),
        (SageMakerSharedModel, "arn:aws:sagemaker:us-east-1:111122223333:shared-model/share_model_id"),
        (SageMakerSharedModelEvent, "arn:aws:sagemaker:us-east-1:111122223333:shared-model-event/share_model_event_id"),
        (SageMakerTrainingJob, "arn:aws:sagemaker:us-east-1:111122223333:training-job/my_training_job"),
        (SageMakerTransformJob, "arn:aws:sagemaker:us-east-1:111122223333:transform-job/my_transform_job"),
        (SageMakerWorkforce, "arn:aws:sagemaker:us-east-1:111122223333:workforce/my_workforce"),
        (SageMakerWorkteam, "arn:aws:sagemaker:us-east-1:111122223333:workteam/my_workteam"),
        (SageMakerDomain, "arn:aws:sagemaker:us-east-1:111122223333:domain/domain_id"),
        (SageMakerUserProfile, "arn:aws:sagemaker:us-east-1:111122223333:user-profile/domain_id/my_user_profile"),
        (SageMakerSpace, "arn:aws:sagemaker:us-east-1:111122223333:space/domain_id/my_space"),
        (SageMakerApp, "arn:aws:sagemaker:us-east-1:111122223333:app/domain_id/my_user_profile/my_app_type/my_app_name"),
        (SageMakerStudioLifecycleConfig, "arn:aws:sagemaker:us-east-1:111122223333:studio-lifecycle-config/my_studio_lifecycle_config"),
        (SageMakerDevice, "arn:aws:sagemaker:us-east-1:111122223333:device-fleet/fleet_name/device/device_name"),
        (SageMakerDeviceFleet, "arn:aws:sagemaker:us-east-1:111122223333:device-fleet/fleet_name"),
    ]
    for class_, arn in class_and_arn_pairs:
        obj: _SageMakerCommon = class_.from_arn(arn)
        assert obj.to_arn() == arn
        assert (
            class_.new(
                obj.aws_account_id,
                obj.aws_region,
                obj.name,
            )
            == obj
        )


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.srv.sagemaker", preview=False)
