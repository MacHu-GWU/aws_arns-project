# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import dataclasses

from ..model import _SlashSeparatedRegional


@dataclasses.dataclass
class SageMaker(_SlashSeparatedRegional):
    service: str = dataclasses.field(default="sagemaker")


@dataclasses.dataclass
class _SageMakerCommon(SageMaker):
    @property
    def name(self) -> str:
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        name: str,
    ):
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=name,
        )


@dataclasses.dataclass
class SageMakerAction(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:action/my_action
    """

    resource_type: str = dataclasses.field(default="action")


@dataclasses.dataclass
class SageMakerAlgorithm(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:algorithm/my_algorithm
    """

    resource_type: str = dataclasses.field(default="algorithm")


@dataclasses.dataclass
class SageMakerAppImageConfig(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:app-image-config/my_app_image_config
    """

    resource_type: str = dataclasses.field(default="app-image-config")


@dataclasses.dataclass
class SageMakerAutomlJob(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:automl-job/my_automl_job
    """

    resource_type: str = dataclasses.field(default="automl-job")


@dataclasses.dataclass
class SageMakerCodeRepository(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:code-repository/my_code_repository
    """

    resource_type: str = dataclasses.field(default="code-repository")


@dataclasses.dataclass
class SageMakerCompilationJob(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:compilation-job/my_compilation_job
    """

    resource_type: str = dataclasses.field(default="compilation-job")


@dataclasses.dataclass
class SageMakerContext(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:context/my_context
    """

    resource_type: str = dataclasses.field(default="context")


@dataclasses.dataclass
class SageMakerDataQualityJobDefinition(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:data-quality-job-definition/my_data_quality_job_definition
    """

    resource_type: str = dataclasses.field(default="data-quality-job-definition")


@dataclasses.dataclass
class SageMakerEndpoint(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:endpoint/my_endpoint
    """

    resource_type: str = dataclasses.field(default="endpoint")


@dataclasses.dataclass
class SageMakerEndpointConfig(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:endpoint-config/my_endpoint_config
    """

    resource_type: str = dataclasses.field(default="endpoint-config")


@dataclasses.dataclass
class SageMakerExperiment(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:experiment/my_experiment
    """

    resource_type: str = dataclasses.field(default="experiment")


@dataclasses.dataclass
class SageMakerExperimentTrial(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:experiment-trial/
    """

    resource_type: str = dataclasses.field(default="experiment-trial")


@dataclasses.dataclass
class SageMakerExperimentTrialComponent(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:experiment-trial-component/
    """

    resource_type: str = dataclasses.field(default="experiment-trial-component")


@dataclasses.dataclass
class SageMakerFeatureGroup(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:feature-group/
    """

    resource_type: str = dataclasses.field(default="feature-group")


@dataclasses.dataclass
class SageMakerHub(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:hub/my_hub
    """

    resource_type: str = dataclasses.field(default="hub")


@dataclasses.dataclass
class SageMakerHubContent(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:hub-content/my_hub/my_hub_content_type/my_hub_content_name
    """

    resource_type: str = dataclasses.field(default="hub-content")


@dataclasses.dataclass
class SageMakerHyperParameterTuningJob(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:hyper-parameter-tuning-job/my_hyper_parameter_tuning_job
    """

    resource_type: str = dataclasses.field(default="hyper-parameter-tuning-job")


@dataclasses.dataclass
class SageMakerImage(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:image/my_image
    """

    resource_type: str = dataclasses.field(default="image")


@dataclasses.dataclass
class SageMakerImageVersion(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:image-version/my_image/1
    """

    resource_type: str = dataclasses.field(default="image-version")


@dataclasses.dataclass
class SageMakerInferenceExperiment(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:inference-experiment/my_inference_experiment
    """

    resource_type: str = dataclasses.field(default="inference-experiment")


@dataclasses.dataclass
class SageMakerInferenceRecommendationsJob(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:inference-recommendations-job/my_inference_recommendations_job
    """

    resource_type: str = dataclasses.field(default="inference-recommendations-job")


@dataclasses.dataclass
class SageMakerLabelingJob(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:labeling-job/my_labeling_job
    """

    resource_type: str = dataclasses.field(default="labeling-job")


@dataclasses.dataclass
class SageMakerModel(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:model/my_model
    """

    resource_type: str = dataclasses.field(default="model")


@dataclasses.dataclass
class SageMakerModelBiasJobDefinition(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:model-bias-job-definition/my_model_bias_job_definition
    """

    resource_type: str = dataclasses.field(default="model-bias-job-definition")


@dataclasses.dataclass
class SageMakerModelCard(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:model-card/my_model_card
    """

    resource_type: str = dataclasses.field(default="model-card")


@dataclasses.dataclass
class SageMakerModelCardExportJob(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:model-card/my_model_card/export-job/my_export_job_name
    """

    resource_type: str = dataclasses.field(default="model-card")


@dataclasses.dataclass
class SageMakerModelExplainabilityJobDefinition(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:model-explainability-job-definition/my_model_explainability_job_definition
    """

    resource_type: str = dataclasses.field(
        default="model-explainability-job-definition"
    )


@dataclasses.dataclass
class SageMakerModelPackage(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:model-package/my_model_package
    """

    resource_type: str = dataclasses.field(default="model-package")


@dataclasses.dataclass
class SageMakerModelPackageGroup(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:model-package-group/my_model_package_group
    """

    resource_type: str = dataclasses.field(default="model-package-group")


@dataclasses.dataclass
class SageMakerModelQualityJobDefinition(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:model-quality-job-definition/my_model_quality_job_definition
    """

    resource_type: str = dataclasses.field(default="model-quality-job-definition")


@dataclasses.dataclass
class SageMakerMonitoringSchedule(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:monitoring-schedule/my_monitoring_schedule
    """

    resource_type: str = dataclasses.field(default="monitoring-schedule")


@dataclasses.dataclass
class SageMakerMonitoringScheduleAlert(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:monitoring-schedule/my_monitoring_schedule/alert/my_monitoring_schedule_alert_name
    """

    resource_type: str = dataclasses.field(default="monitoring-schedule")


@dataclasses.dataclass
class SageMakerNotebookInstance(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:notebook-instance/my_notebook_instance
    """

    resource_type: str = dataclasses.field(default="notebook-instance")


@dataclasses.dataclass
class SageMakerPipeline(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:pipeline/my_pipeline
    """

    resource_type: str = dataclasses.field(default="pipeline")


@dataclasses.dataclass
class SageMakerPipelineExecution(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:pipeline/my_pipeline/execution/1a2b3c
    """

    resource_type: str = dataclasses.field(default="pipeline")


@dataclasses.dataclass
class SageMakerProcessingJob(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:processing-job/my_processing_job
    """

    resource_type: str = dataclasses.field(default="processing-job")


@dataclasses.dataclass
class SageMakerSharedModel(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:shared-model/share_model_id
    """

    resource_type: str = dataclasses.field(default="shared-model")


@dataclasses.dataclass
class SageMakerSharedModelEvent(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:shared-model-event/share_model_event_id
    """

    resource_type: str = dataclasses.field(default="shared-model-event")


@dataclasses.dataclass
class SageMakerTrainingJob(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:training-job/my_training_job
    """

    resource_type: str = dataclasses.field(default="training-job")


@dataclasses.dataclass
class SageMakerTransformJob(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:transform-job/my_transform_job
    """

    resource_type: str = dataclasses.field(default="transform-job")


@dataclasses.dataclass
class SageMakerWorkforce(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:workforce/my_workforce
    """

    resource_type: str = dataclasses.field(default="workforce")


@dataclasses.dataclass
class SageMakerWorkteam(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:workteam/my_workteam
    """

    resource_type: str = dataclasses.field(default="workteam")


@dataclasses.dataclass
class SageMakerDomain(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:domain/domain_id
    """

    resource_type: str = dataclasses.field(default="domain")


@dataclasses.dataclass
class SageMakerUserProfile(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:user-profile/domain_id/my_user_profile
    """

    resource_type: str = dataclasses.field(default="user-profile")


@dataclasses.dataclass
class SageMakerSpace(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:space/domain_id/my_space
    """

    resource_type: str = dataclasses.field(default="space")


@dataclasses.dataclass
class SageMakerApp(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:app/domain_id/my_user_profile/my_app_type/my_app_name
    """

    resource_type: str = dataclasses.field(default="app")


@dataclasses.dataclass
class SageMakerStudioLifecycleConfig(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:studio-lifecycle-config/my_studio_lifecycle_config
    """

    resource_type: str = dataclasses.field(default="studio-lifecycle-config")


@dataclasses.dataclass
class SageMakerDevice(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:device-fleet/fleet_name/device/device_name
    """

    resource_type: str = dataclasses.field(default="device-fleet")


@dataclasses.dataclass
class SageMakerDeviceFleet(_SageMakerCommon):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:device-fleet/fleet_name
    """

    resource_type: str = dataclasses.field(default="device-fleet")
