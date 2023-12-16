class TeamBoard:
    def __init__(self, team_name):
        self.team_name = team_name
        
        self.id = 1 # in the future, this id should be unique to the team
    
    def get_name(self): # get team name
        return self.team_name
    
    def get_id(self):
        return self.id
    
    

