# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import typing as T
import dataclasses

from ..model import _ColonSeparatedRegional


@dataclasses.dataclass
class StepFunction(_ColonSeparatedRegional):
    service: str = dataclasses.field(default="states")


@dataclasses.dataclass
class SfnStateMachine(StepFunction):
    """
    Example:

    - arn:aws:states:us-east-1:111122223333:stateMachine:standard_test
    - arn:aws:states:us-east-1:807388292768:stateMachine:standard_test:1
    - arn:aws:states:us-east-1:807388292768:stateMachine:standard_test:LIVE
    """

    resource_type: str = dataclasses.field(default="stateMachine")

    @property
    def name(self) -> str:
        return self.resource_id.split(":")[0]

    @property
    def version(self) -> T.Optional[str]:
        words = self.resource_id.split(":", 1)
        if len(words) == 2:
            token = words[1]
            if token.isdigit():
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
            if token.isdigit():
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
class _SfnStateMachineExecutionCommon(StepFunction):
    """
    Example:

    - arn:aws:states:us-east-1:111122223333:execution:standard_test:1d858cf6-613f-4576-b94f-e0d654c23843
    - arn:aws:states:us-east-1:111122223333:express:express_test:e935dec6-e748-4977-a2f2-32eeb83d81da:b2f7726e-9b98-4a49-a6c4-9cf23a61f180
    """

    @property
    def state_machine_name(self) -> str:
        return self.resource_id.split(":", 1)[0]

    @property
    def exec_id(self) -> str:
        return self.resource_id.split(":", 1)[1]

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        state_machine_name: str,
        exec_id: int,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=f"{state_machine_name}:{exec_id}",
        )

@dataclasses.dataclass
class SfnStandardStateMachineExecution(_SfnStateMachineExecutionCommon):
    """
    Example:

    - arn:aws:states:us-east-1:111122223333:execution:standard_test:1d858cf6-613f-4576-b94f-e0d654c23843
    """
    resource_type: str = dataclasses.field(default="execution")


@dataclasses.dataclass
class SfnExpressStateMachineExecution(_SfnStateMachineExecutionCommon):
    """
    Example:

    - arn:aws:states:us-east-1:111122223333:express:express_test:e935dec6-e748-4977-a2f2-32eeb83d81da:b2f7726e-9b98-4a49-a6c4-9cf23a61f180
    """
    resource_type: str = dataclasses.field(default="express")
