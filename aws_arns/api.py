# -*- coding: utf-8 -*-

"""
Usage example::

    import aws_arns.api as aws_arns
"""

from .constants import AwsPartitionEnum
from .model import BaseArn
from .model import Arn
from .model import is_arn_instance
from . import resource as res
from .parse_arn import parse_arn
