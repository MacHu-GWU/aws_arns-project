# -*- coding: utf-8 -*-


def test():
    from aws_arns import api

    _ = api.Arn
    _ = api.AwsPartitionEnum
    {%- for resource in resource_list %}
    _ = api.res.{{ resource.class_name }}
    {%- endfor %}


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.api", preview=False)
