# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import typing as T
import dataclasses

from ..model import _ColonSeparatedRegional


@dataclasses.dataclass
class AWSLambda(_ColonSeparatedRegional):
    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        resource_id: str,
        resource_type: str,
    ):
        return super(AWSLambda, cls).new(
            partition="aws",
            service="batch",
            region=aws_region,
            account_id=aws_account_id,
            resource_id=name,
            resource_type=resource_type,
        )


# @dataclasses.dataclass
# class LambdaFunction(AWSLambda):
#     """
#     Example: arn:aws:lambda:us-east-1:111122223333:function:my_func
#     """
#
#     @property
#     def function_name(self) -> str:
#         return self.resource_id
#
#     @classmethod
#     def new(
#         cls,
#         bucket_name: str,
#     ):
#         return super(S3Bucket, cls).new(
#             resource_id=bucket_name,
#         )rn cls.new(uri.split("/")[2])
