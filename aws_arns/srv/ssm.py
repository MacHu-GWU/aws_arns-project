# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import dataclasses

from ..model import _SlashSeparatedRegional


@dataclasses.dataclass
class SystemManager(_SlashSeparatedRegional):
    service: str = dataclasses.field(default="ssm")


@dataclasses.dataclass
class SSMParameter(SystemManager):
    """
    Example: arn:aws:ssm:us-east-1:807388292768:parameter/acu_e5f245a1_test
    """
    resource_type: str = dataclasses.field(default="parameter")

    @property
    def parameter_name(self) -> str:
        """
        It is the stack ARN.
        """
        return self.resource_id

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
