# Contributing to BrainGlobe

## Introduction

**Contributors to BrainGlobe are absolutely encouraged**, whether to fix a bug, develop a new feature, or add a new atlas.

There are many BrainGlobe repositories, so it may not be obvious where a new contribution should go.
If you're unsure about any part of the contributing process, please get in touch. The best place is to start a new discussion on
the [image.sc forum](https://forum.image.sc/tag/brainglobe). If you tag your post with `brainglobe` (and optionally a
specific tool, e.g. `cellfinder`) we will see your question and respond as soon as we can.

If you have a query about contributing to a specific tool, please do raise an issue on the relevant GitHub page.
If it's not the correct repository (e.g. `cellfinder` vs `cellfinder-core`), don't worry, we can move it to the relevant repository later. If
for any reason, you'd rather not reach out in public, feel free to
[email](mailto:code@adamltyson.com?subject=brainglobe-contribution) [Adam Tyson](https://github.com/adamltyson), one
of the core developers.

## To contribute a new atlas

To add a new BrainGlobe atlas, please see the guide at
<!--- TODO: Update to new docs website when ready -->
[docs.brainglobe.info](https://docs.brainglobe.info/bg-atlasapi/adding-a-new-atlas).

## To improve the documentation

Documentation for BrainGlobe is **very important** because it is aimed at researchers who may not have much
computational experience. In particular:

- Installation, although simple via PyPI, assumes a lot (functional Python installation, CUDA installation etc.).
- Although most software can be run through a single command, there are a lot of steps, and so a lot to understand.
- There are a lot of parameters that can be changed, and their impact on the final results is not always obvious.
- It is not immediately obvious how to use the results of the pipeline to answer the particular biological question.

For these reasons (and others) every part of all software must be documented as well as possible,
and all new features must be fully documented.

### Editing the documentation

The documentation is built with [gitbook](https://docs.brainglobe.info/) and mirrored in a [GitHub repository](https://github.com/brainglobe/bg-gitbook).

**There are two ways to edit the documentation**:

- **On GitHub**: Click on the link on the right-hand side of the page you want to edit (`Edit on GitHub`),
  make changes online and submit them as a pull request.
- **Locally**: Fork the repository, clone locally, and then submit your changes as a pull request.

N.B. The `brainrender` documentation is hosted in the same way, but separately. The documentation can be found
[here](https://docs.brainrender.info/), and the GitHub repository is
[here](https://github.com/brainglobe/brainrender-docs).

## To contribute code

### Creating a development environment

It is recommended to use `conda` to install a development environment for
BrainGlobe projects. Once you have `conda` installed, the following commands
will create and activate a `conda` environment with the requirements needed
for a development environment:

```sh
conda create -n brainglobe-dev -c conda-forge python=3.10 napari
conda activate brainglobe-dev
```

This installs packages that often can't be installed via `pip`, including
`pyqt`. The specific version of `Python` is chosen to allow `TensorFlow` to be
installed on macOS arm64 machines.

To install a specific BrainGlobe project for development, clone the
GitHub repository, and then run

```sh
pip install -e .[dev]
```

Or if using `zsh`:

```sh
pip install -e '.[dev]'
```

from inside the repository. This will install the package, its dependencies,
and its development dependencies.

### Pull requests

In all cases, please submit code to the main repository via a pull request. The developers recommend, and adhere,
to the following conventions:

- Please submit _draft_ pull requests as early as possible (you can still push to the branch once submitted) to
  allow for discussion.
- One approval of a PR (by a repo owner) is enough for it to be merged.
- Unless someone approves the PR with optional comments, the PR is immediately merged by the approving reviewer.
- Please merge via "Squash and Merge" on GitHub to maintain a clean commit history.
- Ask for a review from someone specific if you think they would be a particularly suited reviewer (possibly noting
  why they are suited on the PR description)

## Development conventions

BrainGlobe includes many tools and individual repositories. We are working towards adopting common standards across
all repositories. Currently, a handful of repositories follow a common set of development conventions:

- [`brainreg`](https://github.com/brainglobe/brainreg)
- [`cellfinder`](https://github.com/brainglobe/cellfinder)
- [`cellfinder-core`](https://github.com/brainglobe/cellfinder-core)
- [`brainreg-napari`](https://github.com/brainglobe/brainreg-napari)
- [`cellfinder-napari`](https://github.com/brainglobe/cellfinder-napari)
- [`brainglobe-napari-io`](https://github.com/brainglobe/brainglobe-napari-io)

The conventions for these repositories are as follows:

### Formatting

We use [Black](https://black.readthedocs.io/en/stable/), [Flake8](https://flake8.pycqa.org/en/latest/),
[isort](https://pycqa.github.io/isort/) and [mypy](https://mypy.readthedocs.io/en/stable/) to ensure a consistent
code style. You may need to run `pre-commit install` before working on the code to ensure that these tests are run
on each commit if you haven't installed as `[dev]`.

To check your code before committing, please run:

- for staged files

```python
pre-commit run
```

- for all files in the repository

```python
pre-commit run -a
```

### Testing

We use [pytest](https://docs.pytest.org/en/latest/) for testing. Please try to ensure that all functions
are tested, including both unit and integration tests.

Some tests may take a long time, e.g. those requiring `TensorFlow` if you don't have a GPU. These tests should be
marked with `@pytest.mark.slow`, e.g.:

```python
import pytest
@pytest.mark.slow
def test_something_slow() -> None:
    slow_result = run_slow_processes()
    assert slow_result == expected_slow_thing, "some useful error message"
```

During development, these "slow" tests can be skipped by running `pytest -m "not slow"`.

### GitHub actions

All commits & pull requests will be built by GitHub actions
([e.g. cellfinder](https://github.com/brainglobe/cellfinder/actions)). To ensure there are no issues, please check
that it builds: `pip install -e .[dev]` and run all the tests: `pytest` before committing changes.

### Versioning

Versioning is taken care of using [bump2version](https://github.com/c4urself/bump2version).
By using the `bump2version` command, new versions are incremented, a `git` tag is made, and when pushed to the remote
repository, that version will be deployed to PyPI. Usage is as follows:

- Bump to new patch version (e.g. `1.0.0` to `1.0.1-rc0`): `bump2version patch`
- Bump to new minor version (e.g. `1.0.0` to `1.1.0-rc0`): `bump2version minor`
- Bump to new major version (e.g. `1.0.0` to `2.0.0-rc0`): `bump2version major`
- Bump to new release candidate version (e.g. `1.0.0-rc0` to `1.0.0-rc1`): `bump2version rc`
- To create a new release version (e.g. `1.0.0-rc0` to `1.0.0`): `bump2version release`

### Dependency support

Packages have to choose which versions of dependencies they officially support,
with minimum supported versions of each dependency used in continuous
integration testing. BrainGlobe projects should follow
[NEP 29 — Recommend Python and NumPy version support as a community policy
standard](https://numpy.org/neps/nep-0029-deprecation_policy.html) to
determine the **minimum** set of supported package versions:

- The last 42 months of Python releases
- The last 24 months of NumPy releases

In addition to this, the last 24 months of other dependencies should also be
supported.

---

## Cellfinder-specific conventions

### Dependencies

Cellfinder includes a lot of functionality brought in from other packages. Each repository must focus on a single task. Changes should be added to the relevant repository:

- **Cell detection in whole-brain microscopy images**: [cellfinder](https://github.com/BrainGlobe/cellfinder)
- **Cell detection algorithm**: [cellfinder-core](https://github.com/BrainGlobe/cellfinder-core)
- **Registration**: [brainreg](https://github.com/brainglobe/brainreg)
- **Image data IO**: [imio](https://github.com/brainglobe/imio)
- **General imaging processing (and other) tools**: [imlib](https://github.com/adamltyson/imlib)

### File paths

All file paths should be defined in `cellfinder.tools.prep.Paths`. Any intermediate file paths, (i.e. those which are not of interest to the typical end-user) should be prefixed with `tmp__`. These should then be cleaned up as soon as possible after generation.

### Releasing `cellfinder-core`

1. Make sure you have [`bump2version`](https://github.com/c4urself/bump2version/#installation) installed.
2. Check out the latest `main` branch from upstream.
3. Run `bump2version <type>`, where `<type>` is replaced by one of {`major`,` minor`, `patch`}. This will create a new pre-release commit and tag with "rc" in
   the filename.
4. Push the result to the cellfinder-core repository using `git push upstream --follow-tags`.
5. Check that all the tests pass, the package builds correctly, and that all built packages are uploaded to PyPI.
6. Check that there are no issues with the new version of `cellfinder-core` and `cellfinder` by going to <https://github.com/brainglobe/cellfinder/actions/workflows/test_and_deploy.yml/>, clicking on the "Run workflow" button on the left, typing "true" into the prompt, and clicking "Run workflow". This will run the `cellfinder` tests with the development version of `cellfinder-core`. Make sure that these tests pass.
7. If something goes wrong, fix the issues, and run `bump2version rc` to create a new release candidate. Push to upstream again, and go back to step 5.
8. Run `bump2version <type>` to tag the final release version, and push to upstream.
9. Check that all the tests pass, the package builds correctly, and that all built packages are uploaded to PyPI.
10. Tag the new version using `bump2version --current-version X.Y.Z-rcN --new-version X.Y.Z <type>` and push to upstream.
