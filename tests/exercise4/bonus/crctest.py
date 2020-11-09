import os
import argparse

# command line argument parser
# see https://pubhub.devnetcloud.com/media/pyats/docs/easypy/jobfile.html#custom-arguments
parser = argparse.ArgumentParser()
parser.add_argument('--no-parallel-connect',
                    dest = 'p_connect',
                    action='store_false',
                    default = True,
                    help = 'disable connecting to devices in parallel')
parser.add_argument('--crc-threshold',
                    dest = 'crc_threshold',
                    default = 0,
                    type = int,
                    help = 'threshold at which interface CRC will be considered'
                           'fail')

def main(runtime):
    # parse command line arguments
    # only parse arguments we know
    args, _ = parser.parse_known_args()

    # Find the location of the script in relation to the job file
    testscript = os.path.join(os.path.dirname(__file__), 'crctest_script.py')
    
    # run script, pass arguments to script as parameters
    runtime.tasks.run(testscript=testscript,
                      **vars(args))
