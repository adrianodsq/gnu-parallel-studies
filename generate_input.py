import random
import string
import argparse
import time
import random

DESIRED_ELEMENTS = 100
STRING_LENGTH = 20

def should_run_serial(args):
	return args['total'] is not None

letters = string.ascii_uppercase
def generate_random_string(desired_length):
    # choose from all lowercase letter
    result_str = ''.join(random.choice(letters) for i in range(desired_length))
    random_sleep = random.uniform(0.020, 0.060)
    time.sleep(0.020)
    return result_str


# Construct the argument parser
ap = argparse.ArgumentParser()

# Add the arguments to the parser
ap.add_argument("-i", "--index", required=False,
   help="Index of Chunk to process")
   
ap.add_argument("-t", "--total", required=False,
   help="Total of desired elements")

args = vars(ap.parse_args())

# Se passou argumentos para rodar serial - uma execucao gera todos os elementos
if(should_run_serial(args)):
	desired_total_size = int(args['total'])
	for i in range(desired_total_size):
		curr_str = str(i).rjust(3, "0") + generate_random_string(17)
		print(f'{curr_str}')
# Senao roda em modo indexado
else:
	base_multiplier = int(args['index'])
	initial_counter = base_multiplier * DESIRED_ELEMENTS
	# Range is end-exclusive
	for i in range(DESIRED_ELEMENTS):
		curr_val = initial_counter + i
		curr_str = str(curr_val).rjust(3, "0") + generate_random_string(17)
		print(f'{curr_str}')
