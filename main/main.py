import numpy as np
import labels_manager
import sys
import argparse

sys.path.append('/home/ferraris/test_cluster/simple_cluster_test')  # code working directory

from bruker2nifti import study_converter
from subordinate.auxiliary import say_hello


parser = argparse.ArgumentParser()

parser.add_argument('-i',
                    dest='str_input',
                    type=str,
                    required=True)

args = parser.parse_args()

msg = say_hello()

f = open('../output_{}.txt'.format(args.str_input), 'w+')
f.writelines(args.str_input + '\n')
f.writelines(msg + '\n')
f.writelines(study_converter.__file__ + '\n')
f.writelines(labels_manager.__file__ + '\n')
f.writelines(str(np.random.randn()) + '\n')
f.close()

