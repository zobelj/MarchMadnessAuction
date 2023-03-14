teams_raw = []
with open("list.txt", "r") as f:
    
    # read in each line
    for line in f.readlines():
        teams_raw.append(line.split("\t"))

def get_id(team):
    return team.lower().replace(" ", "_").replace(".", "")


teams = []

for team in teams_raw:
    # create a string of an object with the team name, owner, and seed
    # example: duke = Team("Duke", "John", 1)

    # create a Team object
    teams.append(f"{get_id(team[0])} = Team(\"{team[0]}\", \"{team[1]}\", \"{team[2].rstrip()}\")")

for team in teams:
    print(team)