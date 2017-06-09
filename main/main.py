import os
import sys
import argparse
import subprocess

# Extra libraries specific to the selectd python interpreter
import numpy as np
import labels_manager
from bruker2nifti import study_converter

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(dir_path))  # add the code directory /simple_cluster_test

from subordinate.auxiliary import say_hello


parser = argparse.ArgumentParser()

parser.add_argument('-i',
                    dest='str_input',
                    type=str,
                    required=True)

args = parser.parse_args()

msg = say_hello()

proc = subprocess.Popen('fslreorient2std', stdout=subprocess.PIPE, shell=True)
(msg2, err) = proc.communicate()


f = open('../output_{}.txt'.format(args.str_input), 'w+')
f.writelines(args.str_input + '\n')
f.writelines(msg + '\n')
f.writelines('This is the help of fsl reorient2std: \n')
f.writelines(msg2 + '\n')
f.writelines(study_converter.__file__ + '\n')
f.writelines(labels_manager.__file__ + '\n')
f.writelines(str(np.random.randn()) + '\n')
f.close()

