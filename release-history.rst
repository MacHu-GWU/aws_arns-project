.. _release_history:

Release and Version History
==============================================================================


Backlog (TODO)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


0.3.1 (2023-07-11)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Add the following AWS Resources to public API:
    - ``aws_arns.api.IamGroup``
    - ``aws_arns.api.IamUser``
    - ``aws_arns.api.IamRole``
    - ``aws_arns.api.IamPolicy``
    - ``aws_arns.api.IamInstanceProfile``
    - ``aws_arns.api.BatchComputeEnvironment``
    - ``aws_arns.api.BatchJobQueue``
    - ``aws_arns.api.BatchJobDefinition``
    - ``aws_arns.api.BatchJob``
    - ``aws_arns.api.BatchSchedulingPolicy``
    - ``aws_arns.api.A2IHumanReviewWorkflow``
    - ``aws_arns.api.A2IHumanLoop``
    - ``aws_arns.api.A2IWorkerTaskTemplate``
    - ``aws_arns.api.CloudFormationStack``
    - ``aws_arns.api.CloudFormationChangeSet``
    - ``aws_arns.api.CloudFormationStackSet``
    - ``aws_arns.api.CodeBuildProject``
    - ``aws_arns.api.CodeBuildRun``
    - ``aws_arns.api.S3Bucket``
    - ``aws_arns.api.S3Object``


0.2.1 (2023-07-11)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Breaking changes**

- Redesign the API, now we should do ``from aws_arns import api`` instead of ``from aws_arns import ...``.
- Redesign the data class, add ``CrossAccountGlobal``, ``Global``, ``Regional``, ``ResourceIdOnlyRegional``, ``ColonSeparatedRegional``, ``SlashSeparatedRegional``.

**Features and Improvements**

- Add ``iam``, ``batch`` modules.

**Miscellaneous**

- Redesign the testing strategy.


0.1.1 (2023-03-15)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- First release.
- Add ``ARN`` class.
