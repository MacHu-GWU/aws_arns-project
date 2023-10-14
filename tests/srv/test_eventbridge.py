# -*- coding: utf-8 -*-

from aws_arns.srv.eventbridge import (
    _EventBridgeCommon,
    EventBridgeApiDestination,
    EventBridgeArchive,
    EventBridgeConnection,
    EventBridgeEndpoint,
    EventBridgeEventBus,
    EventBridgeEventSource,
    EventBridgeReplay,
    EventBridgeRuleOnDefaultEventBus,
    EventBridgeRuleOnCustomEventBus,
)


def test():
    class_and_arn_pairs = [
        (
            EventBridgeApiDestination,
            "arn:aws:events:us-east-1:111122223333:api-destination/my_api_destination",
        ),
        (
            EventBridgeArchive,
            "arn:aws:events:us-east-1:111122223333:archive/my-archive",
        ),
        (
            EventBridgeConnection,
            "arn:aws:events:us-east-1:111122223333:connection/my-connection",
        ),
        (
            EventBridgeEndpoint,
            "arn:aws:events:us-east-1:111122223333:endpoint/my-endpoint",
        ),
        (
            EventBridgeEventBus,
            "arn:aws:events:us-east-1:111122223333:event-bus/my-event-bus",
        ),
        (
            EventBridgeEventSource,
            "arn:aws:events:us-east-1:111122223333:event-source/my-event-source",
        ),
        (EventBridgeReplay, "arn:aws:events:us-east-1:111122223333:replay/my-replay"),
        (
            EventBridgeRuleOnDefaultEventBus,
            "arn:aws:events:us-east-1:111122223333:rule/my-default-event-bus-rule",
        ),
    ]
    for class_, arn in class_and_arn_pairs:
        obj: _EventBridgeCommon = class_.from_arn(arn)
        assert obj.to_arn() == arn
        assert (
            class_.new(
                aws_account_id=obj.aws_account_id,
                aws_region=obj.aws_region,
                resource_id=obj.resource_id,
            )
            == obj
        )
        assert obj.name == obj.resource_id

    arn = "arn:aws:events:us-east-1:111122223333:rule/my-event-bus/my-rule"
    obj: EventBridgeRuleOnCustomEventBus = EventBridgeRuleOnCustomEventBus.from_arn(arn)
    assert obj.event_bus_name == "my-event-bus"
    assert obj.rule_name == "my-rule"
    assert (
        EventBridgeRuleOnCustomEventBus.new(
            aws_account_id=obj.aws_account_id,
            aws_region=obj.aws_region,
            event_bus_name=obj.event_bus_name,
            rule_name=obj.rule_name,
        )
        == obj
    )


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.srv.eventbridge", preview=False)
