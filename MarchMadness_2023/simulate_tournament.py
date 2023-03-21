#!/usr/bin/env python3
from numpy import var
import random as rd
import string as str

from lib.teams import *
from lib.database import create_tables, run_query
from lib.simulate import sim_game, sim_many_tournaments
from lib.graphs import density_plot

#########################################################################################################
headliner = "Gonzaga beats TCU"
i = 53
#########################################################################################################

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
    query_1 = (f'''INSERT INTO tourney_results VALUES (
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
    
    query_2 = (f'''INSERT INTO schools_pts VALUES(
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

    run_query(query_1)
    run_query(query_2)
    
    return points_dict, points_decided


if __name__ == '__main__':
    create_tables(True)
    points_lists = sim_many_tournaments(10_000, sim_tournament)
    density_plot(points_lists, headliner, i)
