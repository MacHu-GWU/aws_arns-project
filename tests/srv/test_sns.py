# -*- coding: utf-8 -*-

from aws_arns.srv.sns import (
    SnsTopic,
    SnsSubscription,
)


def test():
    arn = "arn:aws:sns:us-east-1:111122223333:my_topic"
    topic = SnsTopic.from_arn(arn)
    assert topic.topic_name == "my_topic"
    assert (
        SnsTopic.new(
            aws_account_id=topic.aws_account_id,
            aws_region=topic.aws_region,
            topic_name=topic.topic_name,
        )
        == topic
    )

    arn = "arn:aws:sns:us-east-1:111122223333:my_topic:a07e1034-10c0-47a6-83c2-552cfcca42db"
    sub = SnsSubscription.from_arn(arn)
    assert sub.topic_name == "my_topic"
    assert sub.subscription_id == "a07e1034-10c0-47a6-83c2-552cfcca42db"
    assert (
        SnsSubscription.new(
            aws_account_id=sub.aws_account_id,
            aws_region=sub.aws_region,
            topic_name=sub.topic_name,
            subscription_id=sub.subscription_id,
        )
        == sub
    )


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.srv.sns", preview=False)
