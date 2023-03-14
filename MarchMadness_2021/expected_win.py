import pandas as pd
from numpy import random, linspace, var
import matplotlib.pyplot as plt
import seaborn as sns

# initialize database containing kenpom stats
df = pd.read_excel("kp_stats_remaining.xlsx")
df.set_index("Team", inplace=True)
pyth_exponent = 11.5

# convert round to auction points
round_to_points = {8: 4, 4: 5, 2: 10}
# convert team to owner
team_to_owner = {"Michigan": "Devan", "USC": "Devan", "UCLA": "Josh", "Baylor": "Jeremy", "Gonzaga": "Jeremy", "Houston": "Joe"}

# randomly decides a win by >= points, >= 20 points, >= 10 points, or < 10 points
def blowout():
    x = random.rand()
    if(x < 0.01):
        return 3
    elif(x < 0.1):
        return 2
    elif (x < 0.30):
        return 1
    
    return 0

# simulate one game given two teams.
# "force" parameter guarantees team1 (1) or team2 (2) a win, or a true simulation (0)
def sim_game(team1, team2, round, points, force):
    # guarantee team1 win
    if(force == 1):
        team1_win_percentage = 1
        team2_win_percentage = 0

    # guarantee team2 win
    elif(force == 2):
        team1_win_percentage = 0
        team2_win_percentage = 1
        
    # true simulation using team stats
    else:
        team1_adjO = df.loc[team1, 'AdjO']
        team1_adjD = df.loc[team1, 'AdjD']

        team2_adjO = df.loc[team2, 'AdjO']
        team2_adjD = df.loc[team2, 'AdjD']

        away_win_percentage_season = (team1_adjO**pyth_exponent) / ((team1_adjO **pyth_exponent) + (team1_adjD**pyth_exponent))
        home_win_percentage_season = (team2_adjO**pyth_exponent) / ((team2_adjO**pyth_exponent) + (team2_adjD**pyth_exponent)) 

        team1_win_percentage = ((away_win_percentage_season - (away_win_percentage_season * home_win_percentage_season)) / ((away_win_percentage_season + home_win_percentage_season) - (2 * away_win_percentage_season * home_win_percentage_season)))
        team2_win_percentage = ((home_win_percentage_season - (home_win_percentage_season * away_win_percentage_season)) / ((away_win_percentage_season + home_win_percentage_season) - (2 * away_win_percentage_season * home_win_percentage_season)))

    # get seeds of both teams
    team1_seed = df.loc[team1, "Seed"]
    team2_seed = df.loc[team2, "Seed"]

    # decide on team1 or team2 win
    x = random.rand()
    if(x < team1_win_percentage):
        if(team1_seed > team2_seed):
            points[team_to_owner[team1]] += round_to_points[round] + 2 + blowout()
        else:
            points[team_to_owner[team1]] += round_to_points[round] + blowout()
        return team1
    else:
        if(team2_seed > team1_seed):
            points[team_to_owner[team2]] += round_to_points[round] + 2 + blowout()
        else:
            points[team_to_owner[team2]] += round_to_points[round] + blowout()
        return team2

# simulate one tournament
def sim_tournament():

    points = {"Devan": 28, "Jeremy": 30, "Josh": 44, "Justin": 12, "Brant": 18, "Nick": 33, "Joe": 26}

    # Elite Eight
    game1_winner = "Gonzaga"

    # Elite Eight
    game2_winner = "UCLA"
    
    # Final Four
    game3_winner = sim_game("Houston", "Baylor", 4, points, 0)

    # Final Four
    game4_winner = sim_game(game1_winner, game2_winner, 4, points, 0)

    # Championship
    champion = sim_game(game3_winner, game4_winner, 2, points, 0)

    return points

# running total of auction wins and points
num_wins = {"Devan": 0, "Jeremy": 0, "Josh": 0, "Justin": 0, "Brant": 0, "Nick": 0, "Joe": 0}
num_points = {"Devan": 0, "Jeremy": 0, "Josh": 0, "Justin": 0, "Brant": 0, "Nick": 0, "Joe": 0}

# list points scored in each tourney simulation
Devan = []
Jeremy = []
Josh = []
Joe = []

# run sim NUM_SIMS time and keep running total of points and auction wins
def sim_results(NUM_SIMS):
    for _ in range(NUM_SIMS):
        points = sim_tournament()

        Devan.append(points["Devan"])
        Josh.append(points["Josh"])
        Jeremy.append(points["Jeremy"])
        Joe.append(points["Joe"])

        for key in num_points:
            num_points[key] += points[key]

        num_wins[max(points, key=points.get)] += 1

    for key in num_wins:
        num_wins[key] = num_wins[key] * 100 /NUM_SIMS
        num_points[key] /= NUM_SIMS

    print(num_wins)
    print(num_points)

# run simulations many times
sim_results(10000)

# plot density function for owners with non-zero variance
legend_list = []
if(var(Devan)):
    sns.kdeplot(Devan, shade=True)
    legend_list.append("Devan: {0}%".format(num_wins["Devan"]))
if(var(Josh)):
    sns.kdeplot(Josh, shade=True)
    legend_list.append("Josh:     {0}%".format(num_wins["Josh"]))
if(var(Jeremy)):
    sns.kdeplot(Jeremy, shade=True)
    legend_list.append("Jeremy: {0}%".format(num_wins["Jeremy"]))
if(var(Joe)):
    sns.kdeplot(Joe, shade=True)
    legend_list.append("Joe:      {0}%".format(num_wins["Joe"]))

# configure and display plot
plt.title("Expected Points Density Function")
plt.xlabel("Points")
plt.ylabel("Probability")
plt.legend(legend_list)
plt.show()
