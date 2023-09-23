# -*- coding: utf-8 -*-

"""
Data model classes for AWS ARNs.
"""

import typing as T
import dataclasses

from .constants import AwsPartitionEnum


def _handle_empty_str(s: str) -> T.Optional[str]:
    """
    This function is used to parse ARN attributes that are optional.
    """
    if s:
        return s
    else:
        return None


def _handle_none(s: T.Optional[str]) -> str:
    """
    This function is used to serialize ARN attributes that are optional.
    """
    if s is None:
        return ""
    else:
        return s


class AwsService:
    """
    List of AWS service name for ARN attribute.
    """
    access_analyzer = "access-analyzer"
    account = "account"
    alexa_for_business = "a4b"
    managed_service_for_prometheus = "aps"
    amplify = "amplify"
    amplify_admin = "amplifybackend"
    amplify_ui_builder = "amplifyuibuilder"
    apache_kafka_api_for_msk = "kafka"
    apigateway = "apigateway"
    app_mesh = "appmesh"
    app_runner = "apprunner"
    app_config = "appconfig"
    app_fabric = "appfabric"
    app_flow = "appflow"
    app_integrations = "app-integrations"
    app_sync = "appsync"
    artifact = "artifact"
    aws_supply_chain = "scn"
    athena = "athena"
    audit_manager = "auditmanager"
    awslambda = "lambda"
    backup = "backup"
    backup_gateway = "backup-gateway"
    batch = "batch"
    bedrock = "bedrock"
    certificate_manager = "acm"
    chatbot = "chatbot"
    chime = "chime"
    clouddirectory = "clouddirectory"
    cloudmap = "servicediscovery"
    cloudhsm = "cloudhsm"
    cloud9 = "cloud9"
    cloudfront = "cloudfront"
    cloudsearch = "cloudsearch"
    cloudshell = "cloudshell"
    cloudtrail = "cloudtrail"
    cloudwatch = "cloudwatch"
    cloudwatch_logs = "logs"
    cloudformation = "cloudformation"
    codeartifact = "codeartifact"
    codecommit = "codecommit"
    codebuild = "codebuild"
    codepipeline = "codepipeline"
    codecatalyst = "codecatalyst"
    codedeploy = "codedeploy"
    codestar = "codestar"
    codewhisperer = "codewhisperer"
    cognito_identity = "cognito-identity"
    cognito_sync = "cognito-sync"
    cognito_idp = "cognito-idp"
    comprehend = "comprehend"
    comprehend_medical = "comprehendmedical"
    config = "config"
    connect = "connect"
    control_tower = "controltower"
    cost_and_usage_report = "cur"
    cost_explorer = "ce"
    data_exchange = "dataexchange"
    data_pipeline = "datapipeline"
    databrew = "databrew"
    datasync = "datasync"
    datazone = "datazone"
    dbqms = "dbqms"
    deepcomposer = "deepcomposer"
    deeplens = "deeplens"
    deepracer = "deepracer"
    detective = "detective"
    device_farm = "devicefarm"
    direct_connect = "directconnect"
    director_service = "ds"
    dms = "dms"
    documentdb_elastic_cluster = "docdb-elastic"
    disaster_recovery_service = "drs"
    dynamodb = "dynamodb"
    dynamodb_accelerator = "dax"
    ec2 = "ec2"
    ec2_auto_scaling = "autoscaling"
    ec2_image_builder = "imagebuilder"
    efs = "elasticfilesystem"
    ecr = "ecr"
    ecr_public = "ecr-public"
    ecs = "ecs"
    eks = "eks"
    elastic_beanstalk = "elasticbeanstalk"
    elastic_transcoder = "elastictranscoder"
    elastic_cache = "elasticache"
    elastic_load_balancer = "elasticloadbalancing"
    emr = "elasticmapreduce"
    event_bridge = "events"
    execute_api = "execute-api"
    glue = "glue"
    iam = "iam"
    logs = "logs"
    rds = "rds"
    s3 = "s3"
    sagemaker = "sagemaker"
    secretsmanager = "secretsmanager"
    sns = "sns"
    sqs = "sqs"
    ssm = "ssm"
    states = "states"


class _Nothing:
    pass


NOTHING = _Nothing()


