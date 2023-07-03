[![PyPI version](https://badge.fury.io/py/brainglobe.svg)](https://badge.fury.io/py/brainglobe)
[![Website](https://img.shields.io/website?up_message=online&url=https%3A%2F%2Fbrainglobe.info)](https://brainglobe.info)
[![Twitter](https://img.shields.io/twitter/follow/brain_globe?style=social)](https://twitter.com/brain_globe)

# brainglobe

The BrainGlobe Initiative exists to facilitate the development of interoperable
Python-based tools for computational neuroanatomy.

We have three aims:

- Develop specialist software for specific analysis and visualisation needs,
  such as [cellfinder](https://github.com/brainglobe/cellfinder) and
  [brainrender](https://github.com/brainglobe/brainrender).

- Develop core tools to facilitate others to build interoperable tools in Python, e.g. the
  [BrainGlobe Atlas API](https://github.com/brainglobe/bg-atlasapi).

- Build a community of neuroscientists and developers to share knowledge, build software and engage
  with the scientific, and open-source community (e.g. by organising hackathons).

## This Package Provides:

This package provides all BrainGlobe tools in one place, requested [through a single command](#installation).

You can read more about the individual tools on the [documentation website](https://brainglobe.info/documentation/index.html).
Currently included packages, and whether they come with the `pip` and `conda-forge` installs are listed below:
|               Package                |  `pip`   | `conda`  | How to access |                               Documentation                               |
| :----------------------------------: | :------: | :------: | :-----------: | :-----------------------------------------------------------------------: |
| BrainGlobe Atlas API (`bg-atlasapi`) | &#x2611; | &#x2611; |               |   [Site](https://brainglobe.info/documentation/bg-atlasapi/index.html)    |
|              `bg-space`              | &#x2611; | &#x2611; |               |     [Site](https://brainglobe.info/documentation/bg-space/index.html)     |
|              `brainreg`              | &#x2611; | &#x2611; |               |     [Site](https://brainglobe.info/documentation/brainreg/index.html)     |
|          `brainreg-segment`          | &#x2611; | &#x2611; |               | [Site](https://brainglobe.info/documentation/brainreg-segment/index.html) |
|            `brainrender`             |          |          |               |   [Site](https://brainglobe.info/documentation/brainrender/index.html)    |
|             `cellfinder`             | &#x2611; |          |               |    [Site](https://brainglobe.info/documentation/cellfinder/index.html)    |
|              `morphapi`              | &#x2611; |          |               |     [Site](https://brainglobe.info/documentation/morphapi/index.html)     |


### [**Funding**](https://brainglobe.info/funders.html#funders) Information

The BrainGlobe project is only possible due to grant funding and the generous support of host institutions, whose information [can be found on this website](https://brainglobe.info/funders.html#funders).

---

## Installation

We recommend users install into a fresh virtual environment using `pip`; since this will resolve all complex dependencies (like `tensorflow`) automatically, across all operating systems and (compatible) Python versions.

### **Recommended**: via `pip`
The `brainglobe` package can be installed from [PyPI](https://pypi.org/project/brainglobe/) into a Python environment by running
```sh
pip install brainglobe
```
This will fetch and install all `brainglobe` packages and tools into your current environment.
Alternatively, you can download the source from [PyPI here](https://pypi.org/project/brainglobe/#files).

### **Alternatives**: via `conda`
We are currently in the process of making BrainGlobe's tools available from `conda-forge` as an alternative to `PyPI`.
However certain tools are currently not available on `conda-forge`, specifically:
- `brainrender` (in progress)
- `morphapi` (in progress)
- `cellfinder` ([see below](#cellfinder-and-conda-forge))

In your desired virtual environment, run
```sh
conda install -c conda-forge brainglobe
```
to install the compatible BrainGlobe tools.

#### **`cellfinder` and `conda-forge`**

Choosing to install via `conda` will provide the (source code for the) `cellfinder` tool.
However due to an ongoing issue with `tensorflow`'s availability on `conda-forge`, the install _will not_ provide `tensorflow` itself.
This is because `tensorflow` versions newer than `1.14.0` are not provided via `conda` channels, and `cellfinder-core` (one of the brainglobe tools) requires a version between `2.5.0` and `2.11.1`.
See [this issue on GitHub for more details](https://github.com/conda-forge/cellfinder-core-feedstock/issues/13).
Users that want to run `cellfinder` will need to manually install a compatible version of `tensorflow` into their environment, before running the `conda install` command above.

---

## Contributing

**Contributors to BrainGlobe are absolutely encouraged**, whether to fix a bug, develop a new feature, or add a new atlas.
If you would like to contribute, please take a look at our [developer documentation](https://brainglobe.info/developers/index.html).
