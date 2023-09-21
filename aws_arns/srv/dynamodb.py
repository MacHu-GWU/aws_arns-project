# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import dataclasses

from ..model import _SlashSeparatedRegional


@dataclasses.dataclass
class Dynamodb(_SlashSeparatedRegional):
    service: str = dataclasses.field(default="dynamodb")


@dataclasses.dataclass
class DynamodbTable(Dynamodb):
    """
    Example: arn:aws:dynamodb:us-east-1:111122223333:table/my_table
    """

    resource_type: str = dataclasses.field(default="table")

    @property
    def table_name(self) -> str:
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        table_name: str,
    ):
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=table_name,
        )


@dataclasses.dataclass
class DynamodbGlobalTable(Dynamodb):
    """
    Example: arn:aws:dynamodb::111122223333:global-table/my_global_table_name
    """

    region: str = dataclasses.field(default=None)
    resource_type: str = dataclasses.field(default="global-table")

    @property
    def table_name(self) -> str:
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        table_name: str,
    ):
        return cls(
            account_id=aws_account_id,
            resource_id=table_name,
        )


@dataclasses.dataclass
class _DynamodbTableCommon(Dynamodb):
    """
    todo: docstring
    """

    resource_type: str = dataclasses.field(default="table")

    @property
    def table_name(self) -> str:
        return self.resource_id.split("/")[0]

    @property
    def table_resource_type(self) -> str:
        return self.resource_id.split("/")[1]

    @property
    def table_resource_name(self) -> str:
        return "/".join(self.resource_id.split("/")[2:])

    @classmethod
    def _new(
        cls,
        aws_account_id: str,
        aws_region: str,
        table_name: str,
        resource_type: str,
        resource_name: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=f"{table_name}/{resource_type}/{resource_name}",
        )


@dataclasses.dataclass
class DynamodbTableIndex(_DynamodbTableCommon):
    """
    Example: arn:aws:dynamodb:us-east-1:111122223333:table/my_table/index/my_index
    """

    @property
    def index_name(self) -> str:  # pragma: no cover
        return self.table_resource_name

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        table_name: str,
        index_name: str,
    ):  # pragma: no cover
        return cls._new(
            aws_account_id=aws_account_id,
            aws_region=aws_region,
            table_name=table_name,
            resource_type="index",
            resource_name=index_name,
        )


@dataclasses.dataclass
class DynamodbTableStream(_DynamodbTableCommon):
    """
    Example: arn:aws:dynamodb:us-east-1:111122223333:table/my_table/stream/my_stream_label
    """

    @property
    def stream_name(self) -> str:  # pragma: no cover
        return self.table_resource_name

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        table_name: str,
        stream_name: str,
    ):  # pragma: no cover
        return cls._new(
            aws_account_id=aws_account_id,
            aws_region=aws_region,
            table_name=table_name,
            resource_type="stream",
            resource_name=stream_name,
        )


@dataclasses.dataclass
class DynamodbTableBackup(_DynamodbTableCommon):
    """
    Example: arn:aws:dynamodb:us-east-1:111122223333:table/my_table/backup/my_backup_name
    """

    @property
    def backup_name(self) -> str:  # pragma: no cover
        return self.table_resource_name

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        table_name: str,
        resource_name: str,
    ):  # pragma: no cover
        return cls._new(
            aws_account_id=aws_account_id,
            aws_region=aws_region,
            table_name=table_name,
            resource_type="backup",
            resource_name=resource_name,
        )


@dataclasses.dataclass
class DynamodbTableExport(_DynamodbTableCommon):
    """
    Example: arn:aws:dynamodb:us-east-1:111122223333:table/my_table/export/my_export_name
    """

    @property
    def export_name(self) -> str:  # pragma: no cover
        return self.table_resource_name

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        table_name: str,
        export_name: str,
    ):  # pragma: no cover
        return cls._new(
            aws_account_id=aws_account_id,
            aws_region=aws_region,
            table_name=table_name,
            resource_type="export",
            resource_name=export_name,
        )


@dataclasses.dataclass
class DynamodbTableImport(_DynamodbTableCommon):
    """
    Example: arn:aws:dynamodb:us-east-1:111122223333:table/my_table/import/my_import_name
    """

    @property
    def import_name(self) -> str:  # pragma: no cover
        return self.table_resource_name

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        table_name: str,
        import_name: str,
    ):  # pragma: no cover
        return cls._new(
            aws_account_id=aws_account_id,
            aws_region=aws_region,
            table_name=table_name,
            resource_type="import",
            resource_name=import_name,
        )
