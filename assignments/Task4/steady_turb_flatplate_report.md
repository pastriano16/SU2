# Setup

A steady turbulent flow is analyzed for a flat plate as shown in the figure below (Source: SU2 Docs) Temperature conditions are varied linearly from the origin of the plate (from 273K to 373K) to study the effect of the advection due to flow on the energy. The python wrapper enables us to customize the temperature boundary condition on the surface. The meshing gets finer as y+ -> 1 to account for the thin turbulent boundary layer. 

![alt text](https://github.com/pastriano16/SU2/blob/master/assignments/Task4/img/turb_plate_mesh_bcs.png?raw=true)

The dimension of the flat plate is 2m and farfield is at 1m from the base of the domain.

# Configuration Options

Modelling is done for a Mach Number of 0.2 using RANS. Freestream temperature is fixed at 300K. Weighted least squares method is used for spatial gradients and an adaptive CFL w.r.t. 100 is used to accomodate for convergence of finer mesh near the wall.

# Convergence History

Convergence is eshtablished against a max threshold of 10^-6 on the rms of density.

# Results

The velocity variation along y is shown below near the turbulent boundary layer at outlet (y-axis is the y-position, x-axis is U(y)): 
![alt text](https://github.com/pastriano16/SU2/blob/master/assignments/Task4/img/U_y.png?raw=true)

The temperature variation along y is shown below near the turbulent boundary layer at outlet (y-axis is the y-position, x-axis is U(y)![alt text](https://github.com/pastriano16/SU2/blob/master/assignments/Task4/img/temperature_y.png?raw=true)

The density variation of fluid at the wall surface (x-axis is x-position):
![alt text](https://github.com/pastriano16/SU2/blob/master/assignments/Task4/img/density.png?raw=true)

The heat flux variation at the surface:
![alt text](https://github.com/pastriano16/SU2/blob/master/assignments/Task4/img/heat_flux.png?raw=true)

The pressure variation at the surface:
![alt text](https://github.com/pastriano16/SU2/blob/master/assignments/Task4/img/pressure_flux.png?raw=true)

We see spikes in the pressure variation near the start and end of the wall, due to the nature of the boundaries. Flow will be decelerated near the start of the wall but accelerated near the end of the wall due to curvature. Thus, using Bernoulli's equation, the nature of pressure will be reversed.