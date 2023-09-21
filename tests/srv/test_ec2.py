# -*- coding: utf-8 -*-

from aws_arns.srv.ec2 import (
    _Ec2Common,
    Ec2Instance,
    Ec2KeyPair,
    EbsVolume,
    EbsSnapshot,
    Ec2NetworkInterface,
    Vpc,
    Subnet,
    RouteTable,
    InternetGateway,
    NatGateway,
    DHCPOptionSet,
    VpcPeeringConnection,
    NetworkACL,
    SecurityGroup,
    SecurityGroupRule,
    VpcEndpoint,
    ElasticIpAllocation,
    VpcCustomGateway,
    VpcPrivateGateway,
    SiteToSiteVPNConnection,
    ClientVPNEndpoint,
    TransitGateway,
    TransitGatewayAttachment,
    Ec2Image,
)


def test():
    class_and_arn_pairs = [
        (
            Ec2Instance,
            "arn:aws:ec2:us-east-1:123456789012:instance/i-1234567890abcdef0",
        ),
        (Ec2KeyPair, "arn:aws:ec2:us-east-1:123456789012:key-pair/i-1234567890abcdef0"),
        (EbsVolume, "arn:aws:ec2:us-east-1:123456789012:volume/vol-1234567890abcdef0"),
        (
            EbsSnapshot,
            "arn:aws:ec2:us-east-1:123456789012:snapshot/snap-1234567890abcdef0",
        ),
        (
            Ec2NetworkInterface,
            "arn:aws:ec2:us-east-1:123456789012:network-interface/eni-1234567890abcdef0",
        ),
        (Vpc, "arn:aws:ec2:us-east-1:123456789012:vpc/vpc-1234567890abcdef0"),
        (Subnet, "arn:aws:ec2:us-east-1:123456789012:subnet/subnet-1234567890abcdef0"),
        (
            RouteTable,
            "arn:aws:ec2:us-east-1:123456789012:route-table/rtb-1234567890abcdef0",
        ),
        (
            InternetGateway,
            "arn:aws:ec2:us-east-1:123456789012:internet-gateway/igw-1234567890abcdef0",
        ),
        (
            NatGateway,
            "arn:aws:ec2:us-east-1:123456789012:natgateway/nat-1234567890abcdef0",
        ),
        (
            DHCPOptionSet,
            "arn:aws:ec2:us-east-1:123456789012:dhcp-options/dopt-1234567890abcdef0",
        ),
        (
            VpcPeeringConnection,
            "arn:aws:ec2:us-east-1:123456789012:vpc-peering-connection/pcx-1234567890abcdef0",
        ),
        (
            NetworkACL,
            "arn:aws:ec2:us-east-1:123456789012:network-acl/acl-1234567890abcdef0",
        ),
        (
            SecurityGroup,
            "arn:aws:ec2:us-east-1:123456789012:security-group/sg-1234567890abcdef0",
        ),
        (
            SecurityGroupRule,
            "arn:aws:ec2:us-east-1:123456789012:security-group-rule/sgr-1234567890abcdef0",
        ),
        (
            VpcEndpoint,
            "arn:aws:ec2:us-east-1:123456789012:vpc-endpoint/vpce-1234567890abcdef0",
        ),
        (
            ElasticIpAllocation,
            "arn:aws:ec2:us-east-1:123456789012:ipv4pool-ec2/eipalloc-1234567890abcdef0",
        ),
        (
            VpcCustomGateway,
            "arn:aws:ec2:us-east-1:123456789012:customer-gateway/cgw-1234567890abcdef0",
        ),
        (
            VpcPrivateGateway,
            "arn:aws:ec2:us-east-1:123456789012:vpn-gateway/vgw-1234567890abcdef0",
        ),
        (
            SiteToSiteVPNConnection,
            "arn:aws:ec2:us-east-1:123456789012:vpn-connection/vpn-1234567890abcdef0",
        ),
        (
            ClientVPNEndpoint,
            "arn:aws:ec2:us-east-1:123456789012:client-vpn-endpoint/cvpn-endpoint-1234567890abcdef0",
        ),
        (
            TransitGateway,
            "arn:aws:ec2:us-east-1:123456789012:transit-gateway/tgw-1234567890abcdef0",
        ),
        (
            TransitGatewayAttachment,
            "arn:aws:ec2:us-east-1:123456789012:transit-gateway-attachment/tgw-attach-1234567890abcdef0",
        ),
        (Ec2Image, "arn:aws:ec2:us-east-1::image/ami-1234567890abcdef0"),
    ]
    for class_, arn in class_and_arn_pairs:
        obj: _Ec2Common = class_.from_arn(arn)
        assert obj.to_arn() == arn
        assert obj.long_id == f"{obj.id_prefix}-{obj.short_id}"
        assert (
            class_.new(
                aws_account_id=obj.aws_account_id,
                aws_region=obj.aws_region,
                resource_id=obj.resource_id,
            )
            == obj
        )


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.srv.ec2", preview=False)
