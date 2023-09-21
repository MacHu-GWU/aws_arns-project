# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import dataclasses

from ..model import _SlashSeparatedRegional


@dataclasses.dataclass
class Ec2(_SlashSeparatedRegional):
    service: str = dataclasses.field(default="ec2")


@dataclasses.dataclass
class _Ec2Common(Ec2):
    """
    todo: docstring
    """

    @classmethod
    def new(
        cls,
        aws_account_id: str,
        aws_region: str,
        resource_id: str,
    ):
        """
        Factory method.
        """
        return cls(
            account_id=aws_account_id,
            region=aws_region,
            resource_id=resource_id,
        )

    _id_prefix: str = None

    @property
    def id_prefix(self) -> str:
        """
        "vpc" part of the "vpc-1234567890abcdef0".
        """
        return "-".join(self.resource_id.split("-")[:-1])

    @property
    def short_id(self) -> str:
        """
        "1234567890abcdef0" part of the "vpc-1234567890abcdef0".
        """
        return self.resource_id.split("-")[-1]

    @property
    def long_id(self) -> str:
        """
        The "vpc-1234567890abcdef0".
        """
        return self.resource_id


@dataclasses.dataclass
class Ec2Instance(_Ec2Common):
    resource_type: str = dataclasses.field(default="instance")

    _id_prefix = "i"

    @property
    def instance_id(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class Ec2KeyPair(_Ec2Common):
    resource_type: str = dataclasses.field(default="key-pair")

    _id_prefix = "key"

    @property
    def key_name(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class EbsVolume(_Ec2Common):
    resource_type: str = dataclasses.field(default="volume")

    _id_prefix = "vol"

    @property
    def volume_id(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class EbsSnapshot(_Ec2Common):
    resource_type: str = dataclasses.field(default="snapshot")

    _id_prefix = "snap"

    @property
    def volume_id(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class Ec2NetworkInterface(_Ec2Common):
    resource_type: str = dataclasses.field(default="network-interface")

    _id_prefix = "eni"

    @property
    def network_interface_id(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class Vpc(_Ec2Common):
    resource_type: str = dataclasses.field(default="vpc")

    _id_prefix = "vpc"

    @property
    def instance_id(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class Subnet(_Ec2Common):
    resource_type: str = dataclasses.field(default="subnet")

    _id_prefix = "subnet"

    @property
    def subnet_id(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class RouteTable(_Ec2Common):
    resource_type: str = dataclasses.field(default="route-table")

    _id_prefix = "rtb"

    @property
    def route_table_id(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class InternetGateway(_Ec2Common):
    resource_type: str = dataclasses.field(default="internet-gateway")

    _id_prefix = "igw"

    @property
    def internet_gateway_id(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class NatGateway(_Ec2Common):
    resource_type: str = dataclasses.field(default="natgateway")

    _id_prefix = "nat"

    @property
    def nat_gateway_id(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class DHCPOptionSet(_Ec2Common):
    resource_type: str = dataclasses.field(default="dhcp-options")

    _id_prefix = "dopt"

    @property
    def dhcp_option_set_id(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class VpcPeeringConnection(_Ec2Common):
    resource_type: str = dataclasses.field(default="vpc-peering-connection")

    _id_prefix = "pcx"

    @property
    def vpc_peering_connection_id(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class NetworkACL(_Ec2Common):
    resource_type: str = dataclasses.field(default="network-acl")

    _id_prefix = "acl"

    @property
    def network_acl_id(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class SecurityGroup(_Ec2Common):
    resource_type: str = dataclasses.field(default="security-group")

    _id_prefix = "sg"

    @property
    def sg_id(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class SecurityGroupRule(_Ec2Common):
    resource_type: str = dataclasses.field(default="security-group-rule")

    _id_prefix = "sgr"

    @property
    def sg_id(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class VpcEndpoint(_Ec2Common):
    resource_type: str = dataclasses.field(default="vpc-endpoint")

    _id_prefix = "vpce"

    @property
    def vpc_endpoint_id(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class ElasticIpAllocation(_Ec2Common):
    resource_type: str = dataclasses.field(default="ipv4pool-ec2")

    _id_prefix = "eipalloc"

    @property
    def elastic_ip_allocation_id(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class VpcCustomGateway(_Ec2Common):
    resource_type: str = dataclasses.field(default="customer-gateway")

    _id_prefix = "cgw"

    @property
    def vpc_custom_gateway_id(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class VpcPrivateGateway(_Ec2Common):
    resource_type: str = dataclasses.field(default="vpn-gateway")

    _id_prefix = "vgw"

    @property
    def vpc_private_gateway_id(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class SiteToSiteVPNConnection(_Ec2Common):
    resource_type: str = dataclasses.field(default="vpn-connection")

    _id_prefix = "vpn"

    @property
    def vpn_connection_id(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class ClientVPNEndpoint(_Ec2Common):
    resource_type: str = dataclasses.field(default="client-vpn-endpoint")

    _id_prefix = "cvpn-endpoint"

    @property
    def client_vpn_endpoint_id(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class TransitGateway(_Ec2Common):
    resource_type: str = dataclasses.field(default="transit-gateway")

    _id_prefix = "tgw"

    @property
    def transit_gateway_id(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class TransitGatewayAttachment(_Ec2Common):
    resource_type: str = dataclasses.field(default="transit-gateway-attachment")

    _id_prefix = "tgw-attach"

    @property
    def transit_gateway_attachment_id(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class TransitGatewayAttachment(_Ec2Common):
    resource_type: str = dataclasses.field(default="transit-gateway-attachment")

    _id_prefix = "tgw-attach"

    @property
    def transit_gateway_attachment_id(self) -> str:  # pragma: no cover
        return self.resource_id


@dataclasses.dataclass
class Ec2Image(_Ec2Common):
    resource_type: str = dataclasses.field(default="image")

    _id_prefix = "ami"

    @property
    def ami_id(self) -> str:  # pragma: no cover
        return self.resource_id
