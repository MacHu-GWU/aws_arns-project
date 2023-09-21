# -*- coding: utf-8 -*-

from aws_arns.srv.sqs import (
    SqsQueue,
)


def test():
    arn = "arn:aws:sqs:us-east-1:111122223333:my_queue"
    queue = SqsQueue.from_arn(arn)
    assert queue.queue_name == "my_queue"
    assert (
        SqsQueue.new(
            aws_account_id=queue.aws_account_id,
            aws_region=queue.aws_region,
            queue_name=queue.queue_name,
        )
        == queue
    )
    assert queue == SqsQueue.from_queue_url(queue.queue_url)

    url = "https://sqs.us-east-1.amazonaws.com/111122223333/my_queue.fifo"
    queue = SqsQueue.from_queue_url(url)
    assert queue.queue_name == "my_queue.fifo"
    assert (
        SqsQueue.new(
            aws_account_id=queue.aws_account_id,
            aws_region=queue.aws_region,
            queue_name=queue.queue_name,
        )
        == queue
    )


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.srv.sqs", preview=False)
