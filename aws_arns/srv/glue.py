# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import dataclasses

from ..model import _SlashSeparatedRegional


@dataclasses.dataclass
class Glue(_SlashSeparatedRegional):
    """
    todo: docstring
    """
    service: str = dataclasses.field(default="glue")


@dataclasses.dataclass
class _GlueCommon(Glue):
    """
    todo: docstring
    """

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        name: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=name,
        )


@dataclasses.dataclass
class GlueDatabase(Glue):
    """
    Example: arn:aws:glue:us-east-1:111122223333:database/db1
    """
    resource_type: str = dataclasses.field(default="database")

    @property
    def database_name(self) -> str:  # pragma: no cover
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        database_name: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=database_name,
        )


@dataclasses.dataclass
class GlueTable(Glue):
    """
    Example: arn:aws:glue:us-east-1:111122223333:table/db1/tbl
    """
    resource_type: str = dataclasses.field(default="table")

    @property
    def database_name(self) -> str:  # pragma: no cover
        return self.resource_id.split("/")[0]

    @property
    def table_name(self) -> str:  # pragma: no cover
        return self.resource_id.split("/")[1]

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        database_name: str,
        table_name: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=f"{database_name}/{table_name}",
        )


@dataclasses.dataclass
class GlueCrawler(_GlueCommon):
    """
    Example: arn:aws:glue:us-east-1:111122223333:crawler/mycrawler
    """
    resource_type: str = dataclasses.field(default="crawler")

    @property
    def crawler_name(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class GlueJob(_GlueCommon):
    """
    Example: arn:aws:glue:us-east-1:111122223333:job/testjob
    """
    resource_type: str = dataclasses.field(default="job")

    @property
    def job_name(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class GlueTrigger(_GlueCommon):
    """
    Example: arn:aws:glue:us-east-1:111122223333:trigger/sampletrigger
    """
    resource_type: str = dataclasses.field(default="trigger")

    @property
    def trigger_name(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class GlueMLTransform(_GlueCommon):
    """
    Example: arn:aws:glue:us-east-1:111122223333:mlTransform/tfm-1234567890
    """
    resource_type: str = dataclasses.field(default="mlTransform")

    @property
    def ml_transform_name(self) -> str:  # pragma: no cover
        return self.resource_id
