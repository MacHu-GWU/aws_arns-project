.. _release_history:

Release and Version History
==============================================================================


Backlog (TODO)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


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
