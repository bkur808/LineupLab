import requests

# Team class
class Team:
    def __init__(self, id, abbreviation, city, conference, division, full_name, name):
        self.id = id
        self.abbreviation = abbreviation
        self.city = city
        self.conference = conference
        self.division = division
        self.full_name = full_name
        self.name = name

    def __str__(self):
        return (f"Team ID: {self.id}\n"
                f"Abbreviation: {self.abbreviation}\n"
                f"City: {self.city}\n"
                f"Conference: {self.conference}\n"
                f"Division: {self.division}\n"
                f"Full Name: {self.full_name}\n"
                f"Name: {self.name}\n")

# Fetch teams from API
BASE_URL = "https://api.balldontlie.io/v1"
API_KEY = "7335c93f-9e28-4d39-9fe5-6afa585ed52f"

headers = {"Authorization": API_KEY}
response = requests.get(f"{BASE_URL}/teams", headers=headers)

# Parse response
if response.status_code == 200:
    teams_data = response.json()["data"]  # Extract 'data' key
    teams = []

    for team_dict in teams_data:  # Avoid naming conflict
        team_obj = Team(
            id=team_dict["id"],
            abbreviation=team_dict["abbreviation"],
            city=team_dict["city"],
            conference=team_dict["conference"],
            division=team_dict["division"],
            full_name=team_dict["full_name"],
            name=team_dict["name"]
        )
        teams.append(team_obj)

    for team in teams:
        print(team)
        print("-" * 40)
else:
    print("Error:", response.status_code, response.text)
