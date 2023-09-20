# -*- coding: utf-8 -*-

import enum


class AwsPartitionEnum(str, enum.Enum):
    aws = "aws"
    aws_cn = "aws-cn"
    aws_us_gov = "aws-us-gov"
