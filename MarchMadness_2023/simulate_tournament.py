#!/usr/bin/env python3

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import random, mean, var
import math

# import team objects
from teams import *

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

        winner = random.choice([team1, team2], p=[team1_win_percentage, team2_win_percentage])
        loser = team2 if winner is team1 else team1

        if(winner.seed > loser.seed):
            points_dict[winner.owner] += round_to_points[round] + 2 + blowout(winner, loser)
        else:
            points_dict[winner.owner] += round_to_points[round] + blowout(winner, loser)

    # forced sim
    # 1 for a normal win, 2 for a 10 point win, etc
    # Underdog and round are automatically accounted for!
    else:
        if(force[0] != 0):
            winner = team1
            loser = team2
            force = force[0]
        else:
            loser = team1
            winner = team2
            force = force[1]
        
        if(winner.seed > loser.seed):
            points_dict[winner.owner] += round_to_points[round] + 2 + force - 1
            points_decided[winner.owner] += round_to_points[round] + 2 + force - 1
        else:
            points_dict[winner.owner] += round_to_points[round] + force - 1
            points_decided[winner.owner] += round_to_points[round] + force - 1
    
    return winner

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


#########################################################################################################
headliner = "Gonzaga beats TCU"
i = 53

#########################################################################################################


def sim_tournament():

    points_dict = {"Devan": 0, "Jeremy": 0, "Josh": 0, "Justin": 0, "Brant": 0, "Nick": 0, "Joe": 0}
    points_decided = {"Devan": 0, "Jeremy": 0, "Josh": 0, "Justin": 0, "Brant": 0, "Nick": 0, "Joe": 0}

    # First Four
    # 2023
    mw_firstfour_11    = sim_game(mississippi_state, pittsburgh, -1, points_dict, points_decided, [0,1])
    west_firstfour_11  = sim_game(arizona_state, nevada, -1, points_dict, points_decided, [3, 0])
    east_firstfour_16  = sim_game(texas_southern, fairleigh_dickinson, -1, points_dict, points_decided, [0,3])
    south_firstfour_16 = sim_game(texas_am_corpus_christi, southeast_missouri_state, -1, points_dict, points_decided, [1,0])


    #####  West Region  #####
    # Round of 64
    # 2023
    r64_w_game1 = sim_game(kansas, howard, 64, points_dict, points_decided, [3,0])
    r64_w_game2 = sim_game(arkansas, illinois, 64, points_dict, points_decided, [2,0])
    r64_w_game3 = sim_game(saint_marys, vcu, 64, points_dict, points_decided, [2,0])
    r64_w_game4 = sim_game(connecticut, iona, 64, points_dict, points_decided, [3,0])
    r64_w_game5 = sim_game(tcu, west_firstfour_11, 64, points_dict, points_decided, [1,0])
    r64_w_game6 = sim_game(gonzaga, grand_canyon, 64, points_dict, points_decided, [2,0])
    r64_w_game7 = sim_game(northwestern, boise_state, 64, points_dict, points_decided, [1,0])
    r64_w_game8 = sim_game(ucla, unc_asheville, 64, points_dict, points_decided, [4,0])

    # Round of 32
    r32_w_game1 = sim_game(r64_w_game1, r64_w_game2, 32, points_dict, points_decided, [0,1]) # Kansas vs Arkansas
    r32_w_game2 = sim_game(r64_w_game3, r64_w_game4, 32, points_dict, points_decided, [0,2]) # Saint Mary's vs UConn
    r32_w_game3 = sim_game(r64_w_game5, r64_w_game6, 32, points_dict, points_decided, [0,1]) # TCU vs Gonzaga
    r32_w_game4 = sim_game(r64_w_game7, r64_w_game8, 32, points_dict, points_decided, [0,1]) # Northwestern vs UCLA

    # Sweet 16
    r16_w_game1 = sim_game(r32_w_game1, r32_w_game2, 16, points_dict, points_decided, []) # Arkansas vs UConn
    r16_w_game2 = sim_game(r32_w_game3, r32_w_game4, 16, points_dict, points_decided, []) # Gonzaga vs UCLA

    # Elite 8
    west_winner = sim_game(r16_w_game1, r16_w_game2, 8, points_dict, points_decided, [])

    ##### Midwest Region #####
    # Round of 64
    # 2023
    r64_mw_game1 = sim_game(houston, northern_kentucky, 64, points_dict, points_decided, [2,0])
    r64_mw_game2 = sim_game(iowa, auburn, 64, points_dict, points_decided, [0,1])
    r64_mw_game3 = sim_game(miami, drake, 64, points_dict, points_decided, [1,0])
    r64_mw_game4 = sim_game(indiana, kent_state, 64, points_dict, points_decided, [2,0])
    r64_mw_game5 = sim_game(iowa_state, mw_firstfour_11, 64, points_dict, points_decided, [0,2])
    r64_mw_game6 = sim_game(xavier, kennesaw_state, 64, points_dict, points_decided, [1,0])
    r64_mw_game7 = sim_game(texas_am, penn_state, 64, points_dict, points_decided, [0,2])
    r64_mw_game8 = sim_game(texas, colgate, 64, points_dict, points_decided, [3,0])

    # Round of 32
    r32_mw_game1 = sim_game(r64_mw_game1, r64_mw_game2, 32, points_dict, points_decided, [2,0]) # Houston vs Auburn
    r32_mw_game2 = sim_game(r64_mw_game3, r64_mw_game4, 32, points_dict, points_decided, [2,0]) # Miami vs Indiana
    r32_mw_game3 = sim_game(r64_mw_game5, r64_mw_game6, 32, points_dict, points_decided, [0,2]) # Pittsburgh vs Xavier
    r32_mw_game4 = sim_game(r64_mw_game7, r64_mw_game8, 32, points_dict, points_decided, [0,1]) # Penn State vs Texas

    # Sweet 16
    r16_mw_game1 = sim_game(r32_mw_game1, r32_mw_game2, 16, points_dict, points_decided, []) # Houston vs Miami
    r16_mw_game2 = sim_game(r32_mw_game3, r32_mw_game4, 16, points_dict, points_decided, []) # Xavier vs Texas

    # Elite 8
    midwest_winner = sim_game(r16_mw_game1, r16_mw_game2, 8, points_dict, points_decided, [])


    ##### East Region    #####
    # Round of 64
    # 2023
    r64_e_game1 = sim_game(purdue, east_firstfour_16, 64, points_dict, points_decided, [0,1])
    r64_e_game2 = sim_game(memphis, florida_atlantic, 64, points_dict, points_decided, [0,1])
    r64_e_game3 = sim_game(duke, oral_roberts, 64, points_dict, points_decided, [3,0])
    r64_e_game4 = sim_game(tennessee, louisiana, 64, points_dict, points_decided, [1,0])
    r64_e_game5 = sim_game(kentucky, providence, 64, points_dict, points_decided, [1,0])
    r64_e_game6 = sim_game(kansas_state, montana_state, 64, points_dict, points_decided, [2,0])
    r64_e_game7 = sim_game(michigan_state, usc, 64, points_dict, points_decided, [2,0])
    r64_e_game8 = sim_game(marquette, vermont, 64, points_dict, points_decided, [2,0])

    # Round of 32
    r32_e_game1 = sim_game(r64_e_game1, r64_e_game2, 32, points_dict, points_decided, [0,1]) # Fairleigh Dickinson vs Florida Atlantic
    r32_e_game2 = sim_game(r64_e_game3, r64_e_game4, 32, points_dict, points_decided, [0,2]) # Duke vs Tennessee
    r32_e_game3 = sim_game(r64_e_game5, r64_e_game6, 32, points_dict, points_decided, [0,1]) # Kentucky vs Kansas State
    r32_e_game4 = sim_game(r64_e_game7, r64_e_game8, 32, points_dict, points_decided, [1,0]) # Michigan State vs Marquette

    # Sweet 16
    r16_e_game1 = sim_game(r32_e_game1, r32_e_game2, 16, points_dict, points_decided, []) # Florida Atlantic vs Tennessee
    r16_e_game2 = sim_game(r32_e_game3, r32_e_game4, 16, points_dict, points_decided, []) # Kansas State vs Michigan State

    # Elite 8
    east_winner = sim_game(r16_e_game1, r16_e_game2, 8, points_dict, points_decided, [])

    ##### South Region   #####
    # Round of 64
    # 2023
    r64_s_game1 = sim_game(alabama, south_firstfour_16, 64, points_dict, points_decided, [3,0])
    r64_s_game2 = sim_game(maryland, west_virginia, 64, points_dict, points_decided, [1,0])
    r64_s_game3 = sim_game(san_diego_state, charleston, 64, points_dict, points_decided, [1,0])
    r64_s_game4 = sim_game(virginia, furman, 64, points_dict, points_decided, [0,1])
    r64_s_game5 = sim_game(creighton, north_carolina_state, 64, points_dict, points_decided, [1,0])
    r64_s_game6 = sim_game(baylor, uc_santa_barbara, 64, points_dict, points_decided, [2,0])
    r64_s_game7 = sim_game(missouri, utah_state, 64, points_dict, points_decided, [2,0])
    r64_s_game8 = sim_game(arizona, princeton, 64, points_dict, points_decided, [0,1])

    # Round of 32
    r32_s_game1 = sim_game(r64_s_game1, r64_s_game2, 32, points_dict, points_decided, [3,0]) # Alabama vs Maryland
    r32_s_game2 = sim_game(r64_s_game3, r64_s_game4, 32, points_dict, points_decided, [3,0]) # San Diego State vs Furman
    r32_s_game3 = sim_game(r64_s_game5, r64_s_game6, 32, points_dict, points_decided, [1,0]) # Creighton vs Baylor
    r32_s_game4 = sim_game(r64_s_game7, r64_s_game8, 32, points_dict, points_decided, [0,2]) # Missouri vs Princeton

    # Sweet 16
    r16_s_game1 = sim_game(r32_s_game1, r32_s_game2, 16, points_dict, points_decided, []) # Alabama vs San Diego State
    r16_s_game2 = sim_game(r32_s_game3, r32_s_game4, 16, points_dict, points_decided, []) # Creighton vs Princeton

    # Elite 8
    south_winner = sim_game(r16_s_game1, r16_s_game2, 8, points_dict, points_decided, [])

    # Final Four
    east_west_winner = sim_game(east_winner, west_winner, 4, points_dict, points_decided, [])
    south_midwest_winner = sim_game(south_winner, midwest_winner, 4, points_dict, points_decided, [])

    # Championship
    champion = sim_game(east_west_winner, south_midwest_winner, 2, points_dict, points_decided, [])
    champion.championships += 1

    return points_dict, points_decided


