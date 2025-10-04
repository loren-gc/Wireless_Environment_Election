class Election:
    def __init__(self, election_id, leader, parent, concluded, neighbours, capacity):
        self.update(election_id, leader, parent, concluded, neighbours, capacity)
    
    def update(self, election_id, leader, parent, concluded, neighbours, capacity):
        self._put_election_id(election_id)
        self._put_leader(leader)
        self._put_parent(parent)
        self._put_concluded(concluded)
        self._put_neighbours(neighbours)
        self._put_neighbours_amount(neighbours)
        self._put_capacity(capacity)
    
    def _put_election_id(self, election_id):
        self._election_id = election_id

    def _put_leader(self, leader):
        self._leader = leader
        
    def _put_parent(self, parent):
        self._parent = parent
        
    def _put_concluded(self, concluded):
        self._concluded = concluded
        
    def _put_neighbours(self, neighbours):
        self._neighbours = neighbours
    
    def _put_neighbours_amount(self, neighbours):
        if neighbours == None:
            self._neighbours_amount = 0
        else:
            self._neighbours_amount = len(neighbours)
    
    def _put_capacity(self, capacity):
        self._capacity = capacity
    
    def get_election_id(self):
        return self._election_id
    
    def get_leader(self):
        return self._leader
    
    def get_parent(self):
        return self._parent
    
    def get_concluded(self):
        return self._concluded
    
    def get_neighbours(self):
        return self._neighbours
    
    def get_neighbours_index(self, index):
        return self._neighbours[index]
    
    def get_neighbours_amount(self):
        return self._neighbours_amount
