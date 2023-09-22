# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import typing as T
import dataclasses

from ..model import _ResourceIdOnlyRegional


@dataclasses.dataclass
class ApiGateway(_ResourceIdOnlyRegional):
    account_id: T.Optional[str] = dataclasses.field(default=None)
    service: str = dataclasses.field(default="apigateway")


_api_version_to_name_mapper = {
    1: "restapis",
    2: "apis",
}

_api_name_to_version_mapper = {
    "restapis": 1,
    "apis": 2,
}


@dataclasses.dataclass
class _ApiCommon(ApiGateway):
    """
    todo: docstring
    """

    api_gateway_version: int = dataclasses.field(default=None)
    api_id: str = dataclasses.field(default=None)
    api_res_type: str = dataclasses.field(default=None)
    api_res_path: T.Optional[str] = dataclasses.field(default=None)

    def __post_init__(self):
        super().__post_init__()
        if self.resource_id is None:
            self.resource_id = (
                f"/{_api_version_to_name_mapper[self.api_gateway_version]}"
                f"/{self.api_id}/{self.api_res_type}{self.api_res_path}"
            )
        else:
            parts = self.resource_id.split("/", 4)
            self.api_gateway_version = _api_name_to_version_mapper[parts[1]]
            self.api_id = parts[2]
            self.api_res_type = parts[3]
            if len(parts) == 5:
                self.api_res_path = "/" + parts[4]
            else:  # pragma: no cover
                self.api_res_path = None

    @classmethod
    def new(
        cls,
        aws_region: str,
        api_id: str,
        api_res_path: T.Optional[str] = None,
    ):
        """
        Factory method.
        """
        if api_res_path is None:  # pragma: no cover
            api_res_path = ""
        return cls(
            region=aws_region,
            resource_id=None,
            api_id=api_id,
            api_res_path=api_res_path,
        )


@dataclasses.dataclass
class _ApiGatewayStage(_ApiCommon):
    api_res_type: str = dataclasses.field(default="stages")


@dataclasses.dataclass
class _ApiGatewayDeployment(_ApiCommon):
    api_res_type: str = dataclasses.field(default="deployments")


@dataclasses.dataclass
class _ApiGatewayAuthorizer(_ApiCommon):
    api_res_type: str = dataclasses.field(default="authorizers")


@dataclasses.dataclass
class _ApiGatewayModel(_ApiCommon):
    api_res_type: str = dataclasses.field(default="models")


@dataclasses.dataclass
class _ApiGatewayRoute(_ApiCommon):
    api_res_type: str = dataclasses.field(default="routes")


@dataclasses.dataclass
class _ApiGatewayIntegration(_ApiCommon):
    api_res_type: str = dataclasses.field(default="integrations")


@dataclasses.dataclass
class ApiGatewayV1Stage(_ApiGatewayStage):
    api_gateway_version: int = dataclasses.field(default=1)


@dataclasses.dataclass
class ApiGatewayV1Deployment(_ApiGatewayDeployment):
    api_gateway_version: int = dataclasses.field(default=1)


@dataclasses.dataclass
class ApiGatewayV1Authorizer(_ApiGatewayAuthorizer):
    api_gateway_version: int = dataclasses.field(default=1)


@dataclasses.dataclass
class ApiGatewayV1Model(_ApiGatewayModel):
    api_gateway_version: int = dataclasses.field(default=1)


@dataclasses.dataclass
class ApiGatewayV1Route(_ApiGatewayRoute):
    api_gateway_version: int = dataclasses.field(default=1)


@dataclasses.dataclass
class ApiGatewayV1Integration(_ApiGatewayIntegration):
    api_gateway_version: int = dataclasses.field(default=1)


@dataclasses.dataclass
class ApiGatewayV2Stage(_ApiGatewayStage):
    api_gateway_version: int = dataclasses.field(default=2)


@dataclasses.dataclass
class ApiGatewayV2Deployment(_ApiGatewayDeployment):
    api_gateway_version: int = dataclasses.field(default=2)


@dataclasses.dataclass
class ApiGatewayV2Authorizer(_ApiGatewayAuthorizer):
    api_gateway_version: int = dataclasses.field(default=2)


@dataclasses.dataclass
class ApiGatewayV2Model(_ApiGatewayModel):
    api_gateway_version: int = dataclasses.field(default=2)


@dataclasses.dataclass
class ApiGatewayV2Route(_ApiGatewayRoute):
    api_gateway_version: int = dataclasses.field(default=2)


@dataclasses.dataclass
class ApiGatewayV2Integration(_ApiGatewayIntegration):
    api_gateway_version: int = dataclasses.field(default=2)
