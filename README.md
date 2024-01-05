[![PyPI version](https://badge.fury.io/py/brainglobe.svg)](https://badge.fury.io/py/brainglobe)
[![Website](https://img.shields.io/website?up_message=online&url=https%3A%2F%2Fbrainglobe.info)](https://brainglobe.info)
[![Twitter](https://img.shields.io/twitter/follow/brain_globe?style=social)](https://twitter.com/brain_globe)

[![Brainglobe logo](https://brainglobe.info/_static/brainglobe.png)](https://brainglobe.info)

# BrainGlobe

This package provides all [BrainGlobe](https://brainglobe.info) tools in one place, installable [in a single command](#installation).
Installing this package will provide you with the complete suite of BrainGlobe tools, without needing to worry about dependency resolution.
A complete list of the tools provided by this package [is provided on our website](TODO:FIXME), and you can also read more about these tools in the [online documentation](https://brainglobe.info/documentation/index.html).

If you are interested in running some of our analysis workflows, you might want to head over to [`brainglobe-workflows`](https://github.com/brainglobe/brainglobe-workflows) and install the analysis pipelines offered by that package too.

## Installation

The current installation process is via `pip`.
We recommend you install this package into a clean virtual environment (preferably either `venv` or `conda`-managed), that has Python 3.9 or newer.
Once you have activated your environment, running

```bash
pip install brainglobe
```

This will fetch and install all `brainglobe` packages and tools into your current environment.

### Is BrainGlobe Available on `conda-forge`?

If you plan on using multiple BrainGlobe tools in your analysis, we strongly recommend you install this package via `pip`, into a clean virtual environment (preferably either `venv` or `conda`-managed).

Providing BrainGlobe through `conda-forge` is in our development plan, and a number of the individual BrainGlobe tools are available on conda-forge for individual install.
However, if you plan on using multiple BrainGlobe tools in your analysis, we still (strongly) recommend installing via `pip` as this will ensure your BrainGlobe tools are consistent with each other.

### Manual package installs

If you are comfortable with manually managing the interdependency of your tools, you can install the individual BrainGlobe tools from PyPI directly.
Please note that if you chose to install tools like this, we cannot guarantee that your tools will be consistent with each other - this is particularly true if you plan to use any of the [analysis workflows](https://github.com/brainglobe/brainglobe-workflows) that we provide.

Those tools that are available on `conda-forge` can likewise be manually installed into your environment.
We are currently in the process of making BrainGlobe's tools available from `conda-forge` as an alternative to `PyPI`, however certain tools are currently not available on `conda-forge`.
Of particular note are:

- `brainrender`
- `cellfinder` ([see below](#cellfinder-and-conda-forge))
- `brainglobe-workflows` (if you wish to use the pre-written analysis pipelines or `brainmapper`)

#### **`cellfinder` and `conda-forge`**

Choosing to install via `conda` will provide the (source code for the) `cellfinder` tool.
However due to an ongoing issue with `tensorflow`'s availability on `conda-forge`, the install _will not_ provide `tensorflow` itself.
This is because `tensorflow` versions newer than `1.14.0` are not provided via `conda` channels, and `cellfinder-core` (one of the brainglobe tools) requires a version between `2.5.0` and `2.11.1`.
See [this issue on GitHub for more details](https://github.com/conda-forge/cellfinder-core-feedstock/issues/13).
Users that want to run `cellfinder` will need to manually install a compatible version of `tensorflow` into their environment, before running the `conda install` command above.

- Windows users will _have_ to manually install their own version of `tensorflow` if they want to use the `conda-forge` install and the `cellfinder` tools.
- `conda-forge` _may_ be able to resolve the dependencies automatically for Linux and MacOS users, however we do not guarantee this. In such a case, a manual install of `tensorflow` will be required first.

If using the `conda-forge` install; attempting to `import` any of `cellfinder`, `cellfinder-napari`, or `cellfinder-core` in your Python scripts may throw an error if the issues above cannot be resolved on your platform.
Similarly, attempting to use `cellfinder`'s CLI functionality will also raise an error.

## Contributing

**Contributors to BrainGlobe are absolutely encouraged**, whether to fix a bug, develop a new feature, or add a new atlas.
If you would like to contribute, please take a look at our [developer documentation](https://brainglobe.info/developers/index.html).

---

# The Brainglobe Initiative

The BrainGlobe Initiative exists to facilitate the development of interoperable Python-based tools for computational neuroanatomy.

We have three aims:

- Develop specialist software for specific analysis and visualisation needs, such as [cellfinder](https://github.com/brainglobe/cellfinder) and [brainrender](https://github.com/brainglobe/brainrender).
- Develop core tools to facilitate others to build interoperable tools in Python, e.g. the [BrainGlobe Atlas API](https://github.com/brainglobe/bg-atlasapi).
- Build a community of neuroscientists and developers to share knowledge, build software and engage with the scientific, and open-source community (e.g. by organising hackathons).

## [Funding](https://brainglobe.info/funders.html#funders) Information

The BrainGlobe project is only possible due to grant funding and the generous support of host institutions, whose information [can be found on this website](https://brainglobe.info/funders.html#funders).
