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

### [**Funding**](https://brainglobe.info/funders.html#funders) Information

The BrainGlobe project is only possible due to grant funding and the generous support of host institutions, whose information [can be found on this website](https://brainglobe.info/funders.html#funders).

---

## Installation

The `brainglobe` package can be installed from [PyPI](https://pypi.org/project/brainglobe/) into a Python environment by running
```sh
pip install brainglobe
```

If you want to install the additional packages `morphapi` and `cellfinder`, you can specify them as optional dependencies:
```sh
pip install brainglobe[morphapi] # Include morphapi
pip install brainglobe[cellfinder] # Include cellfinder
pip install brainglobe[morphapi,cellfinder] # Include both morphapi and cellfinder
```

Alternatively, you can download the source from [PyPI here](https://pypi.org/project/brainglobe/#files).

## Contributing

**Contributors to BrainGlobe are absolutely encouraged**, whether to fix a bug, develop a new feature, or add a new atlas.
If you would like to contribute, please take a look at our [developer documentation](https://brainglobe.info/developers/index.html).
