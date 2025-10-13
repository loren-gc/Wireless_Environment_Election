# Wireless_Environment_Election
Implementation of a leader election algorithm for wireless ad hoc networks, discussed in Tanenbaum’s Distributed Systems.

---

## 📘 Overview

Traditional leader election algorithms assume stable topologies and reliable message passing, which are unrealistic in wireless networks.
In this implementation, each process represents a wireless node capable of:

- Initiating an election (sending ELECTION messages).

- Forwarding election messages to its neighbors.

- Acknowledging messages (ACK) to indicate participation.

- Propagating the final coordinator (COORDINATOR) once the best leader is chosen.

- Each node exchanges information with its neighbors to determine which node in the network has the highest capacity, designating it as the new coordinator.

**OBS**: In this implementation, each process capacity and its neighbors are predefined in each processes' code

## 🧩 How It Works

**Election Initiation**
Any node can start an election by broadcasting an ELECTION message to its neighbor processes containing a unique election ID (based on timestamp).

**Tree Formation**
When a node receives an election message for the first time, it records the sender as its parent and forwards the message to its other neighbors.

**Acknowledgment Phase**
Leaf nodes reply to their parents with an ACK containing their own capacity.
Intermediate nodes collect ACKs from their children, compare all received capacities (plus their own), and propagate the highest back to their parent.

**Leader Selection**
When the source node receives all acknowledgments, it determines the node with the highest capacity as the leader and broadcasts this information to all nodes using a COORDINATOR message.

**Concurrent Elections**
If multiple elections occur simultaneously, nodes participate only in the election with the highest election ID and ignore others.

## 📐 Project Structure

    Wireless-Environment-Election/
    │
    ├── utils/
    │   ├── utils.py          # Core logic for message handling, sockets, and election protocol
    │   └── Election.py       # Election class storing election state and related operations
    │
    └── processes/
        ├── process1.py       # Individual process (node) setup
        ├── process2.py
        ├── ...
        └── process10.py

## 🛜 Topology
![Network topology](images/topology.png)

## 🚀 How to run

First, access the processes directory:

```bash
cd processes/
```

Then, use the command to simultaneously run the 10 processes:
```bash
for i in {1..10}; do
    gnome-terminal --title="Process $i" --command="bash -c 'python3 process$i.py --id $i; exec bash'" &
    sleep 0.1
done
```

<p align="center">To start an election, press "y".</p>
<p align="center">You can start more than one election in more than one process!!</p>

