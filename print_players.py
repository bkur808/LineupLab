import requests

class Player:
    def __init__(self, id, first_name, last_name, position, team_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.team_name = team_name

    def __str__(self):
        return (f"Player ID: {self.id}\n"
                f"Name: {self.first_name} {self.last_name}\n"
                f"Position: {self.position}\n"
                f"Team: {self.team_name}\n")

# Fetch players from API
def fetch_players(api_key):
    BASE_URL = "https://api.balldontlie.io/v1/players"
    headers = {"Authorization": api_key}
    players = []
    page = 1

    while True:
        response = requests.get(BASE_URL, headers=headers, params={"page": page})
        if response.status_code == 200:
            data = response.json()
            players_data = data["data"]
            if not players_data:  # Exit loop if no more players
                break

            # Parse player data into Player objects
            for player_dict in players_data:
                team_name = player_dict["team"]["full_name"] if player_dict["team"] else "Free Agent"
                player_obj = Player(
                    id=player_dict["id"],
                    first_name=player_dict["first_name"],
                    last_name=player_dict["last_name"],
                    position=player_dict["position"],
                    team_name=team_name
                )
                players.append(player_obj)

            # Move to the next page
            page += 1
        else:
            print("Error:", response.status_code, response.text)
            break

    return players

# Your API Key
API_KEY = "7335c93f-9e28-4d39-9fe5-6afa585ed52f"

# Fetch players and print them
players = fetch_players(API_KEY)
for player in players:
    print(player)
    print("-" * 40)

