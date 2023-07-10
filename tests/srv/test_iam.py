# -*- coding: utf-8 -*-

from aws_arns.srv.iam import (
    IamGroup,
    IamUser,
    IamRole,
    IamPolicy,
    IamInstanceProfile,
)


def test():
    arn = "arn:aws:iam::111122223333:group/Admin"
    iam_group = IamGroup.from_arn(arn)
    assert iam_group.region is None
    assert iam_group.iam_group_name == "Admin"
    assert (
        IamGroup.new(aws_account_id=iam_group.account_id, name=iam_group.iam_group_name)
        == iam_group
    )

    arn = "arn:aws:iam::111122223333:user/alice"
    iam_user = IamUser.from_arn(arn)
    assert iam_user.region is None
    assert iam_user.iam_user_name == "alice"
    assert (
        IamUser.new(aws_account_id=iam_user.account_id, name=iam_user.iam_user_name)
        == iam_user
    )

    arn = "arn:aws:iam::111122223333:role/aws-service-role/batch.amazonaws.com/AWSServiceRoleForBatch"
    iam_role = IamRole.from_arn(arn)
    assert iam_role.region is None
    assert (
        iam_role.iam_role_name
        == "aws-service-role/batch.amazonaws.com/AWSServiceRoleForBatch"
    )
    assert iam_role.is_service_role() is True
    assert iam_role.short_name == "AWSServiceRoleForBatch"
    assert (
        IamRole.new(aws_account_id=iam_role.account_id, name=iam_role.iam_role_name)
        == iam_role
    )

    arn = "arn:aws:iam::111122223333:policy/service-role/codebuild-policy"
    iam_policy = IamPolicy.from_arn(arn)
    assert iam_policy.region is None
    assert iam_policy.iam_policy_name == "service-role/codebuild-policy"
    assert iam_policy.short_name == "codebuild-policy"
    assert (
        IamPolicy.new(
            aws_account_id=iam_policy.account_id, name=iam_policy.iam_policy_name
        )
        == iam_policy
    )

    arn = (
        "arn:aws:iam::807388292768:instance-profile/cloud9/AWSCloud9SSMInstanceProfile"
    )
    iam_instance_profile = IamInstanceProfile.from_arn(arn)
    assert iam_instance_profile.region is None
    assert (
        iam_instance_profile.iam_instance_profile_name
        == "cloud9/AWSCloud9SSMInstanceProfile"
    )
    assert (
        IamInstanceProfile.new(
            aws_account_id=iam_instance_profile.account_id,
            name=iam_instance_profile.iam_instance_profile_name,
        )
        == iam_instance_profile
    )


if __name__ == "__main__":
    from aws_arns.tests.helper import run_cov_test

    run_cov_test(__file__, "aws_arns.srv.iam", preview=False)
