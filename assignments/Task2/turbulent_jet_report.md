<p align="center">
<img width="250" height="154" src="Docs/logoSU2small.png">
</p>


# Setup

A steady axisymmetric wall jet is analyzed at turbulent flow conditions with the geometry as given below :

![alt text](https://github.com/pastriano16/SU2/blob/assignments/Task2/img/setup.png?raw=true)

The design resembles a Glauert Wall Jet (1956) and the simulated results have been compared with experimental results from Fukushima et. al. (2000). A 2D domain of 6m * 2.5m is considered as the grid for computational efficiency as the results can be extended axially w.r.t x axis for 3D results. The radius of the inlet is 25cm which is fairly large compared to the domain and hence the virtual origin for any cross section analysis would require a large adjustment. However, the effect of the origin in this test scenario is ignored as we only demostrate the qualitative similarity of the results. Triangular grids have been used throughout which have been made finer near the inlet of the jet. The velocity of the jet is 100 m/s thus Reynolds number is of the order of 10^6.

# Configuration Options

Modelling is done for incompressible flow conditions using RANS. The turbulent viscosity is modelled with SST due to it's compatibility with velocity inlet conditions. The top of the domain and the outlet have been modelled as free stream and the bottom of the domain as the axisymmetry axis. The spatial gradients have been discretized using Green-Gauss scheme and the monotonic upwind scheme is used for conservation laws.

# Convergence History

The simulation is converged on the residual of rms-pressure with a threshold of 10^-6. The convergence criteria can be refined but it leads to larger iteration number requirements. A CFL number of 50 has been used for the simulation which is permissable as implicit numerical methods are used. The convergence of various quantities has been plotted below : 

# Comparison with Experimental Values

![alt text](https://github.com/pastriano16/SU2/blob/assignments/Task2/img/flowsurface.png?raw=true)
![alt text](https://github.com/pastriano16/SU2/blob/assignments/Task2/img/velocity.png?raw=true)
![alt text](https://github.com/pastriano16/SU2/blob/assignments/Task2/img/turb_KE.png?raw=true)




Continuous Integration:<br/>
[![Regression Testing](https://github.com/su2code/SU2/workflows/Regression%20Testing/badge.svg?branch=develop)](https://github.com/su2code/SU2/actions)
[![Release](https://github.com/su2code/SU2/workflows/Release%20Management/badge.svg?branch=develop)](https://github.com/su2code/SU2/actions)

Code Quality:<br/>
[![CodeFactor](https://www.codefactor.io/repository/github/su2code/su2/badge)](https://www.codefactor.io/repository/github/su2code/su2)

# SU2 Introduction

SU2 is a suite of open-source software tools written in C++ for the numerical solution of partial differential equations (PDE) and performing PDE constrained optimization.

The primary applications are computational fluid dynamics and aerodynamic shape optimization, but has been extended to treat more general equations such as electrodynamics and chemically reacting flows.

You will find more information and the latest news in:

- SU2 Home Page: <https://su2code.github.io>
- GitHub repository: <https://github.com/su2code>
- CFD Online: <http://www.cfd-online.com/Forums/su2/>
- Twitter: <https://twitter.com/su2code>
- Facebook: <https://www.facebook.com/su2code>

# SU2 Installation

## Precompiled binaries for Linux, MacOS, Windows

You can find precompiled binaries of the latest version on our [download page](https://su2code.github.io/download.html) or under [releases](https://github.com/su2code/SU2/releases).

## Build SU2

The build system of SU2 is based on a combination of [meson](http://mesonbuild.com/) (as the front-end) and [ninja](https://ninja-build.org/) (as the back-end). Meson is an open source build system meant to be both extremely fast, and, even more importantly, as user friendly as possible. Ninja is a small low-level build system with a focus on speed.

Short summary of the minimal requirements:

- C/C++ compiler
- Python 3

**Note:** all other necessary build tools and dependencies are shipped with the source code or are downloaded automatically.

If you have these tools installed, you can create a configuration using the `meson.py` found in the root source code folder:

```
./meson.py build
```

Use `ninja` to compile and install the code

```
./ninja -C build install
```

For more information on how to install and build SU2 on Linux, MacOS or Windows, have a look at the [documentation](https://su2code.github.io/docs_v7/).

## SU2 Path setup

When installation is complete, please be sure to add the `$SU2_HOME` and `$SU2_RUN` environment variables, and update your `$PATH` with `$SU2_RUN`.

For example, add these lines to your `.bashrc` file:

```
export SU2_RUN="your_prefix/bin"
export SU2_HOME="/path/to/SU2vX.X.X/"
export PATH=$PATH:$SU2_RUN
export PYTHONPATH=$SU2_RUN:$PYTHONPATH
```

`$SU2_RUN` should point to the folder where all binaries and python scripts were installed. This is the prefix you set with the --prefix option to meson. Note that the bin/ directory is automatically added to your prefix path.

`$SU2_HOME` should point to the root directory of the source code distribution, i.e., `/path/to/SU2vX.X.X/`.

Thanks for building, and happy optimizing!

- The SU2 Development Team

# SU2 Developers

We follow the popular "GitFlow" branching model for scalable development. In the SU2 repository, the master branch represents the latest stable major or minor release (7.0, 6.2.0, etc.), it should only be modified during version releases. Work that is staged for release is put into the develop branch via Pull Requests on GitHub from various "feature" branches where folks do their day-to-day work on the code. At release time, the work that has been merged into the develop branch is pushed to the master branch and tagged as a release.

SU2 is being developed by individuals and organized teams all around the world.

A list of current contributors can be found in the AUTHORS.md file.

## Documentation

Code documentation can be generated by calling doxygen from the root of the project, then open Docs/html/index.html in a browser to consult the documentation.