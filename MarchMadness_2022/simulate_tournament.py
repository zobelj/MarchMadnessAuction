#!/usr/bin/env python3

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import random, mean, var

# import kenpom data
df = pd.read_excel("summary22.xlsx")
df.set_index("Team", inplace=True)

# constants
pyth_exponent = 11.5
round_to_points = {64: 1, 32: 2, 16: 3, 8: 4, 4: 5, 2: 10, -1: 0}

class Team():
    def __init__(self, name, owner, seed):
        self.owner = owner
        self.name = name
        self.seed = seed
        self.adjO = df.loc[name, "AdjO"]
        self.adjD = df.loc[name, "AdjD"]


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

def blowout(winner, loser):
    seed_diff = loser.seed - winner.seed + 15

    over30 = seed_diff / 125
    over20 = seed_diff / 100
    over10 = seed_diff / 75
    less10 = 1 - over30 - over20 - over10

    return random.choice([0,1,2,3], p=[less10, over10, over20, over30])

#########################################################################################################
headliner = "UNC beats St. Peter's\nEnd of Weekend 2"
i = 65

#########################################################################################################

def sim_tournament():

    points_dict = {"Devan": 0, "Jeremy": 0, "Josh": 0, "Justin": 0, "Brant": 0, "Nick": 0, "Joe": 0}
    points_decided = {"Devan": 0, "Jeremy": 0, "Josh": 0, "Justin": 0, "Brant": 0, "Nick": 0, "Joe": 0}

    # First Four
    # 2022
    mw_firstfour_16 = sim_game(texas_southern, texas_am_corpus_christi, -1, points_dict, points_decided, [1,0])
    west_firstfour_11 = sim_game(rutgers, notre_dame, -1, points_dict, points_decided, [0,1])
    east_firstfour_12 = sim_game(wyoming, indiana, -1, points_dict, points_decided, [0,1])
    south_firstfour_16 = sim_game(wright_state, bryant, -1, points_dict, points_decided, [2,0])

    #####  West Region  #####
    # Round of 64
    # 2022
    r64_w_game1 = sim_game(gonzaga, georgia_state, 64, points_dict, points_decided, [3,0])
    r64_w_game2 = sim_game(boise_state, memphis, 64, points_dict, points_decided, [0,2])
    r64_w_game3 = sim_game(connecticut, new_mexico_state, 64, points_dict, points_decided, [0,1])
    r64_w_game4 = sim_game(arkansas, vermont, 64, points_dict, points_decided, [1,0])
    r64_w_game5 = sim_game(alabama, west_firstfour_11, 64, points_dict, points_decided, [0,2])
    r64_w_game6 = sim_game(texas_tech, montana_state, 64, points_dict, points_decided, [4,0])
    r64_w_game7 = sim_game(michigan_state, davidson, 64, points_dict, points_decided, [1,0])
    r64_w_game8 = sim_game(duke, csu_fullerton, 64, points_dict, points_decided, [2,0])

    # Round of 32
    r32_w_game1 = sim_game(r64_w_game1, r64_w_game2, 32, points_dict, points_decided, [1,0]) # Gonzaga vs Memphis
    r32_w_game2 = sim_game(r64_w_game3, r64_w_game4, 32, points_dict, points_decided, [0,1]) # New Mexico State vs Arkansas
    r32_w_game3 = sim_game(r64_w_game5, r64_w_game6, 32, points_dict, points_decided, [0,1]) # Notre Dame vs Texas Tech
    r32_w_game4 = sim_game(r64_w_game7, r64_w_game8, 32, points_dict, points_decided, [0,1]) # Michigan State vs Duke

    # Sweet 16
    r16_w_game1 = sim_game(r32_w_game1, r32_w_game2, 16, points_dict, points_decided, [0,1]) # Gonzaga vs Arkansas
    r16_w_game2 = sim_game(r32_w_game3, r32_w_game4, 16, points_dict, points_decided, [0,1]) # Texas Tech vs Duke

    # Elite 8
    west_winner = sim_game(r16_w_game1, r16_w_game2, 8, points_dict, points_decided, [0,1]) # Arkansas vs Duke

    ##### Midwest Region #####
    # Round of 64
    # 2022
    r64_mw_game1 = sim_game(kansas, mw_firstfour_16, 64, points_dict, points_decided, [3,0])
    r64_mw_game2 = sim_game(san_diego_state, creighton, 64, points_dict, points_decided, [0,1])
    r64_mw_game3 = sim_game(iowa, richmond, 64, points_dict, points_decided, [0,1])
    r64_mw_game4 = sim_game(providence, south_dakota_state, 64, points_dict, points_decided, [1,0])
    r64_mw_game5 = sim_game(lsu, iowa_state, 64, points_dict, points_decided, [0,1])
    r64_mw_game6 = sim_game(wisconsin, colgate, 64, points_dict, points_decided, [1,0])
    r64_mw_game7 = sim_game(usc, miami, 64, points_dict, points_decided, [0,1])
    r64_mw_game8 = sim_game(auburn, jacksonville_state, 64, points_dict, points_decided, [2,0])

    # Round of 32
    r32_mw_game1 = sim_game(r64_mw_game1, r64_mw_game2, 32, points_dict, points_decided, [1,0]) # Kansas vs Creighton
    r32_mw_game2 = sim_game(r64_mw_game3, r64_mw_game4, 32, points_dict, points_decided, [0,3]) # Richmond vs Providence
    r32_mw_game3 = sim_game(r64_mw_game5, r64_mw_game6, 32, points_dict, points_decided, [1,0]) # Iowa State vs Wisconsin
    r32_mw_game4 = sim_game(r64_mw_game7, r64_mw_game8, 32, points_dict, points_decided, [2,0]) # Miami vs Auburn

    # Sweet 16
    r16_mw_game1 = sim_game(r32_mw_game1, r32_mw_game2, 16, points_dict, points_decided, [1,0]) # Kansas vs Providence
    r16_mw_game2 = sim_game(r32_mw_game3, r32_mw_game4, 16, points_dict, points_decided, [0,2]) # Iowa State vs Miami

    # Elite 8
    midwest_winner = sim_game(r16_mw_game1, r16_mw_game2, 8, points_dict, points_decided, [3,0]) # Kansas vs Miami


    ##### East Region    #####
    # Round of 64
    # 2022
    r64_e_game1 = sim_game(baylor, norfolk_state, 64, points_dict, points_decided, [4,0])
    r64_e_game2 = sim_game(north_carolina, marquette, 64, points_dict, points_decided, [4,0])
    r64_e_game3 = sim_game(saint_marys, east_firstfour_12, 64, points_dict, points_decided, [3,0])
    r64_e_game4 = sim_game(ucla, akron, 64, points_dict, points_decided, [1,0])
    r64_e_game5 = sim_game(texas, virginia_tech, 64, points_dict, points_decided, [1,0])
    r64_e_game6 = sim_game(purdue, yale, 64, points_dict, points_decided, [3,0])
    r64_e_game7 = sim_game(murray_state, san_francisco, 64, points_dict, points_decided, [1,0])
    r64_e_game8 = sim_game(kentucky, st_peters, 64, points_dict, points_decided, [0,1])

    # Round of 32
    r32_e_game1 = sim_game(r64_e_game1, r64_e_game2, 32, points_dict, points_decided, [0,1]) # Baylor vs UNC
    r32_e_game2 = sim_game(r64_e_game3, r64_e_game4, 32, points_dict, points_decided, [0,2]) # Saint Mary's vs UCLA
    r32_e_game3 = sim_game(r64_e_game5, r64_e_game6, 32, points_dict, points_decided, [0,2]) # Texas vs Purdue
    r32_e_game4 = sim_game(r64_e_game7, r64_e_game8, 32, points_dict, points_decided, [0,2]) # Murray State vs St. Peter's

    # Sweet 16
    r16_e_game1 = sim_game(r32_e_game1, r32_e_game2, 16, points_dict, points_decided, [1,0]) # UNC vs UCLA
    r16_e_game2 = sim_game(r32_e_game3, r32_e_game4, 16, points_dict, points_decided, [0,1]) # Purdue vs St. Peter's

    # Elite 8
    east_winner = sim_game(r16_e_game1, r16_e_game2, 8, points_dict, points_decided, [3,0]) # UNC vs St. Peter's

    ##### South Region   #####
    # Round of 64
    # 2022
    r64_s_game1 = sim_game(arizona, south_firstfour_16, 64, points_dict, points_decided, [2,0])
    r64_s_game2 = sim_game(seton_hall, tcu, 64, points_dict, points_decided, [0,3])
    r64_s_game3 = sim_game(houston, uab, 64, points_dict, points_decided, [2,0])
    r64_s_game4 = sim_game(illinois, chattanooga, 64, points_dict, points_decided, [1,0])
    r64_s_game5 = sim_game(colorado_state, michigan, 64, points_dict, points_decided, [0,2])
    r64_s_game6 = sim_game(tennessee, longwood, 64, points_dict, points_decided, [4,0])
    r64_s_game7 = sim_game(ohio_state, loyola_chicago, 64, points_dict, points_decided, [2,0])
    r64_s_game8 = sim_game(villanova, delaware, 64, points_dict, points_decided, [3,0])

    # Round of 32
    r32_s_game1 = sim_game(r64_s_game1, r64_s_game2, 32, points_dict, points_decided, [1,0]) # Arizona vs TCU
    r32_s_game2 = sim_game(r64_s_game3, r64_s_game4, 32, points_dict, points_decided, [2,0]) # Houston vs Illinois
    r32_s_game3 = sim_game(r64_s_game5, r64_s_game6, 32, points_dict, points_decided, [1,0]) # Michigan vs Tennessee
    r32_s_game4 = sim_game(r64_s_game7, r64_s_game8, 32, points_dict, points_decided, [0,2]) # Ohio State vs Villanova

    # Sweet 16
    r16_s_game1 = sim_game(r32_s_game1, r32_s_game2, 16, points_dict, points_decided, [0,2]) # Arizona vs Houston
    r16_s_game2 = sim_game(r32_s_game3, r32_s_game4, 16, points_dict, points_decided, [0,1]) # Michigan vs Villanova

    # Elite 8
    south_winner = sim_game(r16_s_game1, r16_s_game2, 8, points_dict, points_decided, [0,1]) # Houston vs Villanova

    # Final Four
    east_west_winner = sim_game(east_winner, west_winner, 4, points_dict, points_decided, [])
    south_midwest_winner = sim_game(south_winner, midwest_winner, 4, points_dict, points_decided, [])

    # Championship
    champion = sim_game(east_west_winner, south_midwest_winner, 2, points_dict, points_decided, [])

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

