# -*- coding: utf-8 -*-

from aws_arns.srv.glue import (
    _GlueCommon,
    GlueDatabase,
    GlueTable,
    GlueCrawler,
    GlueJob,
    GlueTrigger,
    GlueMLTransform,
)


def test():
    arn_database = "arn:aws:glue:us-east-1:111122223333:database/db1"
    arn_table = "arn:aws:glue:us-east-1:111122223333:table/db1/tb1"
    arn_crawler = "arn:aws:glue:us-east-1:111122223333:crawler/mycrawler"
    arn_job = "arn:aws:glue:us-east-1:111122223333:job/testjob"
    arn_trigger = "arn:aws:glue:us-east-1:111122223333:trigger/sampletrigger"
    arn_ml_transform = "arn:aws:glue:us-east-1:111122223333:mlTransform/tfm-1234567890"

    database = GlueDatabase.from_arn(arn_database)
    assert database.database_name == "db1"
    assert (
        GlueDatabase.new(
            aws_region=database.region,
            aws_account_id=database.account_id,
            database_name=database.database_name,
        )
        == database
    )

    table = GlueTable.from_arn(arn_table)
    assert table.database_name == "db1"
    assert table.table_name == "tb1"
    assert (
        GlueTable.new(
            aws_region=table.region,
            aws_account_id=table.account_id,
            database_name=table.database_name,
            table_name=table.table_name,
        )
        == table
    )

    class_and_arn_pairs = [
        (GlueCrawler, arn_crawler),
        (GlueJob, arn_job),
        (GlueTrigger, arn_trigger),
        (GlueMLTransform, arn_ml_transform),
    ]
    for class_, arn in class_and_arn_pairs:
        obj: _GlueCommon = class_.from_arn(arn)
        assert obj.to_arn() == arn
        assert (
            class_.new(
                aws_account_id=obj.aws_account_id,
                aws_region=obj.aws_region,
                name=obj.resource_id,
            )
            == obj
        )


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.srv.glue", preview=False)
