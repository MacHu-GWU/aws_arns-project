# -*- coding: utf-8 -*-

from aws_arns.srv.opensearch import (
    OpenSearchDomain,
    OpenSearchServerlessCollection,
    OpenSearchServerlessDashboard,
)


def test():
    oss_domain_arn = "arn:aws:es:us-east-1:111122223333:domain/my_domain"
    oss_sls_collection_arn = (
        "arn:aws:aoss:us-east-1:111122223333:collection/collection_id"
    )
    oss_sls_dashboard_arn = "arn:aws:aoss:us-east-1:111122223333:dashboards/default"

    oss_domain = OpenSearchDomain.from_arn(oss_domain_arn)
    oss_sls_collection = OpenSearchServerlessCollection.from_arn(oss_sls_collection_arn)
    oss_sls_dashboard = OpenSearchServerlessDashboard.from_arn(oss_sls_dashboard_arn)

    assert oss_domain.to_arn() == oss_domain_arn
    assert oss_sls_collection.to_arn() == oss_sls_collection_arn
    assert oss_sls_dashboard.to_arn() == oss_sls_dashboard_arn

    assert oss_domain.domain_name == "my_domain"
    assert oss_sls_collection.collection_id == "collection_id"

    assert OpenSearchDomain.new(
        oss_domain.account_id,
        oss_domain.region,
        oss_domain.domain_name,
    ) == oss_domain

    assert OpenSearchServerlessCollection.new(
        oss_sls_collection.account_id,
        oss_sls_collection.region,
        oss_sls_collection.collection_id,
    ) == oss_sls_collection

    assert OpenSearchServerlessDashboard.new(
        oss_sls_dashboard.account_id,
        oss_sls_dashboard.region,
    ) == oss_sls_dashboard


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.srv.opensearch", preview=False)
