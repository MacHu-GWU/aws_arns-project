# -*- coding: utf-8 -*-

import dataclasses

from ..model import SlashSeparatedRegional


@dataclasses.dataclass
class A2I(SlashSeparatedRegional):
    @property
    def name(self) -> str:
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        name: str,
        resource_type: str,
    ):
        return super(A2I, cls).new(
            partition="aws",
            service="sagemaker",
            region=aws_region,
            account_id=aws_account_id,
            resource_id=name,
            resource_type=resource_type,
        )


@dataclasses.dataclass
class A2IHumanReviewWorkflow(A2I):
    @property
    def a2i_human_review_workflow_name(self) -> str:
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        name: str,
    ):
        return super(A2IHumanReviewWorkflow, cls).new(
            aws_region=aws_region,
            aws_account_id=aws_account_id,
            name=name,
            resource_type="flow-definition",
        )


@dataclasses.dataclass
class A2IHumanLoop(A2I):
    @property
    def a2i_human_loop_name(self) -> str:
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        name: str,
    ):
        return super(A2IHumanLoop, cls).new(
            aws_region=aws_region,
            aws_account_id=aws_account_id,
            name=name,
            resource_type="human-loop",
        )


@dataclasses.dataclass
class A2IWorkerTaskTemplate(A2I):
    @property
    def a2i_worker_task_template_name(self) -> str:
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        name: str,
    ):
        return super(A2IWorkerTaskTemplate, cls).new(
            aws_region=aws_region,
            aws_account_id=aws_account_id,
            name=name,
            resource_type="human-task-ui",
        )
