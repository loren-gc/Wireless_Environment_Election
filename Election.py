# Lorenzo Grippo Chiachio - 823917
# João Vitor Seiji - 822767

class Election:
    def __init__(self, electionId, parent, inElection, capacity):
        self._ackCounter = 0
        self.update(electionId, parent, inElection, capacity)
    
    def update(self, electionId, parent, inElection, capacity):
        self._putElectionId(electionId)
        self._putParent(parent)
        self._putInElection(inElection)
        self._putCapacity(capacity)
 
#################################################### PUTS
    def _putElectionId(self, election_id):
        self._electionId = election_id
        
    def _putParent(self, parent):
        self._parent = parent
        
    def _putInElection(self, inElection):
        self._inElection = inElection
    
    def _putCapacity(self, capacity):
        self._capacity = capacity

#################################################### GETS
    def getElectionId(self):
        return self._electionId
    
    def getParent(self):
        return self._parent
        
    def getCapacity(self):
        return self._capacity
        
    def getAckCounter(self):
        return self._ackCounter

#################################################### OTHERS
    def test(self): # Procedure to test the election object
        if not self.isInElection():
            print("Not in election!!!")
        else:
            print("Election id = ", self.getElectionId())
            print("Parent id = ", self.getParent)
        print("current max capacity = ", self.getCapacity())
    
    def increaseAckCounter(self):
        self._ackCounter += 1
        
    def resetAckCounter(self):
        self._ackCounter = 0
    
    def isInElection(self):
        return self._inElection

