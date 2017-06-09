#!/bin/bash

#
# nohup ./qsub_call.sh

# Add here paths to required libraries:
export PATH=/share/apps/fsl-5.0.8/bin/:$PATH

qsub parameters.qsub.sh
