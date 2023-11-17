import argparse
import time
import random

# Construct the argument parser
ap = argparse.ArgumentParser()

# Add the arguments to the parser
ap.add_argument("-s", "--string", required=False,
   help="String to process")

args = vars(ap.parse_args())
my_str = None
if(args['string'] is not None):
	my_str = args['string']
else:
	my_str = input()

random_sleep = random.uniform(0.020, 0.030)
time.sleep(0.020)

# Reversed String
print(my_str[::-1])
