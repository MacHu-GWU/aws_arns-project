# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import typing as T
import dataclasses

from ..model import _ColonSeparatedRegional


@dataclasses.dataclass
class AwsLambda(_ColonSeparatedRegional):
    service: str = dataclasses.field(default="lambda")


@dataclasses.dataclass
class LambdaFunction(AwsLambda):
    """
    Example:

    - arn:aws:lambda:us-east-1:111122223333:function:my-func
    - arn:aws:lambda:us-east-1:111122223333:function:my-func:LIVE
    - arn:aws:lambda:us-east-1:111122223333:function:my-func:1
    """

    resource_type: str = dataclasses.field(default="function")

    @property
    def name(self) -> str:
        return self.resource_id.split(":", 1)[0]

    @property
    def function_name(self) -> str:
        return self.name

    @property
    def version(self) -> T.Optional[str]:
        words = self.resource_id.split(":", 1)
        if len(words) == 2:
            token = words[1]
            if token == "$LATEST":  # pragma: no cover
                return token
            elif token.isdigit():
                return token
            else:
                raise ValueError(f"Invalid version: {token}")
        else:
            return None

    @property
    def alias(self) -> T.Optional[str]:
        words = self.resource_id.split(":", 1)
        if len(words) == 2:
            token = words[1]
            if token == "$LATEST":  # pragma: no cover
                raise ValueError("Cannot specify alias for $LATEST")
            elif token.isdigit():
                raise ValueError(f"Invalid version: {token}")
            else:
                return token
        else:
            return None

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        name: str,
        version: T.Optional[T.Union[str, int]] = None,
        alias: T.Optional[str] = None,
    ):
        """
        Factory method.
        """
        if version is not None and alias is not None:  # pragma: no cover
            raise ValueError("Cannot specify both version and alias")

        if version is not None:
            resource_id = f"{name}:{version}"
        elif alias is not None:
            resource_id = f"{name}:{alias}"
        else:
            resource_id = name

        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=resource_id,
        )


@dataclasses.dataclass
class LambdaLayer(AwsLambda):
    """
    Example: arn:aws:lambda:us-east-1:111122223333:layer:my-layer:1
    """

    resource_type: str = dataclasses.field(default="layer")

    @property
    def name(self) -> str:
        return self.resource_id.split(":", 1)[0]

    @property
    def layer_name(self) -> str:
        return self.name

    @property
    def version(self) -> int:
        return int(self.resource_id.split(":", 1)[1])

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        name: str,
        version: int,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=f"{name}:{version}",
        )
