import requests
import csv

# Player class
class Player:
    def __init__(self, id, first_name, last_name, position, team_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.team_name = team_name

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

# Write players to CSV
def write_to_csv(players, filename):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        # Write header row
        writer.writerow(["Player ID", "First Name", "Last Name", "Position", "Team Name"])
        # Write player data
        for player in players:
            writer.writerow([player.id, player.first_name, player.last_name, player.position, player.team_name])

# Main script
API_KEY = "7335c93f-9e28-4d39-9fe5-6afa585ed52f"
players = fetch_players(API_KEY)
write_to_csv(players, "players.csv")

print("Player data saved to players.csv")