@dataclasses.dataclass
class BaseArn:
    """
    Amazon Resource Names (ARNs) data model. is a unique identifier for AWS resources.

    ARN format::

        - format: arn:${partition}:${service}:${region}:${account-id}:${resource-id}
            - example: arn:aws:sqs:us-east-1:111122223333:my-queue
        - format: arn:${partition}:${service}:${region}:${account-id}:${resource-type}${sep}${resource-id}
            - example sep = "/": arn:aws:iam::111122223333:role/aws-service-role/batch.amazonaws.com/AWSServiceRoleForBatch
        - format: arn:${partition}:${service}:${region}:${account-id}:${resource-type}${sep}${resource-id}
            - example sep = ":": arn:aws:lambda:us-east-1:111122223333:function:my-func

    Reference:

    - Amazon Resource Names (ARNs): https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html

    .. note::

        Don't initialize this class directly, use the class method :meth:`new` instead.
    """

    partition: str = dataclasses.field(default="aws")
    service: str = dataclasses.field(default=NOTHING)
    region: T.Optional[str] = dataclasses.field(default=NOTHING)
    account_id: T.Optional[str] = dataclasses.field(default=NOTHING)
    resource_type: T.Optional[str] = dataclasses.field(default=NOTHING)
    sep: T.Optional[str] = dataclasses.field(default=NOTHING)
    resource_id: str = dataclasses.field(default=NOTHING)

    def __post_init__(self):
        for k, v in dataclasses.asdict(self).items():
            if isinstance(v, _Nothing):
                raise ValueError(f"arg '{k}' is required")

    @staticmethod
    def _parse_slash_delimited_resource(service: str, resource: str):
        # "arn:aws:s3:::my-bucket/file.txt"
        if service in ["s3", "apigateway"]:
            sep = None
            resource_type, resource_id = None, resource
        # arn:aws:ssm:us-east-1:807388292768:parameter/path/to/my_param
        elif service in ["ssm"]:
            sep = "/"
            resource_type, resource_id = resource.split("/", 1)
            if resource.count("/") > 1:
                resource_id = f"/{resource_id}"
        else:
            sep = "/"
            resource_type, resource_id = resource.split("/", 1)
        return sep, resource_type, resource_id

    @staticmethod
    def _parse_colon_delimited_resource(service: str, resource: str):
        if service in ["sns"]:
            sep = None
            resource_type, resource_id = None, resource
        else:
            sep = ":"
            resource_type, resource_id = resource.split(":", 1)
        return sep, resource_type, resource_id

    @classmethod
    def from_arn(cls, arn: str):
        """
        parse arn string into Arn object.
        """
        if not arn.startswith("arn:"):
            raise ValueError(f"Invalid ARN: {arn!r}")

        _, partition, service, region, account_id, resource = arn.split(":", 5)

        if "/" in resource and ":" in resource:
            if resource.index("/") < resource.index(":"):
                (
                    sep,
                    resource_type,
                    resource_id,
                ) = cls._parse_slash_delimited_resource(service, resource)
            else:
                (
                    sep,
                    resource_type,
                    resource_id,
                ) = cls._parse_colon_delimited_resource(service, resource)
        elif "/" in resource:
            (
                sep,
                resource_type,
                resource_id,
            ) = cls._parse_slash_delimited_resource(service, resource)
        elif ":" in resource:
            (
                sep,
                resource_type,
                resource_id,
            ) = cls._parse_colon_delimited_resource(service, resource)
        else:
            sep = None
            resource_type, resource_id = None, resource

        return cls(
            partition=partition,
            service=service,
            region=_handle_empty_str(region),
            account_id=_handle_empty_str(account_id),
            resource_type=resource_type,
            sep=sep,
            resource_id=resource_id,
        )

    def to_arn(self) -> str:
        """
        convert Arn object into arn string.
        """
        if self.sep:
            if self.sep == "/" and self.resource_id.startswith("/"):
                resource = f"{self.resource_type}{self.resource_id}"
            else:
                resource = f"{self.resource_type}{self.sep}{self.resource_id}"
        else:
            resource = self.resource_id
        return f"arn:{self.partition}:{self.service}:{_handle_none(self.region)}:{_handle_none(self.account_id)}:{resource}"

    @property
    def aws_account_id(self) -> T.Optional[str]:
        return self.account_id

    @property
    def aws_region(self) -> T.Optional[str]:
        return self.region

    def with_us_gov_partition(self):
        self.partition = AwsPartitionEnum.aws_us_gov.value
        return self

    def with_cn_partition(self):
        self.partition = AwsPartitionEnum.aws_cn.value
        return self

    def to_console_url(self) -> str: # pragma: no cover
        """
        AWS console has a magic url that can be used to open a resource in the console.
        However, this is undocumented, and only support a few services.
        """
        if self.aws_region:
            return f"https://{self.aws_region}.console.{self.partition}.amazon.com/go/view?arn={self.to_arn()}"
        else:
            return f"https://console.{self.partition}.amazon.com/go/view?arn={self.to_arn()}"


def is_arn_instance(obj: T.Any) -> bool:
    """
    Identify if an object is an instance of Arn.
    """
    return isinstance(obj, BaseArn)