# running total of auction wins and points
num_wins = {"Devan": 0, "Jeremy": 0, "Josh": 0, "Justin": 0, "Brant": 0, "Nick": 0, "Joe": 0}

# list points scored in each tourney simulation
Devan = []
Jeremy = []
Josh = []
Justin = []
Brant = []
Nick = []
Joe = []
points_decided = {}

def sim_many_tournaments(num_sims):
    for _ in range(num_sims):
        points, points_decided = sim_tournament()

        Devan.append(points["Devan"])
        Brant.append(points["Brant"])
        Jeremy.append(points["Jeremy"])
        Josh.append(points["Josh"])
        Justin.append(points["Justin"])
        Nick.append(points["Nick"])
        Joe.append(points["Joe"])

        num_wins[max(points, key=points.get)] += 1

    for key in num_wins:
        num_wins[key] = num_wins[key] * 100 / num_sims

    avg_points = {key: mean(points_list) for key, points_list in zip(num_wins.keys(), [Devan, Jeremy, Josh, Justin, Brant, Nick, Joe])}

    print("<--- Expected win percentages --->")
    print(num_wins)

    print("<--- Decided points --->")
    print(points_decided)

    print("<--- Average points scored --->")
    print(avg_points)


sim_many_tournaments(100_000)
# plot density function for owners with non-zero variance
legend_list = []
THICKNESS = 2.5

