# -*- coding: utf-8 -*-

"""
.. note::

    Let's use this as an example to show how to create a module for specific AWS services.

    First, you need to create an aws service class that the name is the service,
    and the base class is one of the following:

    - CrossAccountGlobal
    - Global
    - Regional
    - ResourceIdOnlyRegional
    - ColonSeparatedRegional
    - SlashSeparatedRegional

    Then all aws resources in this service should be a class that inherits from
    the service class.
"""

import typing as T
import dataclasses

from ..model import _CrossAccountGlobal


@dataclasses.dataclass
class S3(_CrossAccountGlobal):
    service: str = dataclasses.field(default="s3")
    resource_type: str = dataclasses.field(default=None)
    sep: str = dataclasses.field(default=None)


@dataclasses.dataclass
class S3Bucket(S3):
    """
    Example: arn:aws:s3:::my-bucket
    """
    @property
    def bucket_name(self) -> str:
        return self.resource_id

    @property
    def uri(self) -> str:
        return f"s3://{self.bucket_name}"

    @classmethod
    def new(
        cls,
        bucket_name: str,
    ):
        return cls(
            resource_id=bucket_name,
        )

    @classmethod
    def from_uri(cls, uri: str):
        return cls.new(uri.split("/")[2])


@dataclasses.dataclass
class S3Object(S3):
    """
    Example: arn:aws:s3:::my-bucket/folder/file.txt
    """
    @property
    def bucket(self) -> str:
        return self.resource_id.split("/", 1)[0]

    @property
    def key(self) -> str:
        return self.resource_id.split("/", 1)[1]

    @property
    def uri(self) -> str:
        return f"s3://{self.bucket}/{self.key}"

    @classmethod
    def new(cls, bucket: str, key: str):
        return cls(
            resource_id=f"{bucket}/{key}",
        )

    @classmethod
    def from_uri(cls, uri: str):
        parts = uri.split("/", 3)
        return cls.new(bucket=parts[2], key=parts[3])