# create team objects
# Kept from 2021
ucla = Team("UCLA", "Josh", 4)
arkansas = Team("Arkansas", "Brant", 4)
houston = Team("Houston", "Joe", 5)
colgate = Team("Colgate", "Josh", 14)
wisconsin = Team("Wisconsin", "Brant", 3)
north_carolina = Team("North Carolina", "Jeremy", 8)
connecticut = Team("Connecticut", "Nick", 5)
virginia_tech = Team("Virginia Tech", "Nick", 11)
gonzaga = Team("Gonzaga", "Devan", 1)
kansas = Team("Kansas", "Devan", 1)
lsu = Team("LSU", "Joe", 6)
purdue = Team("Purdue", "Brant", 3)
rutgers = Team("Rutgers", "Joe", 11)
baylor = Team("Baylor", "Justin", 1)
iowa = Team("Iowa", "Devan", 5)
michigan = Team("Michigan", "Joe", 11)
texas_tech = Team("Texas Tech", "Jeremy", 3)
loyola_chicago = Team("Loyola Chicago", "Joe", 10)
san_diego_state = Team("San Diego St.", "Nick", 8)
illinois = Team("Illinois", "Jeremy", 4)
texas = Team("Texas", "Joe", 6)
tennessee = Team("Tennessee", "Justin", 3)
alabama = Team("Alabama", "Nick", 6)
creighton = Team("Creighton", "Jeremy", 9)
ohio_state = Team("Ohio St.", "Jeremy", 7)
michigan_state = Team("Michigan St.", "Joe", 7)
usc = Team("USC", "Brant", 7)
villanova = Team("Villanova", "Brant", 2)

