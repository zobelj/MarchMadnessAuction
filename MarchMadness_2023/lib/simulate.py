import math
import random

from lib.database import run_query

# constants
pyth_exponent = 11.5
round_to_points = {64: 1, 32: 2, 16: 3, 8: 4, 4: 5, 2: 10, -1: 0}

def sim_game(team1, team2, round, points_dict, points_decided, force):

    # real simulation
    if(len(force) == 0):
        team1_win_percentage_season = (team1.adjO**pyth_exponent) / ((team1.adjO**pyth_exponent) + (team1.adjD**pyth_exponent))
        team2_win_percentage_season = (team2.adjO**pyth_exponent) / ((team2.adjO**pyth_exponent) + (team2.adjD**pyth_exponent)) 

        team1_win_percentage = ((team1_win_percentage_season - (team1_win_percentage_season * team2_win_percentage_season)) / ((team1_win_percentage_season + team2_win_percentage_season) - (2 * team1_win_percentage_season * team2_win_percentage_season)))
        team2_win_percentage = 1 - team1_win_percentage

        # get a random number between 0 and 1
        ran_num = random.random()
        winner = team1 if ran_num < team1_win_percentage else team2
        loser = team2 if winner is team1 else team1
        
        blowout_pts = 0
        if(winner.seed > loser.seed):
            blowout_pts = blowout(winner, loser)
            pts = round_to_points[round] + 2 + blowout_pts
            points_dict[winner.owner] += pts
            winner.pts += pts
        else:
            blowout_pts = blowout(winner, loser)
            pts = round_to_points[round] + blowout_pts
            points_dict[winner.owner] += pts
            winner.pts += pts

    # forced sim
    # 1 for a normal win, 2 for a 10 point win, etc
    # Underdog and round are automatically accounted for!
    else:
        if(force[0] != 0):
            winner = team1
            loser = team2
            force = force[0]
            blowout_pts = force - 1
        else:
            loser = team1
            winner = team2
            force = force[1]
            blowout_pts = force - 1
        
        if(winner.seed > loser.seed):
            points_dict[winner.owner] += round_to_points[round] + 2 + force - 1
            points_decided[winner.owner] += round_to_points[round] + 2 + force - 1
            winner.pts += round_to_points[round] + 2 + force - 1
        else:
            points_dict[winner.owner] += round_to_points[round] + force - 1
            points_decided[winner.owner] += round_to_points[round] + force - 1
            winner.pts += round_to_points[round] + force - 1
    return winner, blowout_pts

# This function is based on a logistic regression model
# developed by Jeremy Frank during the 2023 tournament
def blowout(winner, loser):
    blowout_pts = 0

    ten_pt = 1 / ( 1 + math.exp(-1 * ( -0.3395 - 0.0785 * winner.seed + 0.09093 * loser.seed ) ))
    ten_pct_prob = random.random()

    # < 10 pt win
    if(ten_pct_prob > ten_pt):
        return blowout_pts
    
    blowout_pts += 1
    twenty_pt = 1 / ( 1 + math.exp(-1 * ( -1.5551 - 0.0785 * winner.seed + 0.1107 * loser.seed ) ))
    twenty_pct_prob = random.random()

    # 10-19 pt win
    if(twenty_pct_prob > twenty_pt):
        return blowout_pts
    
    blowout_pts += 1
    thirty_pt = 1 / ( 1 + math.exp(-1 * ( -1.1171 - 0.0551 * winner.seed + 0.0166 * loser.seed ) ))
    thirty_pct_prob = random.random()

    # 20-29 pt win
    if(thirty_pct_prob > thirty_pt):
        return blowout_pts
    
    # 30+ pt win
    blowout_pts += 1

    return blowout_pts


def sim_many_tournaments(num_sims, sim_tournament):
    points_lists = {
        "Devan": [],
        "Jeremy": [],
        "Josh": [],
        "Justin": [],
        "Brant": [],
        "Nick": [],
        "Joe": []
    }

    for _ in range(num_sims):
        if _ % 1000 == 0:
            print(f"Simulating tournament {_} of {num_sims}...")
        points, points_decided = sim_tournament()

        points_lists["Devan"].append(points["Devan"])
        points_lists["Brant"].append(points["Brant"])
        points_lists["Jeremy"].append(points["Jeremy"])
        points_lists["Josh"].append(points["Josh"])
        points_lists["Justin"].append(points["Justin"])
        points_lists["Nick"].append(points["Nick"])
        points_lists["Joe"].append(points["Joe"])

    # get the average points scored by each player from the database
    avg_points = run_query('''SELECT ROUND(AVG(Devan_pts), 2) as Devan_avg_pts,
                        ROUND(AVG(Jeremy_pts), 2) as Jeremy_avg_pts,
                        ROUND(AVG(Josh_pts), 2) as Josh_avg_pts,
                        ROUND(AVG(Justin_pts), 2) as Justin_avg_pts,
                        ROUND(AVG(Nick_pts), 2) as Nick_avg_pts,
                        ROUND(AVG(Joe_pts), 2) as Joe_avg_pts
                    FROM march_madness''', fetch="one")
    
    # convert DB results into python dictionaries
    avg_points = dict(zip(["Devan", "Jeremy", "Josh", "Justin", "Nick", "Joe"], avg_points))

    print("<--- Decided points --->")
    print(points_decided)

    print("<--- Average points scored --->")
    print(avg_points)

    return points_lists

