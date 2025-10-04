# Lorenzo Grippo Chiachio - 823917
# João Vitor Seiji - 822767

import threading
from utils import environment_setup

############################################################### CONSTANTS ##############################################################

# process variables
PROCESS_ID = 0
NEIGHBOURS = [1, 2, 3]
CAPACITY = 10

################################################################# MAIN #################################################################

if __name__ == "__main__":
    environment_setup(PROCESS_ID, CAPACITY, NEIGHBOURS)
