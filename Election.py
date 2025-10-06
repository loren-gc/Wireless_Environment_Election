# Lorenzo Grippo Chiachio - 823917
# João Vitor Seiji - 822767

class Election:
    def __init__(self, electionId, leader, parent, concluded, neighbours, capacity):
        self._neighboursAmount = 0
        self._ackCounter = 0
        self.update(electionId, leader, parent, concluded, neighbours, capacity)
    
    def update(self, electionId, leader, parent, concluded, neighbours, capacity):
        self._putElectionId(electionId)
        self._putLeader(leader)
        self._putParent(parent)
        self._putConcluded(concluded)
        self._putNeighbours(neighbours)
        self._putNeighboursAmount(neighbours)
        self._putCapacity(capacity)
 
#################################################### PUTS
    def _putElectionId(self, election_id):
        self._electionId = election_id

    def _putLeader(self, leader):
        self._leader = leader
        
    def _putParent(self, parent):
        self._parent = parent
        
    def _putConcluded(self, concluded):
        self._concluded = concluded
        
    def _putNeighbours(self, neighbours):
        self._neighbours = neighbours
    
    def _putNeighboursAmount(self, neighbours):
        if neighbours == None:
            self._neighboursAmount = 0
        else:
            self._neighboursAmount = len(neighbours)
    
    def _putCapacity(self, capacity):
        self._capacity = capacity

#################################################### GETS
    def getElectionId(self):
        return self._electionId
    
    def getLeader(self):
        return self._leader
    
    def getParent(self):
        return self._parent
    
    def getNeighbours(self):
        return self._neighbours
    
    def getNeighbour(self, index):
        return self._neighbours[index]
    
    def getNeighboursAmount(self):
        return self._neighboursAmount
        
    def getAckCounter(self):
        return self._ackCounter

#################################################### OTHERS
    def increaseAckCounter(self):
        self._ackCounter += 1
        
    def resetAckCounter(self):
        self._ackCounter = 0
    
    def isConcluded(self):
        return self._concluded

