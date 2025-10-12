# Lorenzo Grippo Chiachio - 823917
# João Vitor Seiji - 822767

import threading
from utils import environment_setup, server, client

############################################################### CONSTANTS ##############################################################

# process variables
PROCESS_ID = 2
NEIGHBOURS = [1, 3, 6, 7]

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
