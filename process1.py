# Lorenzo Grippo Chiachio - 823917
# João Vitor Seiji - 822767

import threading
from utils import environment_setup, server, client

############################################################### CONSTANTS ##############################################################

# process variables
PROCESS_ID = 0
NEIGHBOURS = [1, 2, 3]
CAPACITY = 10

################################################################# MAIN #################################################################

if __name__ == "__main__":
    environment_setup(PROCESS_ID, CAPACITY, NEIGHBOURS)
    # Starting threads:
    thread1 = threading.Thread(target=server)
    thread2 = threading.Thread(target=client)
    #thread3 = threading.Thread(target=call_election)
    thread1.start()
    thread2.start()
    #thread3.start()
    thread1.join()
    thread2.join()
    #thread3.join()
