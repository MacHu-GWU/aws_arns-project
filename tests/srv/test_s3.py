# -*- coding: utf-8 -*-

from aws_arns.srv.s3 import (
    S3Bucket,
    S3Object,
)


def test():
    arn = "arn:aws:s3:::my-bucket"
    bucket = S3Bucket.from_arn(arn)
    assert bucket.bucket_name == "my-bucket"
    assert S3Bucket.new(bucket_name=bucket.bucket_name) == bucket

    uri = "s3://my-bucket"
    assert bucket.uri == uri
    assert S3Bucket.from_uri(uri) == bucket

    arn = "arn:aws:s3:::my-bucket/folder/file.txt"
    object = S3Object.from_arn(arn)
    assert object.bucket == "my-bucket"
    assert object.key == "folder/file.txt"
    assert S3Object.new(bucket=object.bucket, key=object.key) == object
    uri = "s3://my-bucket/folder/file.txt"
    assert object.uri == uri
    assert S3Object.from_uri(uri) == object


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.srv.s3", preview=False)
