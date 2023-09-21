# -*- coding: utf-8 -*-

from aws_arns.srv.dynamodb import (
    DynamodbTable,
    DynamodbGlobalTable,
    _DynamodbTableCommon,
    DynamodbTableIndex,
    DynamodbTableStream,
    DynamodbTableBackup,
    DynamodbTableExport,
    DynamodbTableImport,
)


def test():
    arn_table = "arn:aws:dynamodb:us-east-1:111122223333:table/my_table"
    arn_global_table = (
        "arn:aws:dynamodb::111122223333:global-table/my_global_table_name"
    )
    arn_table_index = (
        "arn:aws:dynamodb:us-east-1:111122223333:table/my_table/index/my_index"
    )
    arn_table_stream = (
        "arn:aws:dynamodb:us-east-1:111122223333:table/my_table/stream/my_stream_label"
    )
    arn_table_backup = (
        "arn:aws:dynamodb:us-east-1:111122223333:table/my_table/backup/my_backup_name"
    )
    arn_table_export = (
        "arn:aws:dynamodb:us-east-1:111122223333:table/my_table/export/my_export_name"
    )
    arn_table_import = (
        "arn:aws:dynamodb:us-east-1:111122223333:table/my_table/import/my_import_name"
    )

    table = DynamodbTable.from_arn(arn_table)
    assert (
        DynamodbTable.new(
            aws_region=table.region,
            aws_account_id=table.account_id,
            table_name=table.table_name,
        )
        == table
    )

    global_table = DynamodbGlobalTable.from_arn(arn_global_table)
    assert global_table.aws_region is None
    assert (
        DynamodbGlobalTable.new(
            aws_account_id=global_table.account_id,
            table_name=global_table.table_name,
        )
        == global_table
    )

    class_and_arn_pairs = [
        (DynamodbTable, arn_table),
        (DynamodbGlobalTable, arn_global_table),
        (DynamodbTableIndex, arn_table_index),
        (DynamodbTableStream, arn_table_stream),
        (DynamodbTableBackup, arn_table_backup),
        (DynamodbTableExport, arn_table_export),
        (DynamodbTableImport, arn_table_import),
    ]
    for class_, arn in class_and_arn_pairs:
        obj: DynamodbTable = class_.from_arn(arn)
        assert obj.to_arn() == arn

    class_and_arn_pairs = [
        (DynamodbTableIndex, arn_table_index),
        (DynamodbTableStream, arn_table_stream),
        (DynamodbTableBackup, arn_table_backup),
        (DynamodbTableExport, arn_table_export),
        (DynamodbTableImport, arn_table_import),
    ]
    for class_, arn in class_and_arn_pairs:
        obj: _DynamodbTableCommon = class_.from_arn(arn)
        assert obj.table_resource_type in obj.resource_id
        assert (
            class_.new(
                obj.aws_account_id,
                obj.aws_region,
                obj.table_name,
                obj.table_resource_name,
            )
            == obj
        )


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.srv.dynamodb", preview=False)
