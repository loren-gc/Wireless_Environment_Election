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
neighbours_amount = 0
process_neighbours = None

election = None
coordinator_id = None
ELECTION_WAIT_TIME = 5

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
    global process_id, server_port, process_capacity, process_neighbours, neighbours_amount, election
    process_id = program_process_id
    server_port = process_id+BASE_PORT
    process_capacity = capacity
    process_neighbours = neighbours
    neighbours_amount = len(neighbours)
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
def send_ack(destiny_process_id):
    global election
    with lock:
        capacity = election.getCapacity()
        election_id = election.getElectionId()
    ack_message = {
        'type': Message.ACK,
        'election_id': election_id
        'capacity': capacity
    }
    payload = json.dumps(ack_message).encode("utf-8")
    destiny_port = BASE_PORT+destiny_process_id
    send_payload(payload, destiny_port)

def propagate_election(election_message):
    global process_id, election, process_neighbours
    election_message["process_id"] = process_id
    payload = json.dumps(election_message).encode("utf-8")
    current_parent = election.getParent()
    for neighbour in process_neighbours:
        if neighbour != current_parent:
            send_payload(payload, BASE_PORT+neighbour)

def handle_election(election_message):
    # Check if theres another election with higher election_id occurring
    # check if the incoming election message corresponds to the current election
    # discard the election with lower priority
    global election, process_id, neighbours_amount
    with lock:
        election.increaseAckCounter()
        if (not election.isInElection()) or (election.isInElection() and election.getElectionId() < election_message["election_id"]):
            election.resetAckCounter()
            election.increaseAckCounter()
            election.update(election_message["election_id"], election_message["process_id"], True, process_capacity)
            election_message["process_id"] = process_id
            propagate_election(election_message)
        elif election.isInElection() and election.getElectionId() == election_message["election_id"]:
            send_ack(election_message["process_id"])
        if election.getAckCounter() == nieghbours_amount:
            send_ack(election.getParent())

def handle_ack(ack_message):
    # check if the ack corresponds to the current election
    # update the election capacity if necessary
    # check ackCounter
    global election, neighbours_amount
    with lock:
        if ack_message["election_id"] != election.getElectionId():
            return
        if ack_message["cpacity"] > election.getCapacity():
            election.putCapacity(ack_message["capacity"])
        if election.getAckCounter() == neighbours_amount:
            send_ack(election.getCapacity())

def handle_coordinator(message):
    # change the coordinator
    # reset the election object
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
def create_election_message(election_id):
    global process_id, election, process_capacity
    election.update(election_id, process_id, True, process_capacity)
    election_message = {
        'type': Message.ELECTION,
        'election_id': election_id,
        'process_id': process_id
    }
    return election_message

def client():
    global process_id, election, process_neighbours, process_capacity
    while True:
        start_election = input("\nPress 'y' if you want to start an election!!\n")
        if start_election == 'y':
            with lock:
                # If there ISN'T another election with higher election_id occurring:
                # send the election to all the neighbours;
                # update the election object with the current process infos
                election_id = int(time.time() * 1000)
                if (not election.isInElection()) or (election_id > election.getElectionId()):
                    election_message = create_election_message(election_id)
                    propagate_election(election_message)
        election.test()
        time.sleep(ELECTION_WAIT_TIME)

