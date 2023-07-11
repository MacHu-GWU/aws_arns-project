# -*- coding: utf-8 -*-

import typing as T
import dataclasses

from ..model import CrossAccountGlobal


@dataclasses.dataclass
class S3(CrossAccountGlobal):
    @classmethod
    def new(
        cls,
        resource_id: str,
        resource_type: T.Optional[str] = None,
        sep: T.Optional[str] = None,
    ):
        return super(S3, cls).new(
            service="s3",
            resource_id=resource_id,
            partition="aws",
            resource_type=resource_type,
            sep=sep,
        )


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
        return super(S3Bucket, cls).new(
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
        return self.resource_type

    @property
    def key(self) -> str:
        return self.resource_id

    @property
    def uri(self) -> str:
        return f"s3://{self.bucket}/{self.key}"

    @classmethod
    def new(cls, bucket: str, key: str):
        return super(S3Object, cls).new(
            resource_id=key,
            resource_type=bucket,
            sep="/",
        )

    @classmethod
    def from_uri(cls, uri: str):
        parts = uri.split("/", 3)
        return cls.new(bucket=parts[2], key=parts[3])
