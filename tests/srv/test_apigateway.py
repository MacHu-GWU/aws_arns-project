# -*- coding: utf-8 -*-

from aws_arns.srv.apigateway import (
    ApiGatewayV1RestApi,
    ApiGatewayV1Stage,
    ApiGatewayV1Deployment,
    ApiGatewayV1Authorizer,
    ApiGatewayV1Model,
    ApiGatewayV1Route,
    ApiGatewayV1Integration,
    ApiGatewayV2Api,
    ApiGatewayV2Stage,
    ApiGatewayV2Deployment,
    ApiGatewayV2Authorizer,
    ApiGatewayV2Model,
    ApiGatewayV2Route,
    ApiGatewayV2Integration,
)


def test():
    for class_, arn, api_gateway_version, api_id, api_res_type, api_res_path in [
        (ApiGatewayV1Stage, "arn:aws:apigateway:us-east-1::/restapis/my_rest_api/stages/my_stage/path/to/resource", 1, "my_rest_api", "stages", "/my_stage/path/to/resource"),
        (ApiGatewayV1Deployment, "arn:aws:apigateway:us-east-1::/restapis/my_rest_api/deployments/my_deployment", 1, "my_rest_api", "deployments", "/my_deployment"),
        (ApiGatewayV1Authorizer, "arn:aws:apigateway:us-east-1::/restapis/my_rest_api/authorizers/my_authorizer", 1, "my_rest_api", "authorizers", "/my_authorizer"),
        (ApiGatewayV1Model, "arn:aws:apigateway:us-east-1::/restapis/my_rest_api/models/my_model", 1, "my_rest_api", "models", "/my_model"),
        (ApiGatewayV1Route, "arn:aws:apigateway:us-east-1::/restapis/my_rest_api/routes/my_route", 1, "my_rest_api", "routes", "/my_route"),
        (ApiGatewayV1Integration, "arn:aws:apigateway:us-east-1::/restapis/my_rest_api/integrations/my_integration", 1, "my_rest_api", "integrations", "/my_integration"),
        (ApiGatewayV1RestApi, "arn:aws:apigateway:us-east-1::/restapis/my_rest_api", 1, "my_rest_api", None, None),
        (ApiGatewayV2Stage, "arn:aws:apigateway:us-east-1::/apis/my_api/stages/my_stage/path/to/resource", 2, "my_api", "stages", "/my_stage/path/to/resource"),
        (ApiGatewayV2Deployment, "arn:aws:apigateway:us-east-1::/apis/my_api/deployments/my_deployment", 2, "my_api", "deployments", "/my_deployment"),
        (ApiGatewayV2Authorizer, "arn:aws:apigateway:us-east-1::/apis/my_api/authorizers/my_authorizer", 2, "my_api", "authorizers", "/my_authorizer"),
        (ApiGatewayV2Model, "arn:aws:apigateway:us-east-1::/apis/my_api/models/my_model", 2, "my_api", "models", "/my_model"),
        (ApiGatewayV2Route, "arn:aws:apigateway:us-east-1::/apis/my_api/routes/my_route", 2, "my_api", "routes", "/my_route"),
        (ApiGatewayV2Integration, "arn:aws:apigateway:us-east-1::/apis/my_api/integrations/my_integration", 2, "my_api", "integrations", "/my_integration"),
        (ApiGatewayV2Api, "arn:aws:apigateway:us-east-1::/apis/my_api", 2, "my_api", None, None),
    ]:
        obj = class_.from_arn(arn)
        assert obj.to_arn() == arn
        assert obj.api_gateway_version == api_gateway_version
        assert obj.api_id == api_id
        assert obj.api_res_type == api_res_type
        assert obj.api_res_path == api_res_path
        assert obj.new(
            aws_region=obj.aws_region,
            api_id=obj.api_id,
            api_res_path=obj.api_res_path,
        ) == obj


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.srv.apigateway", preview=False)
