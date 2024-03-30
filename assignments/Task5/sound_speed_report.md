# Implementation

The volume output and screen/history output were modified by adding a few lines of code to [`CFlowCompOutput.cpp`](https://github.com/pastriano16/SU2/blob/429b7caaafeae12def893018133616ad0efce538/SU2_CFD/src/output/CFlowCompOutput.cpp#L339) (functions changed are: `LoadHistoryData` and `LoadVolumeData`). The file was identified by a traceback from the COutput.cpp class. The flow solution already has the speed of sound calculated in it, which is referenced at every point for Volume Output and at the centerline of the outlet(iPoint=1) for screen output.
The group name is assigned as PRIMITIVE and field_type as RESIDUAL, which is inaccurate but serves the task at hand!

The field names are added to the config file to display them.

# Results

The history output can be viewed [here](https://github.com/pastriano16/SU2/blob/master/assignments/Task5/history.csv).

The nature of the speed of sound throughout the domain is shown below :
![alt text](https://github.com/pastriano16/SU2/blob/master/assignments/Task5/img/sound_speed.png?raw=true)
