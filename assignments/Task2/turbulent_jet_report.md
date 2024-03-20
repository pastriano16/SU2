# Setup

A steady axisymmetric wall jet is analyzed at turbulent flow conditions with the geometry as given below :

![alt text](https://github.com/pastriano16/SU2/blob/master/assignments/Task2/img/setup.png?raw=true)

The design resembles a Glauert Wall Jet (1956) and the simulated results have been compared with experimental results from Fukushima et al. (2000). A 2D domain of 6m * 2.5m is considered as the grid for computational efficiency as the results can be extended axially w.r.t x axis for 3D results. The radius of the inlet is 25cm which is fairly large compared to the domain and hence, the virtual origin for any cross section analysis would require a large adjustment. However, the effect of the origin in this test scenario is ignored as we only demonstrate the qualitative similarity of the results. Triangular grids have been used throughout which have been made finer near the inlet of the jet. The velocity of the jet is 100 m/s; thus Reynolds number is of the order of 10^6.

# Configuration Options

Modelling is done for incompressible flow conditions using RANS. The turbulent viscosity is modelled with SST due to it's compatibility with velocity inlet conditions. The top of the domain and the outlet have been modelled as free stream and the bottom of the domain as the axisymmetry axis. The spatial gradients have been discretized using Green-Gauss scheme and the monotonic upwind scheme is used for conservation laws.

# Convergence History

The simulation is converged on the residual of rms-pressure with a threshold of 10^-6. The convergence criteria can be refined but it leads to larger iteration number requirements. A CFL number of 50 has been used for the simulation, which is permissible as implicit numerical methods are used. The convergence of various quantities has been plotted below : 
![alt text](https://github.com/pastriano16/SU2/blob/master/assignments/Task2/img/convergence.png?raw=true)

# Comparison with Experimental Values

The flow magnitude in the domain is shown below : 
![alt text](https://github.com/pastriano16/SU2/blob/master/assignments/Task2/img/flowsurface.png?raw=true)

The velocity magnitude at a distance of x/d = 50 is plotted below. The trend correlates very well with the experimental plot (see Fig. 4)
![alt text](https://github.com/pastriano16/SU2/blob/master/assignments/Task2/img/velocity.png?raw=true)

The turbulent kinetic energy is also plotted at the same x/d position. It goes to 0 at the centerline and approaches a maxima before the freestream. This also correlates well with the experimental plot of |uv|/U^2 (see Fig. 8)
![alt text](https://github.com/pastriano16/SU2/blob/master/assignments/Task2/img/turb_KE.png?raw=true)

# Issues

The quality of the mesh could be improved near the centerline, where the turbulent statistics matter the most. A finer mesh can give us more accurate results with the gradients normal to the symmetry line. It would also be better to use a quadrilateral mesh to improve the consistency of the numerical scheme, as viscous effects (eddy/shear) would be dominant. The residual threshold can also be improved given enough iterations.
