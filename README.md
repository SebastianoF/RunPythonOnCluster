### RunPythonOnCluster

Simple skeleton to interface python code and the cluster, submitting python code with nohup and qsub command.
Run with 
```
nohup ./qsub_call.sh
```
And check the job submission status with  
```
qstat
```
Set the appropriate path to the python interpreter on run_python.sh.
Add extra libraries installed on your python interpreter in the main - some example are 
commented - to check if they exists and are callable.

#### Thanks
Thansk to Tristan Clark (CS UCL) for the help!