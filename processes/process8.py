# Lorenzo Grippo Chiachio - 823917
# João Vitor Seiji - 822767

import threading
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import utils
from utils.utils import environment_setup, server, client

############################################################### CONSTANTS ##############################################################

# process variables
PROCESS_ID = 7
NEIGHBOURS = [2, 4, 8]

################################################################# MAIN #################################################################

if __name__ == "__main__":
    capacity = int(input("Please enter this process' capacity:\n"))
    environment_setup(PROCESS_ID, capacity, NEIGHBOURS)
    # Starting threads:
    thread1 = threading.Thread(target=server)
    thread2 = threading.Thread(target=client)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
