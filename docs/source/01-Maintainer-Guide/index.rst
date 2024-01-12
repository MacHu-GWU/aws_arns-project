Maintainer Guide
==============================================================================


Objective
------------------------------------------------------------------------------
这个库的目的是方便开发者解析 ARN 和生成 ARN.


Understand ARN
------------------------------------------------------------------------------
根据官方文档 `Amazon Resource Names (ARNs) <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_, Arn 有这么几个部分组成:

- partition: AWS 的分区, 各个分区之间物理隔离. 所有的商业版 AWS 位于 ``aws``, 北美政府分区则是 ``aws-us-gov``, 中国分区则是 ``aws-cn``.
- service: 每个 AWS Service 的名字, 比如 ``s3``, ``iam``, ``batch`` 等等.
- region: AWS 的地理区, 例如 ``us-east-1``, ``us-west-1`` 等等. 有的服务是全球性的, 例如 s3, iam, 那么在 ARN 中该部分就是空字符串.
- account_id: AWS 的 Account id, 例如 ``111122223333``, 有的服务是跨 Account 的, 例如 s3, 那么在 ARN 中该部分就是空字符串.
- resource_type: 一个 service 下可能有很多不同的资源, 例如 IAM 下有 group, user, role, policy. 但是有的 service 可能只有一种资源, 例如 SNS, SQS, 就不会有 resource_type. 所以这个字段是可选的.
- sep: 用于分隔 resource_type 和 resource_id 的分隔符, 例如 IAM 中就是 "/", 而 Lambda 中就是 ":". 如果是 service 下只有一种资源的情况, 例如 SNS, SQS, 就不会有 sep. 所以这个字段就是可选的.
- resource_id: 在 service 下的资源唯一标志符. 对于有的资源 resource_id 和你创建资源时指定的人类可读的 name 是一样的, 例如 Lambda function 的名字. 有的资源的 resource_id 是系统生成的, 例如你创建 EC2 时生成的 instance_id, 这个和你创建时候指定的 name 是不一样的. 这个字段是必选项.

从分类上看, 有以下几种 ARN format:

- format: ``arn:${partition}:${service}:${region}:${account-id}:${resource-id}``
    - example: ``arn:aws:sqs:us-east-1:111122223333:my-queue``
- format: ``arn:${partition}:${service}:${region}:${account-id}:${resource-type}${sep}${resource-id}``
    - example sep = "/": ``arn:aws:iam::111122223333:role/aws-service-role/batch.amazonaws.com/AWSServiceRoleForBatch``
- format: ``arn:${partition}:${service}:${region}:${account-id}:${resource-type}${sep}${resource-id}``
    - example sep = ":": ``arn:aws:lambda:us-east-1:111122223333:function:my-func``


Data Modeling
------------------------------------------------------------------------------
为了保持代码结构清晰, 我们用面向对象的思维将类的继承关系设计如下:

首先有一个 BaseArn, 它是所有 Arn 类的基类. 它有全部的 7 个字段, 并且除了 partition 字段 (之后再解释为什么), 它们的默认值都是 NOTHING. 如果任何一个字段在初始化的时候没有赋值, ``__post_init__`` 方法就会报错::

    @dataclasses.dataclass
    class BaseArn:
        partition: str = dataclasses.field(default="aws")
        service: str = dataclasses.field(default=NOTHING)
        region: T.Optional[str] = dataclasses.field(default=NOTHING)
        account_id: T.Optional[str] = dataclasses.field(default=NOTHING)
        resource_type: T.Optional[str] = dataclasses.field(default=NOTHING)
        sep: T.Optional[str] = dataclasses.field(default=NOTHING)
        resource_id: str = dataclasses.field(default=NOTHING)

        def __post_init__(self):
            for k, v in dataclasses.asdict(self).items():
                if isinstance(v, _Nothing):
                    raise ValueError(f"arg '{k}' is required")

由前面的分析我们可以看出, 按照 ARN 的格式, 我们可以将其分为以下几类:

- ``CrossAccountGlobal``: 跨 Account 的 global 资源, 例如 S3, ARN 中既没有 account_id 也没有 region.
- ``Global``: global 资源, 例如 IAM, ARN 中没有 region.
- ``Regional``: regional 资源, 大部分的 AWS 服务都属于这一类别. 在这一类别下又分为以下几种
    - ``ResourceIdOnlyRegional``: 只有 resource_id, 没有 resource_type, 例如 SNS, SQS.
    - ``ColonSeparatedRegional``: 用 ":" 分隔 type 和 id, 例如 Lambda
    - ``SlashSeparatedRegional``: 用 "/" 分隔 type 和 id, 例如 CloudFormation, 大部分的服务属于此类

而这些子类都是继承了 ``BaseArn`` 类, 并且 override 了一些属性并给这些属性赋予了默认值, 例如 ``CrossAccountGlobal`` 中的 account_id 和 region 的默认值都是 None.

这里有必要解释一下 partition. 由于存在 3 种 partition, 并且另外 99% 的用户都在 aws commercial 上, 其他两种 Partition 用的很少, 我们不想为了另外两种 Partition 的情况为每一个 AWS Resource 对象专门新创建两个类, 这样代码太臃肿了. 所以我们提供了两个方法能将创建的实例转化为另外两个 partition 中的情况::

    @dataclasses.dataclass
    class BaseArn:
        ...

        def with_us_gov_partition(self):
            self.partition = AwsPartitionEnum.aws_us_gov.value
            return self

        def with_cn_partition(self):
            self.partition = AwsPartitionEnum.aws_cn.value
            return self

对于每个 AWS Service, 我们会根据 ARN format 继承 ``CrossAccountGlobal``, ``ColonSeparatedRegional``, ``SlashSeparatedRegional`` 等几个类中的一个. 并且 override, service 属性并提供默认值, 例如::

    @dataclasses.dataclass
    class AwsLambda(_ColonSeparatedRegional):
        service: str = dataclasses.field(default="lambda")

而对于每个 AWS Service 下的 resource, 则会继承这个父类, 并且 override resource_type 属性, 例如::

    @dataclasses.dataclass
    class LambdaFunction(_ColonSeparatedRegional):
        resource_type: str = dataclasses.field(default="function")

这样的代码设计能大幅简化我们声明每个 AWS Resource 专属的 ARN 的类的工作量.

最后, 为了方便用户 Import 以及测试, 我们创建了一个 ``gen_code/gen_code.py`` 脚本. 它能自动生成 ``aws_arns/resource.py`` 文件, 这个文件会把所有定义过的 AWS Resource 类 import 进来, 使得用户只要打出 ``aws_arns.res.``, IDE 就会自动补全所要使用的类. ``aws_arns/resource.py`` 的文件内容看起来像这个样子::

    from .srv.awslambda import LambdaFunction
    from .srv.awslambda import LambdaLayer
    from .srv.batch import BatchComputeEnvironment
    from .srv.batch import BatchJob
    from .srv.batch import BatchJobDefinition
    from .srv.batch import BatchJobQueue
    from .srv.batch import BatchSchedulingPolicy


Complete List of AWS Resources that Support ARN
------------------------------------------------------------------------------
如果要获得完整的支持 ARN 的 Resource 的列表以及它们的格式, 最好的方法是在 `AWS IAM Policy 中创建一个新的 Policy <https://us-east-1.console.aws.amazon.com/iam/home?region=us-east-1#/policies/create?step=edit>`_, 然后选则一个 Service, 并选择 All action. 然后底下 resource 一栏就会出现所有支持 ARN 的 resource 的列表. 每个 resource 旁边有个 information 的符号, 点开就可以看到 ARN 的格式.
