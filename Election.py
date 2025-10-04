class Election:
    def __init__(self, election_id, leader, parent):
        self._election_id = election_id
        self._leader = leader
        self._parent = parent
    
    def update(self, election_id, leader, parent):
        self._put_election_id(election_id)
        self._put_leader(leader)
        self._put_parent(parent)
    
    def _put_election_id(self, election_id):
        self._election_id = election_id

    def _put_leader(self, leader):
        self._leader = leader
        
    def _put_parent(self, parent):
        self._parent = parent

    def get_election_id(self):
        return self._election_id
    
    def get_leader(self):
        return self._leader
    
    def get_parent(self):
        return self._parent
