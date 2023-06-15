# BrianGlobe constituent packages

List of tools that BrianGlobe provides, the corresponding repository in which the source code for the tool resides, and any dependencies on other BrainGlobe packages.

Packages are listed top to bottom based on the number of brainglobe dependencies they posses, IE packages appear earlier in the list if they appear _lower down_ in the BrainGlobe dependency tree.

[`napari`](https://napari.org/stable/) is external to BrainGlobe, but is included in the dependency lists to emphasise BrainGlobe plugins for `napari`.

![Interdependency graph for BrainGlobe tools](assets/BrainGlobe-dependencies.svg)

----
----

## `bg-space`

[Repository](https://github.com/brainglobe/bg-space)

Provides a neat way of defining an anatomical space, and of operating stacks and point transformations between spaces.

## `cellfinder-core`

[Repository](https://github.com/brainglobe/cellfinder-core)

This package implements the cell detection algorithm from Tyson, Rousseau & Niedworok et al. (2021) without any dependency on data type (i.e. it can be used outside of whole-brain microscopy).

## `imio`

[Repository](https://github.com/brainglobe/imio)

The aim of imio is to be a lightweight image loading library for the file types supported by cellfinder, and brainreg.

----
----

## `bg-atlasapi`

[Repository](https://github.com/brainglobe/bg-atlasapi/)

The brainglobe atlas API (BG-AtlasAPI) provides a common interface for programmers to download and process brain atlas data from multiple sources.

Dependencies:
- [bg-space](#bg-space) >= 0.5.0

----
----

## `bg-atlasgen`

[Repository](https://github.com/brainglobe/bg-atlasgen)

Utilities and scripts for the generation of cleaned-up data for the bg-atlasapi module.

Dependencies:
- [`bg-atlasapi`](#bg-atlasapi)
- [`imio`](#imio)

## `brainglobe-napari`

[Repository](https://github.com/brainglobe/brainglobe-napari)

Napari plugin for [bg-atlasapi](#bg-atlasapi). Note that repository README uses the name "brainglobe" for "bg-atlasapi" due to a historical renaming.

Dependencies:
- [`bg-atlasapi`](#bg-atlasapi)

## `brainglobe-napari-io`

[Repository](https://github.com/brainglobe/brainglobe-napari-io)

Napari plugin for visualising [cellfinder](#cellfinder) and [brainreg](#brainreg) results.

Dependencies:
- [`bg-atlasapi`](#bg-atlasapi)
- [`bg-space`](#bg-space)
- `napari`

## `morphapi`

[Repository](https://github.com/brainglobe/morphapi)

Morphapi is a lightweight python package for downloading neurons morphological reconstructions from publicly available datasets.

Dependencies:
- [`bg-atlasapi`](#bg-atlasapi)

----
----

## `brainreg-segment`

[Repository](https://github.com/brainglobe/brainreg-segment)

`brainreg-segment` is a companion to [`brainreg`](#brainreg) allowing manual segmentation of regions/objects within the brain (e.g. injection sites, probes etc.) allowing for automated analysis of brain region distribution, and visualisation (e.g. in [`brainrender`](#brainrender)).

- [`brainglobe-napari-io`](#brainglobe-napari-io)
- [`imio`](#imio)
- `napari`

## `brainrender`

[Repository](https://github.com/brainglobe/brainrender)

`brainrender` is a python package for the visualization of three dimensional neuro-anatomical data. It can be used to render data from publicly available data set (e.g. Allen Brain atlas) as well as user generated experimental data. The goal of brainrender is to facilitate the exploration and dissemination of neuro-anatomical data by providing a user-friendly platform to create high-quality 3D renderings.

Dependencies:
- [`morphapi`](#morphapi) >=0.1.3.0
- [`bg-atlasapi`](#bg-atlasapi) >=1.0.0

## `cellfinder-napari`

[Repository](https://github.com/brainglobe/cellfinder-napari)

`cellfinder-napari` is a front-end to [`cellfinder-core`](#cellfinder-core) to allow ease of use within the `napari` multidimensional image viewer. For more details on this approach, please see Tyson, Rousseau & Niedworok et al. (2021). This algorithm can also be used within the original cellfinder software for whole-brain microscopy analysis.

Dependencies:
- [`brainglobe-napari-io`](#brainglobe-napari-io)
- [`cellfinder-core`](#cellfinder-core) >=0.3
- `napari`

----
----

## `bg-heatmaps`

[Repository](https://github.com/brainglobe/bg-heatmaps)

Dependencies:
- [`brainrender`](#brainrender)

Rendering heatmaps with brainrender.

## `brainreg`

[Repository](https://github.com/brainglobe/brainreg)

`brainreg` is an update to `amap` (itself a port of the original Java software) to include multiple registration backends, and to support the many atlases provided by [`bg-atlasapi`](#bg-atlasapi).

Dependencies:
- [`bg-atlasapi`](#bg-atlasapi)
- [`imio`](#imio)

Additionally, this package used to be able to be installed with an optional `napari` dependency.
In which case, the only dependencies are:
- [brainglobe-napari](#brainglobe-napari)
- [brainreg-segment](#brainreg-segment) >=0.0.2

since the packages above are included in these packages.

## `cellfinder-visualize`

[Repository](https://github.com/brainglobe/cellfinder-visualize)

`cellfinder-visualize` is a tool for post-cellfinder data visualisation and analysis.

Dependencies:
- [`brainrender`](#brainrender)

----
----

## `brainreg-napari`

[Repository](https://github.com/brainglobe/brainreg-napari)

Napari plugin to run [`brainreg`](#brainreg).

Dependencies:
- [`brainreg`](#brainreg)

## `cellfinder`

[Repository](https://github.com/brainglobe/cellfinder)

Whole-brain cell detection, registration and analysis.

Dependencies:
- [`brainreg`](#brainreg)
- [`cellfinder-napari`](#cellfinder-napari) (with [`cellfinder-core`](#cellfinder-core) >=0.2.4)
