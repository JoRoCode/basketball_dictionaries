

# Set up a new file and add the Player class with the given constructor
# Challenge 1: Update the constructor to accept a dictionary (player) as an argument and set the attributes using the dictionary


class Player:
    
    team_list = []
    
    
    def __init__(self, data):
        self.name = data['name']
        self.age = data['age']
        self.position = data['position']
        self.team = data['team']
        Player.team_list.append(self)
    

# Ninja Bonus: Add an @class method called get_team(cls, team_list) that, given a list of dictionaries populates and returns a new list of Player objects.
    @classmethod
    def get_team(cls,team_list):
        

        new_team = []
        for player in players:
            new_team.append(player)
        print(new_team)
        return new_team
            
# Complete challenge 2: Create 3 instances of the Player class using the given dictionaries

Kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    }

Jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    }

Kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32, 
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    }

Damian = {
    	"name": "Damian Lillard", 
    	"age":33, 
        "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    }

Joel = {
    	"name": "Joel Embiid", 
    	"age":32, 
        "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    }

Bob = {
    	"name": "Bob Sagget", 
    	"age":67, 
    	"position": "Team Comedian", 
    	"team": "Denver Nuggetsa"
    }


player_kevin = Player(Kevin)
player_jason = Player(Jason)
player_kyrie = Player(Kyrie)
player_damian = Player(Damian)
player_jole = Player(Joel)
player_bob = Player(Bob)

players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33, "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32, "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
    	"name": "", 
    	"age":16, 
    	"position": "P", 
    	"team": "en"
    }
]

# Complete challenge 3: Populate a new list with Player instances from the list of players.

print(player_bob.name)
print(player_kevin.age)
print(player_jason.position)
print(player_kyrie.team)
print(Player.team_list)
print(Player.get_team(players))



