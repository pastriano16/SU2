# Setup

A flat plate with a temporally varying surface temperature is analyzed in time domain. A circular domain has been meshed as shown below.
![alt text](https://github.com/pastriano16/SU2/blob/master/assignments/Task3/img/mesh_domain.png?raw=true)

The plate is situated at the center of the mesh as shown.
![alt text](https://github.com/pastriano16/SU2/blob/master/assignments/Task3/img/mes_flat_plate.png?raw=true)

The mesh considered is a standard test-case for SU2. A python wrapper is used for customizing the temporal boundary condition of the surface. 

# Configuration Options

Modelling is done for compressible conditions due to temperature variations. The Prandtl number for thermal conductivity is taken to be constant and an ideal gas equation of state is assumed for flowing air. The weighted least-squares model has been used for convergence along with Euler-Implicit discretization for time stepping.

# Convergence History

The simulation is converged on a maximum residual of 10^-6, although it is not immediatelyclear which parameter the residual is calculated on. A fixed CFL number of 7 has been used for the entire mesh. The convergence of various quantities has been plotted below 
# Results

The variation of the temperatrure with time near the surface is shown below : 
![alt text](https://github.com/pastriano16/SU2/blob/master/assignments/Task3/img/temperature.gif?raw=true)

The variation of the density with time near the surface :
![alt text](https://github.com/pastriano16/SU2/blob/master/assignments/Task3/img/density.gif?raw=true)
The variation of the turbulent KE with time near the surface:
![alt text](https://github.com/pastriano16/SU2/blob/master/assignments/Task3/img/turb_KE.gif?raw=true)

The time variation of heat flux from the surface (two values at each x-position denote upper and lower surfaces):  
![alt text](https://github.com/pastriano16/SU2/blob/master/assignments/Task3/img/heat_flux.gif?raw=true)

The values of density and heatflux are high near the ends as we have a stagnation point for the flow there, thus advection of heat is low
