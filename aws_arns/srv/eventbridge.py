# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import dataclasses

from ..model import _SlashSeparatedRegional


@dataclasses.dataclass
class EventBridge(_SlashSeparatedRegional):
    service: str = dataclasses.field(default="events")


@dataclasses.dataclass
class _EventBridgeCommon(EventBridge):
    """
    todo: docstring
    """

    @property
    def name(self) -> str:
        return self.resource_id

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        resource_id: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=resource_id,
        )


@dataclasses.dataclass
class EventBridgeApiDestination(_EventBridgeCommon):
    """
    Example: arn:aws:events:us-east-1:111122223333:api-destination/my_api_destination
    """

    resource_type: str = dataclasses.field(default="api-destination")


@dataclasses.dataclass
class EventBridgeArchive(_EventBridgeCommon):
    """
    Example: arn:aws:events:us-east-1:111122223333:archive/my-archive
    """

    resource_type: str = dataclasses.field(default="archive")


@dataclasses.dataclass
class EventBridgeConnection(_EventBridgeCommon):
    """
    Example: arn:aws:events:us-east-1:111122223333:connection/my-connection
    """

    resource_type: str = dataclasses.field(default="connection")


@dataclasses.dataclass
class EventBridgeEndpoint(_EventBridgeCommon):
    """
    Example: arn:aws:events:us-east-1:111122223333:endpoint/my-endpoint
    """

    resource_type: str = dataclasses.field(default="endpoint")


@dataclasses.dataclass
class EventBridgeEventBus(_EventBridgeCommon):
    """
    Example: arn:aws:events:us-east-1:111122223333:event-bus/my-event-bus
    """

    resource_type: str = dataclasses.field(default="event-bus")


@dataclasses.dataclass
class EventBridgeeventSource(_EventBridgeCommon):
    """
    Example: arn:aws:events:us-east-1:111122223333:event-source/my-event-source
    """

    resource_type: str = dataclasses.field(default="event-source")


@dataclasses.dataclass
class EventBridgeReplay(_EventBridgeCommon):
    """
    Example: arn:aws:events:us-east-1:111122223333:replay/my-replay
    """

    resource_type: str = dataclasses.field(default="replay")


@dataclasses.dataclass
class EventBridgeRuleOnDefaultEventBus(_EventBridgeCommon):
    """
    Example: arn:aws:events:us-east-1:111122223333:rule/my-default-event-bus-rule
    """

    resource_type: str = dataclasses.field(default="rule")


@dataclasses.dataclass
class EventBridgeRuleOnCustomEventBus(EventBridge):
    """
    Example: arn:aws:events:us-east-1:111122223333:rule/my-event-bus/my-rule
    """

    resource_type: str = dataclasses.field(default="rule")

    @classmethod
    def new(
        cls, aws_account_id: str, aws_region: str, event_bus_name: str, rule_name: str
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=f"{event_bus_name}/{rule_name}",
        )

    @property
    def event_bus_name(self) -> str:
        return self.resource_id.split("/")[0]

    @property
    def rule_name(self) -> str:
        return self.resource_id.split("/")[1]