if(var(Devan)):
    sns.kdeplot(Devan, linewidth=THICKNESS, color="tab:blue")
    legend_list.append("Devan:   {0}%".format(num_wins["Devan"]))

if(var(Jeremy)):
    sns.kdeplot(Jeremy, linewidth=THICKNESS, color="tab:orange")
    legend_list.append("Jeremy:  {0}%".format(num_wins["Jeremy"]))

if(var(Josh)):
    sns.kdeplot(Josh, linewidth=THICKNESS, color="tab:green")
    legend_list.append("Josh:    {0}%".format(num_wins["Josh"]))

if(var(Justin)):
    sns.kdeplot(Justin, linewidth=THICKNESS, color="tab:red")
    legend_list.append("Justin:  {0}%".format(num_wins["Justin"]))

# Brant's odds are < 1%
# if(var(Brant)):
#     sns.kdeplot(Brant, linewidth=THICKNESS, color="tab:purple")
#     legend_list.append("Brant:   {0}%".format(num_wins["Brant"]))

if(var(Nick)):
    sns.kdeplot(Nick, linewidth=THICKNESS, color="tab:brown")
    legend_list.append("Nick:    {0}%".format(num_wins["Nick"]))

if(var(Joe)):
    sns.kdeplot(Joe, linewidth=THICKNESS, color="tab:pink")
    legend_list.append("Joe:     {0}%".format(num_wins["Joe"]))

# configure and display plot
plt.title(headliner)
plt.xlabel("Points")
plt.ylabel("")
plt.yticks([])
plt.legend(legend_list)
plt.savefig(f"./mm_figs/mm_{i}.png", dpi=300)
#plt.show()
