# Lorenzo Grippo Chiachio - 823917
# João Vitor Seiji - 822767

import socket
import threading
import queue
import json
import time
from enum import IntEnum
from Election import *

################################################## CONSTANTS ##################################################
lock = threading.Lock()

# Constants imported from the process
process_id = 0
server_port = 0
process_capacity = 0
process_neighbours = None

election = None
ELECTION_WAIT_TIME = 5
leader = None

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
    global process_id, server_port, process_capacity, process_neighbours, election
    process_id = program_process_id
    server_port = process_id+BASE_PORT
    process_capacity = capacity
    process_neighbours = neighbours
    election = Election(None, None, False, process_capacity)
    election.test()
    
def send_payload(payload, destiny_port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((GENERAL_ADDRESS, destiny_port))
        s.sendall(payload)
        s.close()
    except:
        pass

#################################################### SERVER
def propagate_election(election_message):
    global process_id, process_neighbours
    election_message["process_id"] = process_id
    payload = json.dumps(election_message).encode("utf-8")
    for neighbour in process_neighbours:
        send_payload(payload, BASE_PORT+neighbour)

def handle_election(message):
    global election
    # Check if theres another election with higher election_id occurring
    # discard the election with lower priority
    global election
    if election.isInElection() and election.getElectionId() < message["election_id"]:
            election.update(message["election_id"], message["process_id"], True, process_capacity)
            propagate_election(message)
    elif not election.isInElection(): # Not in election
        election.update(message["election_id"], message["process_id"], True, process_capacity)
        propagate_election(message)

def handle_ack(message):
    # check ackCounter
    print("")

def handle_coordinator(message):
    # change the coordinator
    print("")

def handle_message(message):
    t = message["type"]
    if t == Message.ELECTION:
        handle_election(messsage)
    elif t == Message.ACK:
        handle_ack(message)
    else:
        handle_coordinator(message)

def handle_client(conn, addr):
    try:
        data = conn.recv(1024)
        message = json.loads(data.decode("utf-8"))
        handle_message(message)
    except json.JSONDecodeError:
        print(f"[{addr}] Error: Invalid JSON!")
    finally:
        conn.close()

def server():
    global server_port, SERVER_IP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SERVER_IP, server_port))
    server.listen()
    while True:
        conn, addr = server.accept()
        # thread to handle the client:
        thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
        thread.start()

#################################################### CLIENT
def client():
    global process_id, election, process_neighbours, process_capacity
    while True:
        start_election = input("\nPress 'y' if you want to start an election!!\n")
        if start_election == 'y':
            with lock: # UPDATE THE ELECTION OBJECT WITH THE CURRENT PROCESS INFOS
                print("hey")
                # Check if theres another election with higher election_id occurring
                # if not, send the election to all the neighbours
                
                #election_id = int(time.time() * 1000)
                #election.update(election_id, process_id, False, process_capacity)
            #election_test()
        time.sleep(ELECTION_WAIT_TIME)

