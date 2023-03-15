# -*- coding: utf-8 -*-

import typing as T
import dataclasses

from . import compat


def _handle_empty_str(s: str) -> T.Optional[str]:
    if s:
        return s
    else:
        return None


def _handle_none(s: T.Optional[str]) -> str:
    if s is None:
        return ""
    else:
        return s


@dataclasses.dataclass
class Arn:
    """
    Amazon Resource Names (ARNs) data model. is a unique identifier for AWS resources.

    Reference:

    - Amazon Resource Names (ARNs): https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html
    """
    partition: str = dataclasses.field()
    service: str = dataclasses.field()
    region: str = dataclasses.field()
    account_id: str = dataclasses.field()
    resource_id: str = dataclasses.field()
    resource_type: T.Optional[str] = dataclasses.field(default=None)
    sep: T.Optional[str] = dataclasses.field(default=None)

    @classmethod
    def from_arn(cls, arn: str) -> "Arn":
        """
        parse arn string into Arn object.
        """
        if not arn.startswith("arn:"):
            raise ValueError(f"Invalid ARN: {arn!r}")

        _, partition, service, region, account_id, resource = arn.split(":", 5)

        if "/" in resource:
            sep = "/"
            resource_type, resource_id = resource.split("/", 1)
        elif ":" in resource:
            sep = ":"
            resource_type, resource_id = resource.split(":", 1)
        else:
            sep = None
            resource_type, resource_id = None, resource

        return cls(
            partition=partition,
            service=service,
            region=_handle_empty_str(region),
            account_id=_handle_empty_str(account_id),
            resource_id=resource_id,
            resource_type=resource_type,
            sep=sep,
        )

    def to_arn(self) -> str:
        """
        convert Arn object into arn string.
        """
        if self.sep:
            resource = f"{self.resource_type}{self.sep}{self.resource_id}"
        else:
            resource = self.resource_id
        return f"arn:{self.partition}:{self.service}:{_handle_none(self.region)}:{_handle_none(self.account_id)}:{resource}"
