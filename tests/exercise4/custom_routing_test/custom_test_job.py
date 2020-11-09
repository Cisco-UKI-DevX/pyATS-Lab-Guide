.
# To run the job:
# pyats run job BGP_check_job.py --testbed-file <testbed_file.yaml>
# Description: This job file checks that all BGP neighbors are in Established state
import os

# All run() must be inside a main function
def main(runtime):
    # Find the location of the script in relation to the job file
    custom_test = os.path.join(os.path.dirname(__file__), 
                             'custom_test.py')
    # Execute the testscript
    runtime.tasks.run(testscript=custom_test)
