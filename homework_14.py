# Football Team Managmenet System

class FootballTeam:
    
    def __init__(self, team_name, coach):
        self.team_name = team_name
        self.coach = coach
        self.players = []
    
    # 1. მოთამაშის დამატება
    def add_player(self, name, position, shirt_number, age, nationality):
        
        player_dict = {
            "name" : name,
            "position" : position,
            "shirt_number" : shirt_number,
            "age" : age,
            "nationality" : nationality
        }
        
        self.players.append(player_dict)
    
    # 2. მოთამაშის წაშლა
    def del_player(self, shirt_number):
        for player in self.players:
            if player["shirt_number"] == shirt_number:
                self.players.remove(player)
                print(f'{player["name"]} has successfuly been deleted. ')
                return
            
        print(f'player with number {shirt_number} not found.')

    # 3. მოთამაშის ინფორმაციის განახლება
    def player_update(self, shirt_number, **kwargs):
        for player in self.players:
            if player["shirt_number"] == shirt_number:
                player.update(kwargs)
                print(f"{player["name"]}'s data has been updated!")
                return
    
    # 4. კლუბის ინფორმაციის ჩვენება
    def club_info(self):
        print(f'Club name - {self.team_name}\nCoach - {self.coach}\n')
        player_list = [player["name"] for player in self.players]
        print(f'Player list: {player_list}')



    # 5. მოთამაშის ინფორმაციის ჩვენება 
    def player_info(self, shirt_number):
        for player in self.players:
            if player["shirt_number"] == shirt_number:
                print(f"Player number {player['shirt_number']} information: ")
                print(f"Name: {player['name']}")
                print(f"Position: {player['position']}")
                print(f"Age: {player['age']}")
                print(f"Nationality: {player['nationality']}")
                
                
                for key, value in player.items():
                    if key not in ["name", "position", "shirt_number", "age", "nationality"]:
                        print(f"{key}: {value}")


milan = FootballTeam("AC Milan","Ruben Amorim")

milan.add_player("Rafael Leao", "Forward", 10, 27, "Portugal")
milan.add_player("Christian Pulisic", "Midfielder", 11, 27, "USA")
milan.add_player("Matteo Gabbia", "Defender", 46, 26, "Italy")

milan.club_info()

milan.player_info(10)


# milan.player_update(10, goals=7, Height=191, weight=80)

# milan.del_player(46)

# milan.club_info()

