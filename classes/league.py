

# DO NOT USE : NOT CURRENTLY IN USE


class League:
    def __init__(self, league_name, hostTeam):
        self.league_name = league_name
        self.teams = [hostTeam]
        self.id = 1 # in the future, this id should be completely unique using db to create id

    def get_name(self): # returns name of league
        return self.league_name
    
    def set_name(self, new_name): # sets new league name
        self.league_name = new_name

    def get_teams(self): # returns array of teams in league
        return self.teams
    
    def get_team_names(self): # returns array of team NAMES in league
        team_names = []
        for team in self.get_teams():
            team_names.append(team.get_name())
        return team_names
    
    def add_team(self, new_team): # adds a new team to the league
        self.teams.append(new_team)

    def sort_teams(self): # sorts teams array from most points to least points (left --> right)
        self.teams.sort(reverse = True, key = lambda team : team.points)

    def get_id(self):
        return self.id