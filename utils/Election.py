# Lorenzo Grippo Chiachio - 823917
# João Vitor Seiji - 822767

class Election:
    def __init__(self, electionId, parent, inElection, capacity, capacityOwner):
        self._ackCounter = 0
        self.update(electionId, parent, inElection, capacity, capacityOwner)
 
#################################################### PUTS
    def putElectionId(self, election_id):
        self._electionId = election_id
        
    def putParent(self, parent):
        self._parent = parent
        
    def putInElection(self, inElection):
        self._inElection = inElection
    
    def putCapacity(self, capacity):
        self._capacity = capacity
        
    def putCapacityOwner(self, capacityOwner):
        self._capacityOwner = capacityOwner

#################################################### GETS
    def getElectionId(self):
        return self._electionId
    
    def getParent(self):
        return self._parent
        
    def getCapacity(self):
        return self._capacity
        
    def getCapacityOwner(self):
        return self._capacityOwner
        
    def getAckCounter(self):
        return self._ackCounter

#################################################### OTHERS        
    def update(self, electionId, parent, inElection, capacity, capacityOwner):
        self.putElectionId(electionId)
        self.putParent(parent)
        self.putInElection(inElection)
        self.putCapacity(capacity)
        self.putCapacityOwner(capacityOwner)
    
    def reset(self, capacity, capacityOwner):
        self.resetAckCounter()
        self.update(None, None, False, capacity, capacityOwner)
    
    def increaseAckCounter(self):
        self._ackCounter += 1
        
    def resetAckCounter(self):
        self._ackCounter = 0
    
    def isInElection(self):
        return self._inElection

    def test(self): # Procedure to test the election object
        if not self.isInElection():
            print("Not in election!!!")
        else:
            print("Election id = ", self.getElectionId())
            print("Parent id = ", self.getParent)
        print("current max capacity = ", self.getCapacity())
        print("currents capacity owner = ", self.getCapacityOwner())

