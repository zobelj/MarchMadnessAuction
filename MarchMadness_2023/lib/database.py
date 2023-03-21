import sqlite3
import pandas as pd

DB_PATH = 'lib/march_madness.db'

def create_tables(drop_existing=False):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    if(drop_existing):
        print("Dropping existing table tourney_results...")
        c.execute("DROP TABLE IF EXISTS tourney_results")
        c.execute("DROP TABLE IF EXISTS schools_pts")
    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS tourney_results
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
                final_winner text, final_winner_blowout integer)
                ''')
    c.execute('''CREATE TABLE IF NOT EXISTS schools_pts
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


def create_pre_tables(drop_existing=False):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    if(drop_existing):
        print("Dropping existing table tourney_results_pre...")
        c.execute("DROP TABLE IF EXISTS tourney_results_pre")
        c.execute("DROP TABLE IF EXISTS schools_pts_pre")
    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS tourney_results_pre
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
                final_winner text, final_winner_blowout integer)
                ''')
    c.execute('''CREATE TABLE IF NOT EXISTS schools_pts_pre
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


def run_query(query, fetch=None):

    # run a query and fetch the results
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(query)

    if fetch == "all":
        return c.fetchall()
    elif fetch == "one":
        return c.fetchone()
    elif fetch == "sql":
        return pd.read_sql_query(query, conn)
    
    conn.commit()

    return None