@dataclasses.dataclass
class Arn(BaseArn):
    """
    todo: docstring
    """
    @classmethod
    def new(
        cls,
        service: str,
        partition: str,
        region: T.Optional[str],
        account_id: T.Optional[str],
        resource_type: T.Optional[str],
        sep: T.Optional[str],
        resource_id: str,
    ):  # pragma: no cover
        """
        Factory method.
        """
        return cls(
            service=service,
            partition=partition,
            region=region,
            account_id=account_id,
            resource_type=resource_type,
            sep=sep,
            resource_id=resource_id,
        )


@dataclasses.dataclass
class _CrossAccountGlobal(BaseArn):
    """
    No account, no region. Example:

    - AWS S3
        - Bucket: arn:aws:s3:::my-bucket
            - ${partition}: aws
            - ${service}: s3
            - ${region}: None
            - ${account-id}: None
            - ${resource-type}: None
            - ${sep}: None
            - ${resource-id}: my-bucket
    """

    region: T.Optional[str] = dataclasses.field(default=None)
    account_id: T.Optional[str] = dataclasses.field(default=None)


@dataclasses.dataclass
class _Global(BaseArn):
    """
    No region. Example:

    - AWS IAM:
        - Role: arn:aws:iam::807388292768:role/acu_e5f245a1_test
            - ${partition}: aws
            - ${service}: iam
            - ${region}: None
            - ${account-id}: 807388292768
            - ${resource-type}: role
            - ${sep}: "/"
            - ${resource-id}: acu_e5f245a1_test
    - AWS Route53
    """

    region: T.Optional[str] = dataclasses.field(default=None)


@dataclasses.dataclass
class _Regional(BaseArn):
    """
    Normal regional resources. Example:

    - AWS SQS
    - AWS Lambda

    .. warning::

        Don't subclass this class directly, use one of those:

        - :class:`ResourceIdOnlyRegional`
        - :class:`ColonSeparatedRegional`
        - :class:`SlashSeparatedRegional`
    """


@dataclasses.dataclass
class _ResourceIdOnlyRegional(_Regional):
    """
    Only one resource type in this service. Example:

    - AWS SQS:
        - queue: arn:aws:sqs:us-east-1:807388292768:acu_e5f245a1_test
            - ${partition}: aws
            - ${service}: sqs
            - ${region}: us-east-1
            - ${account-id}: 807388292768
            - ${resource-type}: None
            - ${sep}: None
            - ${resource-id}: acu_e5f245a1_test
    - AWS SNS:
        - queue: arn:aws:sns:us-east-1:807388292768:acu_e5f245a1_test
            - ${partition}: aws
            - ${service}: sns
            - ${region}: us-east-1
            - ${account-id}: 807388292768
            - ${resource-type}: None
            - ${sep}: None
            - ${resource-id}: acu_e5f245a1_test
    """

    resource_type: T.Optional[str] = dataclasses.field(default=None)
    sep: T.Optional[str] = dataclasses.field(default=None)


@dataclasses.dataclass
class _ColonSeparatedRegional(_Regional):
    """
    Example:

    - AWS Lambda:
        - Function: arn:aws:lambda:us-east-1:807388292768:function:acu_e5f245a1_test
            - ${partition}: aws
            - ${service}: lambda
            - ${region}: us-east-1
            - ${account-id}: 807388292768
            - ${resource-type}: function
            - ${sep}: ":"
            - ${resource-id}: acu_e5f245a1_test
        - Version: arn:aws:lambda:us-east-1:807388292768:function:acu_e5f245a1_test:1
            - ${resource-id}: acu_e5f245a1_test:1
        - Alias: arn:aws:lambda:us-east-1:807388292768:function:acu_e5f245a1_test:LIVE
            - ${resource-id}: acu_e5f245a1_test:LIVE
    """

    sep: T.Optional[str] = dataclasses.field(default=":")


@dataclasses.dataclass
class _SlashSeparatedRegional(_Regional):
    """
    Example:

    - AWS CloudFormation
        - Stack: arn:aws:cloudformation:us-east-1:807388292768:stack/CDKToolkit/d8677750-1d2c-11ee-b9bb-0e26849ff9df
            - ${partition}: aws
            - ${service}: cloudformation
            - ${region}: us-east-1
            - ${account-id}: 807388292768
            - ${resource-type}: stack
            - ${sep}: "/"
            - ${resource-id}: CDKToolkit/d8677750-1d2c-11ee-b9bb-0e26849ff9df
        - StackSet: arn:aws:cloudformation:us-east-1:807388292768:stackset/acu-ab1049bd-test-self-managed:273c6018-4440-40c5-8869-89c3e4b17f84
            - ${resource-type}: stackset
            - ${resource-id}: acu-ab1049bd-test-self-managed:273c6018-4440-40c5-8869-89c3e4b17f84
    """

    sep: T.Optional[str] = dataclasses.field(default="/")
