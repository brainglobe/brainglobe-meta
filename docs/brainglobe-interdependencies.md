# BrianGlobe constituent packages

List of tools that BrianGlobe provides, the corresponding repository in which the source code for the tool resides, and any dependencies on other BrainGlobe packages.

Packages are listed top to bottom based on the number of brainglobe dependencies they posses, IE packages appear earlier in the list if they appear _lower down_ in the BrainGlobe dependency tree.

![Interdependency graph for BrainGlobe tools](assets/BrainGlobe-dependencies.svg)

## Repositories

|        Package         |                        Repo                        |                    `PyPI`                     |                         `conda-forge`                         |
| :--------------------: | :------------------------------------------------: | :-------------------------------------------: | :-----------------------------------------------------------: |
|       `bg-space`       |       https://github.com/brainglobe/bg-space       |       https://pypi.org/project/bg-space       |       https://github.com/conda-forge/bg-space-feedstock       |
|   `brainglobe-utils`   |   https://github.com/brainglobe/brainglobe-utils   |   https://pypi.org/project/brainglobe-utils   |   https://github.com/conda-forge/brainglobe-utils-feedstock   |
|     `bg-atlasapi`      |     https://github.com/brainglobe/bg-atlasapi      |     https://pypi.org/project/bg-atlasapi      |     https://github.com/conda-forge/bg-atlasapi-feedstock      |
|       `brainreg`       |       https://github.com/brainglobe/brainreg       |       https://pypi.org/project/brainreg       |       https://github.com/conda-forge/brainreg-feedstock       |
|         `imio`         |         https://github.com/brainglobe/imio         |         https://pypi.org/project/imio         |         https://github.com/conda-forge/imio-feedstock         |
|   `cellfinder-core`    |   https://github.com/brainglobe/cellfinder-core    |   https://pypi.org/project/cellfinder-core    |   https://github.com/conda-forge/cellfinder-core-feedstock    |
|       `morphio`        |       https://github.com/brainglobe/morphapi       |       https://pypi.org/project/morphio        |                           See notes                           |
| `brainglobe-napari-io` | https://github.com/brainglobe/brainglobe-napari-io | https://pypi.org/project/brainglobe-napari-io | https://github.com/conda-forge/brainglobe-napari-io-feedstock |
|     `bg-atlasgen`      |     https://github.com/brainglobe/bg-atlasgen      |                   See notes                   |                           See notes                           |
|   `brainglobe-segmentation`   |   https://github.com/brainglobe/brainglobe-segmentation   |   https://pypi.org/project/brainglobe-segmentation   |   https://github.com/conda-forge/brainglobe-segmentation-feedstock   |
|  `cellfinder-napari`   |  https://github.com/brainglobe/cellfinder-napari   |  https://pypi.org/project/cellfinder-napari   |  https://github.com/conda-forge/cellfinder-napari-feedstock   |
|      `cellfinder`      |      https://github.com/brainglobe/cellfinder      |      https://pypi.org/project/cellfinder      |                         Not available                         |


## Notes

- `bg-atlasgen`
  - Not on PyPI, intended to be locally installed to generate data to add a new BrainGlobe atlas.
- `brainglobe-napari`
  - **Work in progress**
  - [Repository](https://github.com/brainglobe/brainglobe-napari)
  - Napari plugin for [bg-atlasapi](#bg-atlasapi). Note that repository README uses the name "brainglobe" for "bg-atlasapi" due to a historical renaming.
  - Dependencies: `bg-atlasapi`
