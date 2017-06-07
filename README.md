### PythonOnCluster

Simple skeleton to interface python code and the cluster, submitting python code with nohup and qsub command.
Run with 
```
nohup ./main_runner.sh
```
And check the job submission status with  
```
qstat
```
Set the appropriate path to the python interpreter on run_python.sh.
Add extra libraries installed on your python interpreter in the main - some example are 
commented - to check if they exists and are callable.

#### Structure
+ **main/main.py** is the python module that we want to run on the cluster.
+ **run_python.sh** select the python interpreter on the cluster and run the main python function. 
It is called by qsub_cell.sh
+ **qsub_cell.sh** is called by main_runner.py and it submits the code in run_python.py to the cluster.
+ **main_runner.py** call different qsub_cell.sh that are submitted to different nodes with the selected parsed parameters.


