date
hostname

#$ -l h_rt=00:2:00
#$ -l tmem=2G
#$ -l h_vmem=2G
#$ -N "SimpleTest"
#$ -S /bin/bash
#$ -cwd
#$ -t 1-10

MYSUBJECT=`sed -n ${SGE_TASK_ID}p subjects.txt`
# echo text $SGE_TASK_ID
# echo $MYSUBJECT

./run_python.sh $MYSUBJECT
