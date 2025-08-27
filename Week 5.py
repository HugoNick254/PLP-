class Player:
    #"A class containing some of my favourite basketball players."

    #"Attributes include: name, age, position played, team playing for"

    def __init__(self, name, age, position, team):

        self.name = name 
        self.age = age
        self.position = position
        self.team = team
    

    def get_info(self):
        print(f"This is {self.name}, {self.age} years old, a {self.position} for {self.team}.")


class NBAPlayer(Player):
    #"A class showing the status of the players in relation to the NBA."

    def __init__(self, name, age, position, team, is_active):
            super().__init__(name, age, position, team)
            self.status = "Active" if is_active else "Retired"

    def get_status_info(self):
            return f"{self.name} is currently {self.status}"


player1 = NBAPlayer("Shai Gilgeous-Alexander", "27", "Point Guard", "Oklahoma City Thunder", True)
player2 = NBAPlayer("Nikola Jokic", "30", "Centre", "Denver Nuggets", True)
player3 = NBAPlayer("Kevin Durant", "36", "Small Forward", "Houston Rockets", True)
player4 = NBAPlayer("Carmelo Anthony", "41", "Power Forward", "New York Knicks", False)
player5 = NBAPlayer("Michael Jordan", "62", "Shooting Guard", "Chicago Bulls", False)

print(player1.get_info())
print(player1.get_status_info())

print(player4.get_info())
print(player4.get_status_info())