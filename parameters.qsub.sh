date
hostname

#$ -l h_rt=00:01:00
#$ -l tmem=2G
#$ -l h_vmem=2G
#$ -N "SimpleTest"
#$ -S /bin/bash
#$ -cwd
#$ -t 1-10
#$ -e ../z_output/
#$ -o ../z_output/

MYSUBJECT=`sed -n ${SGE_TASK_ID}p job_parameters.txt`

export PATH=/share/apps/fsl-5.0.8/bin/:${PATH}
export PATH=/home/ferraris/software_lib/NiftyFit2/niftyfit-build/fit-apps/:${PATH}
export LD_LIBRARY_PATH=/share/apps/cmic/NiftyMIDAS/bin/:${LD_LIBRARY_PATH}

EXEC=/home/ferraris/py_venvs/v2/bin/python
CALLER=main/main.py

echo $EXEC $CALLER -i $MYSUBJECT

$EXEC $CALLER -i $MYSUBJECT
