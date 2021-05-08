# Currency Scrapper

Currency Scrapper is a data application which extracts, transforms and loads
currency information using Apache Airflow.

This project is currently a **work in progress**.

## Contents

- [Building and Running](#Building-and-Running-)
- [Testing](#Testing-)
- [Structure](#Structure-)
- [Branching](#Branching-)
- [Versioning](#Versioning-)
  - [How to increment the version](#How-to-increment-the-version-)
- [Committing](#Committing-)
- [References](#References-)

## Building and Running [[^](#Contents)]

TODO.

## Testing [[^](#Contents)]

TODO.

## Structure [[^](#Contents)]

TODO.

## Branching [[^](#Contents)]

TODO.

## Versioning [[^](#Contents)]

The project uses the [bump2version](https://pypi.org/project/bump2version) in
order to control the version numbers following the [semantic versioning 2.0.0](https://semver.org).

### How to increment the version [[^](#Contents)]

**After commit a modification** (because the repository must be clean), you
must update the version according to the following rules:

- Increment the `MAJOR` version when you make incompatible API changes.
- Increment the `MINOR` version when you add functionality in a backwards compatible manner.
- Increment the `PATCH` version when you make backward compatible bug fixes.

It's possible to perform a dry-run test without touch any file, for example with
a `MINOR`, run:

```console
$ bump2version --dry-run --verbose minor
Reading config file .bumpversion.cfg:
[bumpversion]
current_version = 0.1.0
commit = False
tag = False

[bumpversion:file:setup.py]

Attempting to increment part 'minor'
Values are now: major=0, minor=5, patch=0
Dry run active, won't touch any files.
New version will be '0.2.0'
Asserting files setup.py contain the version string...
current_version=0.1.0
commit=False
tag=False
new_version=0.2.0
Would write to config file .bumpversion.cfg:
[bumpversion]
current_version = 0.2.0
commit = False
tag = False

[bumpversion:file:setup.py]


Would prepare Git commit
Would add changes in file 'setup.py' to Git
Would add changes in file '.bumpversion.cfg' to Git
Would commit to Git with message 'Bump version: 0.1.0 → 0.2.0'
Would tag 'v0.2.0' with message 'Bump version: 0.1.0 → 0.2.0' in Git and not signing
```

To increment the `MAJOR` version run:

```console
$ bump2version major --commit
Check for added large files..............................................Passed
Check for case conflicts.................................................Passed
Check docstring is first.................................................Passed
Check that executables have shebangs.................(no files to check)Skipped
Check for merge conflicts................................................Passed
Check Yaml...........................................(no files to check)Skipped
Detect Private Key.......................................................Passed
Fix End of Files.........................................................Passed
Tests should match the pattern test*.py..............(no files to check)Skipped
Trim Trailing Whitespace.................................................Passed
black....................................................................Passed
flake8...................................................................Passed
```

To increment the `MINOR` version run:

```console
$ bump2version minor --commit
Check for added large files..............................................Passed
Check for case conflicts.................................................Passed
Check docstring is first.................................................Passed
Check that executables have shebangs.................(no files to check)Skipped
Check for merge conflicts................................................Passed
Check Yaml...........................................(no files to check)Skipped
Detect Private Key.......................................................Passed
Fix End of Files.........................................................Passed
Tests should match the pattern test*.py..............(no files to check)Skipped
Trim Trailing Whitespace.................................................Passed
black....................................................................Passed
flake8...................................................................Passed
```

To increment the `PATCH` version run:

```console
$ bump2version patch --commit
Check for added large files..............................................Passed
Check for case conflicts.................................................Passed
Check docstring is first.................................................Passed
Check that executables have shebangs.................(no files to check)Skipped
Check for merge conflicts................................................Passed
Check Yaml...........................................(no files to check)Skipped
Detect Private Key.......................................................Passed
Fix End of Files.........................................................Passed
Tests should match the pattern test*.py..............(no files to check)Skipped
Trim Trailing Whitespace.................................................Passed
black....................................................................Passed
flake8...................................................................Passed
```

Then you can go ahead and commit again to send the updated versioning files.

## Committing [[^](#Contents)]

TODO.

## References [[^](#Contents)]

- [The Twelve-Factor App](https://12factor.net)
- [Running Airflow in Docker](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html)
