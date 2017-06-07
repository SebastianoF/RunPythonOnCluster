#!/bin/bash

# This is a single q-sub

echo "submitting a job ${1}"
qsub -l h_rt=00:01:00 -l tmem=1G -l h_vmem=1G -N "job_sj_${1}" -cwd -v SUBJECT=${1} run_python.sh
