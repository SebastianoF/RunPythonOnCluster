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

#### Links and tutorials:
+ [sun grid engine for beginners](http://bioinformatics.mdc-berlin.de/intro2UnixandSGE/sun_grid_engine_for_beginners/how_to_submit_a_job_using_qsub.html)
+ [qsub tutorial](https://wikis.nyu.edu/display/NYUHPC/Tutorial+-+Submitting+a+job+using+qsub)

#### Thanks
Thansk to Tristan Clark (CS UCL) for the help!