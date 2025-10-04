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
neighbours = []

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

