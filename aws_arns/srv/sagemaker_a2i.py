# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import dataclasses

from ..model import _SlashSeparatedRegional


@dataclasses.dataclass
class A2I(_SlashSeparatedRegional):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:flow-definition/my-flow
    """

    service: str = dataclasses.field(default="sagemaker")

    @property
    def name(self) -> str:
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


@dataclasses.dataclass
class A2IHumanReviewWorkflow(A2I):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:flow-definition/my_flow
    """

    resource_type: str = dataclasses.field(default="flow-definition")

    @property
    def a2i_human_review_workflow_name(self) -> str:
        return self.resource_id


@dataclasses.dataclass
class A2IHumanLoop(A2I):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:human-loop/1a2b3c
    """

    resource_type: str = dataclasses.field(default="human-loop")

    @property
    def a2i_human_loop_name(self) -> str:
        return self.resource_id


@dataclasses.dataclass
class A2IWorkerTaskTemplate(A2I):
    """
    Example: arn:aws:sagemaker:us-east-1:111122223333:human-task-ui/my-ui
    """

    resource_type: str = dataclasses.field(default="human-task-ui")

    @property
    def a2i_worker_task_template_name(self) -> str:
        return self.resource_id
