# Lorenzo Grippo Chiachio - 823917
# João Vitor Seiji - 822767

import socket
import threading
import queue
import json
import time
from enum import IntEnum
import signal
import sys
from Election import *

################################################## CONSTANTS ##################################################
lock = threading.Lock()

# Constants imported from the process
process_id = 0
server_port = 0
process_capacity = 0

PROCESSES_AMOUNT = 10
BASE_PORT = 5050

GENERAL_ADDRESS = "127.0.0.1"
SERVER_IP = "127.0.0.1"

################################################ MESSAGE CLASS ################################################
class Message(IntEnum):
    ELECTION = 1
    ACK = 2
    COORDINATOR = 3

########################################### FUNCTIONS AND PROCEDURES ##########################################
############################ GENERAL PROCEDURES AND FUNCTIONS
def environment_setup(program_process_id, capacity, neighbours):
    global process_id, server_port, process_capacity
    process_id = program_process_id
    server_port = process_id+BASE_PORT
    process_capacity = capacity
    election = Election(None, None, None, False, neighbours, process_capacity)
    print(election.get_neighbours_amount())
    print(election.get_neighbours())
    print(election.get_neighbours_index(1))
    
def send_payload(payload, destiny_port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((GENERAL_ADDRESS, destiny_port))
        s.sendall(payload)
        s.close()
    except:
        pass