# Added for 2022
texas_southern = Team("Texas Southern", "Josh", 16)
texas_am_corpus_christi = Team("Texas A&M Corpus Chris", "Josh", 16)
notre_dame = Team("Notre Dame", "Nick", 11)
wyoming = Team("Wyoming", "Nick", 12)
indiana = Team("Indiana", "Joe", 12)
wright_state = Team("Wright St.", "Josh", 16)
bryant = Team("Bryant", "Jeremy", 16)
georgia_state = Team("Georgia St.", "Joe", 16)
boise_state = Team("Boise St.", "Nick", 8)
memphis = Team("Memphis", "Jeremy", 9)
new_mexico_state = Team("New Mexico St.", "Justin", 12)
vermont = Team("Vermont", "Josh", 13)
montana_state = Team("Montana St.", "Josh", 14)
davidson = Team("Davidson", "Nick", 10)
duke = Team("Duke", "Nick", 2)
csu_fullerton = Team("Cal St. Fullerton", "Justin", 15)
richmond = Team("Richmond", "Nick", 12)
providence = Team("Providence", "Justin", 4)
south_dakota_state = Team("South Dakota St.", "Josh", 13)
iowa_state = Team("Iowa St.", "Joe", 11)
miami = Team("Miami FL", "Jeremy", 10)
auburn = Team("Auburn", "Josh", 2)
jacksonville_state = Team("Jackson St.", "Nick", 15)
norfolk_state = Team("Norfolk St.", "Nick", 16)
marquette = Team("Marquette", "Jeremy", 9)
saint_marys = Team("Saint Mary's", "Justin", 5)
akron = Team("Akron", "Nick", 13)
yale = Team("Yale", "Jeremy", 14)
murray_state = Team("Murray St.", "Brant", 7)
san_francisco = Team("San Francisco", "Devan", 10)
kentucky = Team("Kentucky", "Joe", 2)
st_peters = Team("Saint Peter's", "Joe", 15)
arizona = Team("Arizona", "Josh", 1)
seton_hall = Team("Seton Hall", "Joe", 8)
tcu = Team("TCU", "Jeremy", 9)
uab = Team("UAB", "Brant", 12)
chattanooga = Team("Chattanooga", "Nick", 13)
colorado_state = Team("Colorado St.", "Nick", 6)
longwood = Team("Longwood", "Justin", 14)
delaware = Team("Delaware", "Justin", 15)

sim_many_tournaments(10000)
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


if(var(Brant)):
    sns.kdeplot(Brant, linewidth=THICKNESS, color="tab:purple")
    legend_list.append("Brant:   {0}%".format(num_wins["Brant"]))

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
plt.show()
