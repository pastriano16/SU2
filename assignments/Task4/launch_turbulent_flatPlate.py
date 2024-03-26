#!/usr/bin/env python

## \file launch_unsteady_CHT_FlatPlate.py
#  \brief Python script to launch SU2_CFD with customized unsteady boundary conditions using the Python wrapper.
#  \author Amartya Prusty
#  \version 8.0.1 "Harrier"
#
# SU2 Project Website: https://su2code.github.io
#
# The SU2 Project is maintained by the SU2 Foundation
# (http://su2foundation.org)
#
# Copyright 2012-2024, SU2 Contributors (cf. AUTHORS.md)
#
# SU2 is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# SU2 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with SU2. If not, see <http://www.gnu.org/licenses/>.

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

import sys
from optparse import OptionParser	# use a parser for configuration
import pysu2			            # imports the SU2 wrapped module
from math import *

# -------------------------------------------------------------------
#  Main
# -------------------------------------------------------------------

def main():

  # Command line options
  parser=OptionParser()
  parser.add_option("-f", "--file", dest="filename", help="Read config from FILE", metavar="FILE")
  parser.add_option("--parallel", action="store_true",
                    help="Specify if we need to initialize MPI", dest="with_MPI", default=False)

  (options, args) = parser.parse_args()
  options.nDim = int(2)
  options.nZone = int(1)

  # Import mpi4py for parallel run
  if options.with_MPI == True:
    from mpi4py import MPI
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
  else:
    comm = 0
    rank = 0

  # Initialize the corresponding driver of SU2, this includes solver preprocessing
  try:
      SU2Driver = pysu2.CSinglezoneDriver(options.filename, options.nZone, comm);
  except TypeError as exception:
    print('A TypeError occured in pysu2.CDriver : ',exception)
    if options.with_MPI == True:
      print('ERROR : You are trying to initialize MPI with a serial build of the wrapper. Please, remove the --parallel option that is incompatible with a serial build.')
    else:
      print('ERROR : You are trying to launch a computation without initializing MPI but the wrapper has been built in parallel. Please add the --parallel option in order to initialize MPI for the wrapper.')
    return


  MarkerID = None
  MarkerName = 'wall'       # Specified by the user

  # Get all the tags
  MarkerList =  SU2Driver.GetMarkerTags()
  # Get all the markers defined on this rank and their associated indices.
  allMarkerIDs = SU2Driver.GetMarkerIndices()

  #Check if the specified marker exists and if it exists on this rank.
  if MarkerName in MarkerList and MarkerName in allMarkerIDs.keys():
    MarkerID = allMarkerIDs[MarkerName]

  # Number of vertices on the specified marker (per rank).
  nVertex = SU2Driver.GetNumberMarkerNodes(MarkerID) if MarkerID >= 0 else 0
  if nVertex > 0:
    MarkerCoords = SU2Driver.MarkerCoordinates(MarkerID)
    L = 2.0
    for iVertex in range(nVertex):
      x = MarkerCoords(iVertex, 0)
      WallTemp = 273.0 + (x*100.0/L)
      SU2Driver.SetMarkerCustomTemperature(MarkerID, iVertex, WallTemp)
  # Time loop is defined in Python so that we have acces to SU2 functionalities at each time step
  if rank == 0:
    print("\n------------------------------ Begin Solver -----------------------------\n")
  sys.stdout.flush()
  if options.with_MPI == True:
    comm.Barrier()

  
  # Time iteration preprocessing
  SU2Driver.Preprocess(0)
  # Tell the SU2 drive to update the boundary conditions
  SU2Driver.BoundaryConditionsUpdate()
  # Run one time iteration (e.g. dual-time)
  SU2Driver.Run()
  # Postprocess the solver and exit cleanly
  SU2Driver.Postprocess()
  # Update the solver for the next time iteration
  SU2Driver.Update()
  # Monitor the solver and output solution to file if required
  stopCalc = SU2Driver.Monitor(0)
  SU2Driver.Output(0)
  
  # Finalize the solver and exit cleanly.
  SU2Driver.Finalize()


# -------------------------------------------------------------------
#  Run Main Program
# -------------------------------------------------------------------

# this is only accessed if running from command prompt
if __name__ == '__main__':
    main()