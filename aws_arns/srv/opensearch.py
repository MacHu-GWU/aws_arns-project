# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import dataclasses

from ..model import _SlashSeparatedRegional


@dataclasses.dataclass
class OpenSearch(_SlashSeparatedRegional):
    service: str = dataclasses.field(default="es")


@dataclasses.dataclass
class OpenSearchServerless(_SlashSeparatedRegional):
    service: str = dataclasses.field(default="aoss")


@dataclasses.dataclass
class OpenSearchIngestionService(_SlashSeparatedRegional):
    service: str = dataclasses.field(default="osis")


@dataclasses.dataclass
class OpenSearchDomain(OpenSearch):
    """
    Example: arn:aws:es:us-east-1:111122223333:domain/my_domain
    """

    resource_type: str = dataclasses.field(default="domain")

    @property
    def domain_name(self) -> str:
        """
        "my_domain" part of
        arn:aws:es:us-east-1:111122223333:domain/my_domain
        """
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        domain_name: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=domain_name,
        )


@dataclasses.dataclass
class OpenSearchServerlessCollection(OpenSearchServerless):
    """
    Example: arn:aws:es:us-east-1:111122223333:domain/my_domain
    """

    resource_type: str = dataclasses.field(default="collection")

    @property
    def collection_id(self) -> str:
        """
        "collection_id" part of
        arn:aws:aoss:us-east-1:111122223333:collection/collection_id
        """
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        collection_id: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=collection_id,
        )


@dataclasses.dataclass
class OpenSearchServerlessDashboard(OpenSearchServerless):
    """
    Example: arn:aws:aoss:us-east-1:111122223333:dashboards/default
    """

    resource_type: str = dataclasses.field(default="dashboards")

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id="default",
        )


@dataclasses.dataclass
class OpenSearchServerlessCollection(OpenSearchServerless):
    """
    Example: arn:aws:es:us-east-1:111122223333:domain/my_domain
    """

    resource_type: str = dataclasses.field(default="collection")

    @property
    def collection_id(self) -> str:
        """
        "collection_id" part of
        arn:aws:aoss:us-east-1:111122223333:collection/collection_id
        """
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        collection_id: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=collection_id,
        )


@dataclasses.dataclass
class OpenSearchIngestionPipeline(OpenSearchIngestionService):
    """
    Example: arn:aws:osis:us-east-1:111122223333:pipeline/my_pipeline
    """

    resource_type: str = dataclasses.field(default="pipeline")

    @property
    def pipeline_name(self) -> str:
        """
        "pipeline name" part of
        arn:aws:osis:us-east-1:111122223333:pipeline/my_pipeline
        """
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        pipeline_name: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=pipeline_name,
        )


@dataclasses.dataclass
class OpenSearchIngestionPipelineBlueprint(OpenSearchIngestionService):
    """
    Example: arn:aws:osis:us-east-1:111122223333:blueprint/blueprint_name
    """

    resource_type: str = dataclasses.field(default="blueprint")

    @property
    def blueprint_name(self) -> str:
        """
        "pipeline name" part of
        arn:aws:osis:us-east-1:111122223333:blueprint/blueprint_name
        """
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        blueprint_name: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=blueprint_name,
        )
