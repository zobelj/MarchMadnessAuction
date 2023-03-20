#!/usr/bin/env python3

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import random, mean, var
import math
import sqlite3
import random as rd
import string as str
# import team objects
from teams import *

# constants
pyth_exponent = 11.5
round_to_points = {64: 1, 32: 2, 16: 3, 8: 4, 4: 5, 2: 10, -1: 0}

def create_database(drop_existing=False):
    conn = sqlite3.connect('march_madness.db')
    c = conn.cursor()

    
    if(drop_existing):
        c.execute("DROP TABLE IF EXISTS march_madness")
        c.execute("DROP TABLE IF EXISTS march_madness_team_pts")
    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS march_madness
                    (sim_id text PRIMARY KEY,
                    Devan_win integer, Jeremy_win integer, Josh_win integer, Justin_win integer, Brant_win integer, Nick_win integer, Joe_win integer,
                        Devan_pts integer, Jeremy_pts integer, Josh_pts integer, Justin_pts integer, Brant_pts integer, Nick_pts integer, Joe_pts integer,
                 mw_firstfour_11 text, mw_firstfour_11_blowout integer, west_firstfour_11 text, west_firstfour_11_blowout integer,
                 east_firstfour_16 text, east_firstfour_16_blowout integer, south_firstfour_16 text, south_firstfour_16_blowout integer,
                 r64_w_game1 text, r64_w_game1_blowout integer, r64_w_game2 text, r64_w_game2_blowout integer, r64_w_game3 text, r64_w_game3_blowout integer, r64_w_game4 text, r64_w_game4_blowout integer, 
                 r64_w_game5 text, r64_w_game5_blowout integer, r64_w_game6 text, r64_w_game6_blowout integer, r64_w_game7 text, r64_w_game7_blowout integer, r64_w_game8 text, r64_w_game8_blowout integer,
                 r64_mw_game1 text, r64_mw_game1_blowout integer, r64_mw_game2 text, r64_mw_game2_blowout integer, r64_mw_game3 text, r64_mw_game3_blowout integer, r64_mw_game4 text, r64_mw_game4_blowout integer,
                r64_mw_game5 text, r64_mw_game5_blowout integer, r64_mw_game6 text, r64_mw_game6_blowout integer, r64_mw_game7 text, r64_mw_game7_blowout integer, r64_mw_game8 text, r64_mw_game8_blowout integer,
                r64_e_game1 text, r64_e_game1_blowout integer, r64_e_game2 text, r64_e_game2_blowout integer, r64_e_game3 text, r64_e_game3_blowout integer, r64_e_game4 text, r64_e_game4_blowout integer,
                r64_e_game5 text, r64_e_game5_blowout integer, r64_e_game6 text, r64_e_game6_blowout integer, r64_e_game7 text, r64_e_game7_blowout integer, r64_e_game8 text, r64_e_game8_blowout integer,
                r64_s_game1 text, r64_s_game1_blowout integer, r64_s_game2 text, r64_s_game2_blowout integer, r64_s_game3 text, r64_s_game3_blowout integer, r64_s_game4 text, r64_s_game4_blowout integer,
                r64_s_game5 text, r64_s_game5_blowout integer, r64_s_game6 text, r64_s_game6_blowout integer, r64_s_game7 text, r64_s_game7_blowout integer, r64_s_game8 text, r64_s_game8_blowout integer,
                r32_w_game1 text, r32_w_game1_blowout integer, r32_w_game2 text, r32_w_game2_blowout integer, r32_w_game3 text, r32_w_game3_blowout integer, r32_w_game4 text, r32_w_game4_blowout integer,
                r32_mw_game1 text, r32_mw_game1_blowout integer, r32_mw_game2 text, r32_mw_game2_blowout integer, r32_mw_game3 text, r32_mw_game3_blowout integer, r32_mw_game4 text, r32_mw_game4_blowout integer,
                r32_e_game1 text, r32_e_game1_blowout integer, r32_e_game2 text, r32_e_game2_blowout integer, r32_e_game3 text, r32_e_game3_blowout integer, r32_e_game4 text, r32_e_game4_blowout integer,
                r32_s_game1 text, r32_s_game1_blowout integer, r32_s_game2 text, r32_s_game2_blowout integer, r32_s_game3 text, r32_s_game3_blowout integer, r32_s_game4 text, r32_s_game4_blowout integer,
                r16_w_game1 text, r16_w_game1_blowout integer, r16_w_game2 text, r16_w_game2_blowout integer, r16_mw_game1 text, r16_mw_game1_blowout integer, r16_mw_game2 text, r16_mw_game2_blowout integer,
                r16_e_game1 text, r16_e_game1_blowout integer, r16_e_game2 text, r16_e_game2_blowout integer, r16_s_game1 text, r16_s_game1_blowout integer, r16_s_game2 text, r16_s_game2_blowout integer,
                west_winner text, west_winner_blowout integer, midwest_winner text, midwest_winner_blowout integer, east_winner text, east_winner_blowout integer, south_winner text, south_winner_blowout integer,
                south_east_winner text, south_east_winner_blowout integer, west_midwest_winner text, west_midwest_winner_blowout integer,
                final_winner text, final_winner_blowout integer)''')
    c.execute('''CREATE TABLE IF NOT EXISTS march_madness_team_pts
                    (sim_id text PRIMARY KEY,
                        mississippi_state_pts integer, pittsburgh_pts integer, arizona_state_pts integer, nevada_pts integer,
                        texas_southern_pts integer, fairleigh_dickinson_pts integer, texas_am_corpus_christi_pts integer, southeast_missouri_state_pts integer,
                        kansas_pts integer, howard_pts integer, arkansas_pts integer, illinois_pts integer, saint_marys_pts integer, vcu_pts integer, connecticut_pts integer, iona_pts integer,
                        tcu_pts integer, gonzaga_pts integer, grand_canyon_pts integer, northwestern_pts integer, boise_state_pts integer, ucla_pts integer, unc_asheville_pts integer,
                        houston_pts integer, northern_kentucky_pts integer, iowa_pts integer, auburn_pts integer, miami_pts integer, drake_pts integer, indiana_pts integer, kent_state_pts integer,
                        iowa_state_pts integer, xavier_pts integer, kennesaw_state_pts integer, texas_am_pts integer, penn_state_pts integer, texas_pts integer, colgate_pts integer,
                        purdue_pts integer, memphis_pts integer, florida_atlantic_pts integer, duke_pts integer, oral_roberts_pts integer, tennessee_pts integer, louisiana_pts integer,
                        kentucky_pts integer, providence_pts integer, kansas_state_pts integer, montana_state_pts integer, michigan_state_pts integer, usc_pts integer, marquette_pts integer, vermont_pts integer,
                        alabama_pts integer, maryland_pts integer, west_virginia_pts integer, san_diego_state_pts integer, charleston_pts integer, virginia_pts integer, furman_pts integer,
                        creighton_pts integer, north_carolina_state_pts integer, baylor_pts integer, uc_santa_barbara_pts integer, missouri_pts integer, utah_state_pts integer, arizona_pts integer, princeton_pts integer)
                        
                        ''') 
                 
                 

    # Save (commit) the changes
    conn.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()


def sim_game(team1, team2, round, points_dict, points_decided, force):

    # real simulation
    if(len(force) == 0):
        team1_win_percentage_season = (team1.adjO**pyth_exponent) / ((team1.adjO**pyth_exponent) + (team1.adjD**pyth_exponent))
        team2_win_percentage_season = (team2.adjO**pyth_exponent) / ((team2.adjO**pyth_exponent) + (team2.adjD**pyth_exponent)) 

        team1_win_percentage = ((team1_win_percentage_season - (team1_win_percentage_season * team2_win_percentage_season)) / ((team1_win_percentage_season + team2_win_percentage_season) - (2 * team1_win_percentage_season * team2_win_percentage_season)))
        team2_win_percentage = 1 - team1_win_percentage

        winner = random.choice([team1, team2], p=[team1_win_percentage, team2_win_percentage])
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


#########################################################################################################
headliner = "Gonzaga beats TCU"
i = 53

#########################################################################################################
create_database()

def sim_tournament():

    sim_id = ''.join(rd.choices(str.ascii_uppercase + str.digits, k=10))
    points_dict = {"Devan": 0, "Jeremy": 0, "Josh": 0, "Justin": 0, "Brant": 0, "Nick": 0, "Joe": 0}
    points_decided = {"Devan": 0, "Jeremy": 0, "Josh": 0, "Justin": 0, "Brant": 0, "Nick": 0, "Joe": 0}
    wins = {"Devan": 0, "Jeremy": 0, "Josh": 0, "Justin": 0, "Brant": 0, "Nick": 0, "Joe": 0}

    #for team in team_list, reset pts to 0
    for team in team_list:
        team.pts = 0

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
    r64_w_game5 = sim_game(tcu, west_firstfour_11[0], 64, points_dict, points_decided, [1,0])
    r64_w_game6 = sim_game(gonzaga, grand_canyon, 64, points_dict, points_decided, [2,0])
    r64_w_game7 = sim_game(northwestern, boise_state, 64, points_dict, points_decided, [1,0])
    r64_w_game8 = sim_game(ucla, unc_asheville, 64, points_dict, points_decided, [4,0])

    # Round of 32
    r32_w_game1 = sim_game(r64_w_game1[0], r64_w_game2[0], 32, points_dict, points_decided, [0,1]) # Kansas vs Arkansas
    r32_w_game2 = sim_game(r64_w_game3[0], r64_w_game4[0], 32, points_dict, points_decided, [0,2]) # Saint Mary's vs UConn
    r32_w_game3 = sim_game(r64_w_game5[0], r64_w_game6[0], 32, points_dict, points_decided, [0,1]) # TCU vs Gonzaga
    r32_w_game4 = sim_game(r64_w_game7[0], r64_w_game8[0], 32, points_dict, points_decided, [0,1]) # Northwestern vs UCLA

    # Sweet 16
    r16_w_game1 = sim_game(r32_w_game1[0], r32_w_game2[0], 16, points_dict, points_decided, []) # Arkansas vs UConn
    r16_w_game2 = sim_game(r32_w_game3[0], r32_w_game4[0], 16, points_dict, points_decided, []) # Gonzaga vs UCLA

    # Elite 8
    west_winner = sim_game(r16_w_game1[0], r16_w_game2[0], 8, points_dict, points_decided, [])

    ##### Midwest Region #####
    # Round of 64
    # 2023
    r64_mw_game1 = sim_game(houston, northern_kentucky, 64, points_dict, points_decided, [2,0])
    r64_mw_game2 = sim_game(iowa, auburn, 64, points_dict, points_decided, [0,1])
    r64_mw_game3 = sim_game(miami, drake, 64, points_dict, points_decided, [1,0])
    r64_mw_game4 = sim_game(indiana, kent_state, 64, points_dict, points_decided, [2,0])
    r64_mw_game5 = sim_game(iowa_state, mw_firstfour_11[0], 64, points_dict, points_decided, [0,2])
    r64_mw_game6 = sim_game(xavier, kennesaw_state, 64, points_dict, points_decided, [1,0])
    r64_mw_game7 = sim_game(texas_am, penn_state, 64, points_dict, points_decided, [0,2])
    r64_mw_game8 = sim_game(texas, colgate, 64, points_dict, points_decided, [3,0])

    # Round of 32
    r32_mw_game1 = sim_game(r64_mw_game1[0], r64_mw_game2[0], 32, points_dict, points_decided, [2,0]) # Houston vs Auburn
    r32_mw_game2 = sim_game(r64_mw_game3[0], r64_mw_game4[0], 32, points_dict, points_decided, [2,0]) # Miami vs Indiana
    r32_mw_game3 = sim_game(r64_mw_game5[0], r64_mw_game6[0], 32, points_dict, points_decided, [0,2]) # Pittsburgh vs Xavier
    r32_mw_game4 = sim_game(r64_mw_game7[0], r64_mw_game8[0], 32, points_dict, points_decided, [0,1]) # Penn State vs Texas

    # Sweet 16
    r16_mw_game1 = sim_game(r32_mw_game1[0], r32_mw_game2[0], 16, points_dict, points_decided, []) # Houston vs Miami
    r16_mw_game2 = sim_game(r32_mw_game3[0], r32_mw_game4[0], 16, points_dict, points_decided, []) # Xavier vs Texas

    # Elite 8
    midwest_winner = sim_game(r16_mw_game1[0], r16_mw_game2[0], 8, points_dict, points_decided, [])


    ##### East Region    #####
    # Round of 64
    # 2023
    r64_e_game1 = sim_game(purdue, east_firstfour_16[0], 64, points_dict, points_decided, [0,1])
    r64_e_game2 = sim_game(memphis, florida_atlantic, 64, points_dict, points_decided, [0,1])
    r64_e_game3 = sim_game(duke, oral_roberts, 64, points_dict, points_decided, [3,0])
    r64_e_game4 = sim_game(tennessee, louisiana, 64, points_dict, points_decided, [1,0])
    r64_e_game5 = sim_game(kentucky, providence, 64, points_dict, points_decided, [1,0])
    r64_e_game6 = sim_game(kansas_state, montana_state, 64, points_dict, points_decided, [2,0])
    r64_e_game7 = sim_game(michigan_state, usc, 64, points_dict, points_decided, [2,0])
    r64_e_game8 = sim_game(marquette, vermont, 64, points_dict, points_decided, [2,0])
    # Round of 32
    r32_e_game1 = sim_game(r64_e_game1[0], r64_e_game2[0], 32, points_dict, points_decided, [0,1]) # Fairleigh Dickinson vs Florida Atlantic
    r32_e_game2 = sim_game(r64_e_game3[0], r64_e_game4[0], 32, points_dict, points_decided, [0,2]) # Duke vs Tennessee
    r32_e_game3 = sim_game(r64_e_game5[0], r64_e_game6[0], 32, points_dict, points_decided, [0,1]) # Kentucky vs Kansas State
    r32_e_game4 = sim_game(r64_e_game7[0], r64_e_game8[0], 32, points_dict, points_decided, [1,0]) # Michigan State vs Marquette

    # Sweet 16
    r16_e_game1 = sim_game(r32_e_game1[0], r32_e_game2[0], 16, points_dict, points_decided, []) # Florida Atlantic vs Tennessee
    r16_e_game2 = sim_game(r32_e_game3[0], r32_e_game4[0], 16, points_dict, points_decided, []) # Kansas State vs Michigan State

    # Elite 8
    east_winner = sim_game(r16_e_game1[0], r16_e_game2[0], 8, points_dict, points_decided, [])

    ##### South Region   #####
    # Round of 64
    # 2023
    r64_s_game1 = sim_game(alabama, south_firstfour_16[0], 64, points_dict, points_decided, [3,0])
    r64_s_game2 = sim_game(maryland, west_virginia, 64, points_dict, points_decided, [1,0])
    r64_s_game3 = sim_game(san_diego_state, charleston, 64, points_dict, points_decided, [1,0])
    r64_s_game4 = sim_game(virginia, furman, 64, points_dict, points_decided, [0,1])
    r64_s_game5 = sim_game(creighton, north_carolina_state, 64, points_dict, points_decided, [1,0])
    r64_s_game6 = sim_game(baylor, uc_santa_barbara, 64, points_dict, points_decided, [2,0])
    r64_s_game7 = sim_game(missouri, utah_state, 64, points_dict, points_decided, [2,0])
    r64_s_game8 = sim_game(arizona, princeton, 64, points_dict, points_decided, [0,1])

    # Round of 32
    r32_s_game1 = sim_game(r64_s_game1[0], r64_s_game2[0], 32, points_dict, points_decided, [3,0]) # Alabama vs Maryland
    r32_s_game2 = sim_game(r64_s_game3[0], r64_s_game4[0], 32, points_dict, points_decided, [3,0]) # San Diego State vs Furman
    r32_s_game3 = sim_game(r64_s_game5[0], r64_s_game6[0], 32, points_dict, points_decided, [1,0]) # Creighton vs Baylor
    r32_s_game4 = sim_game(r64_s_game7[0], r64_s_game8[0], 32, points_dict, points_decided, [0,2]) # Missouri vs Princeton

    # Sweet 16
    r16_s_game1 = sim_game(r32_s_game1[0], r32_s_game2[0], 16, points_dict, points_decided, []) # Alabama vs San Diego State
    r16_s_game2 = sim_game(r32_s_game3[0], r32_s_game4[0], 16, points_dict, points_decided, []) # Creighton vs Princeton

    # Elite 8
    south_winner = sim_game(r16_s_game1[0], r16_s_game2[0], 8, points_dict, points_decided, [])

    # Final Four
    south_east_winner = sim_game(south_winner[0], east_winner[0], 4, points_dict, points_decided, [])
    west_midwest_winner = sim_game(west_winner[0], midwest_winner[0], 4, points_dict, points_decided, [])

    # Championship
    champion = sim_game(south_east_winner[0], west_midwest_winner[0], 2, points_dict, points_decided, [])
    champion[0].championships += 1

    #create list of all players
    for player in points_dict:
        # if player has max points, change win[player] to 1
        if points_dict[player] == max(points_dict.values()):
            wins[player] += 1

    # add row to march_madness.db
    conn = sqlite3.connect('march_madness.db')
    c = conn.cursor()
    string = (f'''INSERT INTO march_madness VALUES (
            '{sim_id}', 
            {wins["Devan"]}, {wins["Jeremy"]}, {wins["Josh"]}, {wins["Justin"]}, {wins["Brant"]}, {wins["Nick"]}, {wins["Joe"]},
            {points_dict["Devan"]}, {points_dict["Jeremy"]}, {points_dict["Josh"]}, {points_dict["Justin"]}, {points_dict["Brant"]}, {points_dict["Nick"]}, {points_dict["Joe"]},
              "{mw_firstfour_11[0].name}", {mw_firstfour_11[1]}, "{west_firstfour_11[0].name}", {west_firstfour_11[1]}, "{south_firstfour_16[0].name}", {south_firstfour_16[1]}, "{east_firstfour_16[0].name}", {east_firstfour_16[1]},
              "{r64_w_game1[0].name}", {r64_w_game1[1]}, "{r64_w_game2[0].name}", {r64_w_game2[1]}, "{r64_w_game3[0].name}", {r64_w_game3[1]}, "{r64_w_game4[0].name}", {r64_w_game4[1]}, "{r64_w_game5[0].name}", {r64_w_game5[1]}, "{r64_w_game6[0].name}", {r64_w_game6[1]}, "{r64_w_game7[0].name}", {r64_w_game7[1]}, "{r64_w_game8[0].name}", {r64_w_game8[1]},
              "{r64_mw_game1[0].name}", {r64_mw_game1[1]}, "{r64_mw_game2[0].name}", {r64_mw_game2[1]}, "{r64_mw_game3[0].name}", {r64_mw_game3[1]}, "{r64_mw_game4[0].name}", {r64_mw_game4[1]}, "{r64_mw_game5[0].name}", {r64_mw_game5[1]}, "{r64_mw_game6[0].name}", {r64_mw_game6[1]}, "{r64_mw_game7[0].name}", {r64_mw_game7[1]}, "{r64_mw_game8[0].name}", {r64_mw_game8[1]},
              "{r64_e_game1[0].name}", {r64_e_game1[1]}, "{r64_e_game2[0].name}", {r64_e_game2[1]}, "{r64_e_game3[0].name}", {r64_e_game3[1]}, "{r64_e_game4[0].name}", {r64_e_game4[1]}, "{r64_e_game5[0].name}", {r64_e_game5[1]}, "{r64_e_game6[0].name}", {r64_e_game6[1]}, "{r64_e_game7[0].name}", {r64_e_game7[1]}, "{r64_e_game8[0].name}", {r64_e_game8[1]},
                "{r64_s_game1[0].name}", {r64_s_game1[1]}, "{r64_s_game2[0].name}", {r64_s_game2[1]}, "{r64_s_game3[0].name}", {r64_s_game3[1]}, "{r64_s_game4[0].name}", {r64_s_game4[1]}, "{r64_s_game5[0].name}", {r64_s_game5[1]}, "{r64_s_game6[0].name}", {r64_s_game6[1]}, "{r64_s_game7[0].name}", {r64_s_game7[1]}, "{r64_s_game8[0].name}", {r64_s_game8[1]},
                "{r32_w_game1[0].name}", {r32_w_game1[1]}, "{r32_w_game2[0].name}", {r32_w_game2[1]}, "{r32_w_game3[0].name}", {r32_w_game3[1]}, "{r32_w_game4[0].name}", {r32_w_game4[1]},
                "{r32_mw_game1[0].name}", {r32_mw_game1[1]}, "{r32_mw_game2[0].name}", {r32_mw_game2[1]}, "{r32_mw_game3[0].name}", {r32_mw_game3[1]}, "{r32_mw_game4[0].name}", {r32_mw_game4[1]},
                "{r32_e_game1[0].name}", {r32_e_game1[1]}, "{r32_e_game2[0].name}", {r32_e_game2[1]}, "{r32_e_game3[0].name}", {r32_e_game3[1]}, "{r32_e_game4[0].name}", {r32_e_game4[1]},
                "{r32_s_game1[0].name}", {r32_s_game1[1]}, "{r32_s_game2[0].name}", {r32_s_game2[1]}, "{r32_s_game3[0].name}", {r32_s_game3[1]}, "{r32_s_game4[0].name}", {r32_s_game4[1]},
                "{r16_w_game1[0].name}", {r16_w_game1[1]}, "{r16_w_game2[0].name}", {r16_w_game2[1]},
                "{r16_mw_game1[0].name}", {r16_mw_game1[1]}, "{r16_mw_game2[0].name}", {r16_mw_game2[1]},
                "{r16_e_game1[0].name}", {r16_e_game1[1]}, "{r16_e_game2[0].name}", {r16_e_game2[1]},
                "{r16_s_game1[0].name}", {r16_s_game1[1]}, "{r16_s_game2[0].name}", {r16_s_game2[1]},
                "{west_winner[0].name}", {west_winner[1]},
                "{midwest_winner[0].name}", {midwest_winner[1]},
                "{east_winner[0].name}", {east_winner[1]},
                "{south_winner[0].name}", {south_winner[1]},
                "{south_east_winner[0].name}", {south_east_winner[1]},
                "{west_midwest_winner[0].name}", {west_midwest_winner[1]},
                "{champion[0].name}", {champion[1]})''')
    
    string_2 = (f'''INSERT INTO march_madness_team_pts VALUES(
                '{sim_id}',
                {mississippi_state.pts}, {pittsburgh.pts}, {arizona_state.pts}, {nevada.pts},
                {texas_southern.pts}, {fairleigh_dickinson.pts}, {texas_am_corpus_christi.pts}, {southeast_missouri_state.pts},
                {kansas.pts}, {howard.pts}, {arkansas.pts}, {illinois.pts}, {saint_marys.pts}, {vcu.pts}, {connecticut.pts}, {iona.pts},
                {tcu.pts}, {gonzaga.pts}, {grand_canyon.pts}, {northwestern.pts}, {boise_state.pts}, {ucla.pts}, {unc_asheville.pts},
                {houston.pts}, {northern_kentucky.pts}, {iowa.pts}, {auburn.pts}, {miami.pts}, {drake.pts}, {indiana.pts}, {kent_state.pts},
                {iowa_state.pts}, {xavier.pts}, {kennesaw_state.pts}, {texas_am.pts}, {penn_state.pts}, {texas.pts}, {colgate.pts},
                {purdue.pts}, {memphis.pts}, {florida_atlantic.pts}, {duke.pts}, {oral_roberts.pts}, {tennessee.pts}, {louisiana.pts},
                {kentucky.pts}, {providence.pts}, {kansas_state.pts}, {montana_state.pts}, {michigan_state.pts}, {usc.pts}, {marquette.pts}, {vermont.pts},
                {alabama.pts}, {maryland.pts}, {west_virginia.pts}, {san_diego_state.pts}, {charleston.pts}, {virginia.pts}, {furman.pts},
                {creighton.pts}, {north_carolina_state.pts}, {baylor.pts}, {uc_santa_barbara.pts}, {missouri.pts}, {utah_state.pts}, {arizona.pts}, {princeton.pts})''')

    conn.execute(string)   
    conn.execute(string_2)        
    conn.commit()
    conn.close()

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
        if _ % 1000 == 0:
            print(f"Simulating tournament {_} of {num_sims}...")
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

# if(var(Justin)):
#     sns.kdeplot(Justin, linewidth=THICKNESS, color="tab:red")
#     legend_list.append("Justin:  {0}%".format(num_wins["Justin"]))

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
