import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import random, mean, var

# import kenpom data
df = pd.read_excel("kenpom.xlsx")
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


def sim_game(team1, team2, round, points_dict, force):

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
    else:
        if(force[0] == 1):
            winner = team1
            loser = team2
        else:
            loser = team1
            winner = team2
        
        if(winner.seed > loser.seed):
            points_dict[winner.owner] += round_to_points[round] + 2 + force[1]
        else:
            points_dict[winner.owner] += round_to_points[round] + force[1]
    
    return winner

def blowout(winner, loser):
    seed_diff = loser.seed - winner.seed + 15

    over30 = seed_diff / 125
    over20 = seed_diff / 100
    over10 = seed_diff / 75
    less10 = 1 - over30 - over20 - over10

    return random.choice([0,1,2,3], p=[less10, over10, over20, over30])

###################################
headliner = "Gonzaga beats UCLA"
i = 66

###################################


def sim_tournament():
    global ucla_east_wins
    points_dict = {"Devan": 0, "Jeremy": 0, "Josh": 0, "Justin": 0, "Brant": 0, "Nick": 0, "Joe": 0}

    # First Four
    west_firstfour_16 = sim_game(norfolk_state, appalachian_state, -1, points_dict, [])
    west_firstfour_11 = sim_game(wichita_state, drake, -1, points_dict, [])
    east_firstfour_16 = sim_game(mount_saint_marys, texas_southern, -1, points_dict, [])
    east_firstfour_11 = sim_game(ucla, michigan_state, -1, points_dict, [])

    #####  West Region  #####
    # Round of 64
    r64_w_game1 = sim_game(gonzaga, west_firstfour_16, 64, points_dict, [])
    r64_w_game2 = sim_game(oklahoma, missouri, 64, points_dict, [])
    r64_w_game3 = sim_game(creighton, ucsb, 64, points_dict, [])
    r64_w_game4 = sim_game(virginia, ohio, 64, points_dict, [])
    r64_w_game5 = sim_game(usc, west_firstfour_11, 64, points_dict, [])
    r64_w_game6 = sim_game(kansas, eastern_washington, 64, points_dict, [])
    r64_w_game7 = sim_game(oregon, vcu, 64, points_dict, [])
    r64_w_game8 = sim_game(iowa, grand_canyon, 64, points_dict, [1,1])

    # Round of 32
    r32_w_game1 = sim_game(r64_w_game1, r64_w_game2, 32, points_dict, [])
    r32_w_game2 = sim_game(r64_w_game3, r64_w_game4, 32, points_dict, [])
    r32_w_game3 = sim_game(r64_w_game5, r64_w_game6, 32, points_dict, [])
    r32_w_game4 = sim_game(r64_w_game7, r64_w_game8, 32, points_dict, [])

    # Sweet 16
    r16_w_game1 = sim_game(r32_w_game1, r32_w_game2, 16, points_dict, [])
    r16_w_game2 = sim_game(r32_w_game3, r32_w_game4, 16, points_dict, [])

    # Elite 8
    west_winner = sim_game(r16_w_game1, r16_w_game2, 8, points_dict, [])

    ##### Midwest Region #####
    # Round of 64
    r64_mw_game1 = sim_game(illinois, drexel, 64, points_dict, [])
    r64_mw_game2 = sim_game(loyola_chicago, georgia_tech, 64, points_dict, [])
    r64_mw_game3 = sim_game(tennessee, oregon_state, 64, points_dict, [])
    r64_mw_game4 = sim_game(oklahoma_state, liberty, 64, points_dict, [])
    r64_mw_game5 = sim_game(san_diego_state, syracuse, 64, points_dict, [])
    r64_mw_game6 = sim_game(west_virginia, morehead_state, 64, points_dict, [])
    r64_mw_game7 = sim_game(clemson, rutgers, 64, points_dict, [])
    r64_mw_game8 = sim_game(houston, cleveland_state, 64, points_dict, [])

    # Round of 32
    r32_mw_game1 = sim_game(r64_mw_game1, r64_mw_game2, 32, points_dict, [])
    r32_mw_game2 = sim_game(r64_mw_game3, r64_mw_game4, 32, points_dict, [])
    r32_mw_game3 = sim_game(r64_mw_game5, r64_mw_game6, 32, points_dict, [])
    r32_mw_game4 = sim_game(r64_mw_game7, r64_mw_game8, 32, points_dict, [])

    # Sweet 16
    r16_mw_game1 = sim_game(r32_mw_game1, r32_mw_game2, 16, points_dict, [])
    r16_mw_game2 = sim_game(r32_mw_game3, r32_mw_game4, 16, points_dict, [])

    # Elite 8
    midwest_winner = sim_game(r16_mw_game1, r16_mw_game2, 8, points_dict, [])


    ##### East Region    #####
    # Round of 64
    r64_e_game1 = sim_game(michigan, east_firstfour_16, 64, points_dict, [])
    r64_e_game2 = sim_game(lsu, saint_bonaventure, 64, points_dict, [])
    r64_e_game3 = sim_game(colorado, georgetown, 64, points_dict, [])
    r64_e_game4 = sim_game(florida_state, unc_greensboro, 64, points_dict, [])
    r64_e_game5 = sim_game(byu, east_firstfour_11, 64, points_dict, [])
    r64_e_game6 = sim_game(texas, abilene_christian, 64, points_dict, [])
    r64_e_game7 = sim_game(connecticut, maryland, 64, points_dict, [])
    r64_e_game8 = sim_game(alabama, iona, 64, points_dict, [])

    # Round of 32
    r32_e_game1 = sim_game(r64_e_game1, r64_e_game2, 32, points_dict, [])
    r32_e_game2 = sim_game(r64_e_game3, r64_e_game4, 32, points_dict, [])
    r32_e_game3 = sim_game(r64_e_game5, r64_e_game6, 32, points_dict, [])
    r32_e_game4 = sim_game(r64_e_game7, r64_e_game8, 32, points_dict, [])

    # Sweet 16
    r16_e_game1 = sim_game(r32_e_game1, r32_e_game2, 16, points_dict, [])
    r16_e_game2 = sim_game(r32_e_game3, r32_e_game4, 16, points_dict, [])

    # Elite 8
    east_winner = sim_game(r16_e_game1, r16_e_game2, 8, points_dict, [])

    ##### South Region   #####
    # Round of 64
    r64_s_game1 = sim_game(baylor, hartford, 64, points_dict, [])
    r64_s_game2 = sim_game(north_carolina, wisconsin, 64, points_dict, [])
    r64_s_game3 = sim_game(villanova, winthrop, 64, points_dict, [])
    r64_s_game4 = sim_game(purdue, north_texas, 64, points_dict, [])
    r64_s_game5 = sim_game(texas_tech, utah_state, 64, points_dict, [])
    r64_s_game6 = sim_game(arkansas, colgate, 64, points_dict, [])
    r64_s_game7 = sim_game(florida, virginia_tech, 64, points_dict, [])
    r64_s_game8 = sim_game(ohio_state, oral_roberts, 64, points_dict, [])

    # Round of 32
    r32_s_game1 = sim_game(r64_s_game1, r64_s_game2, 32, points_dict, [])
    r32_s_game2 = sim_game(r64_s_game3, r64_s_game4, 32, points_dict, [])
    r32_s_game3 = sim_game(r64_s_game5, r64_s_game6, 32, points_dict, [])
    r32_s_game4 = sim_game(r64_s_game7, r64_s_game8, 32, points_dict, [])

    # Sweet 16
    r16_s_game1 = sim_game(r32_s_game1, r32_s_game2, 16, points_dict, [])
    r16_s_game2 = sim_game(r32_s_game3, r32_s_game4, 16, points_dict, [])

    # Elite 8
    south_winner = sim_game(r16_s_game1, r16_s_game2, 8, points_dict, [])

    # Final Four
    east_west_winner = sim_game(east_winner, west_winner, 4, points_dict, [])
    south_midwest_winner = sim_game(south_winner, midwest_winner, 4, points_dict, [])

    # Championship
    champion = sim_game(east_west_winner, south_midwest_winner, 2, points_dict, [])

    #print(f"Champion: {champion.name}, {champion.seed}")

    return points_dict, east_winner


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

def sim_many_tournaments(num_sims):
    ucla_east_wins = 0

    for _ in range(num_sims):
        east_winner = sim_tournament()[1]
        if(east_winner == ucla):
            ucla_east_wins += 1
    
    print(f"UCLA east wins: {ucla_east_wins}")
    print(f"UCLA east win%: {ucla_east_wins/num_sims * 100:0.3}")


# create team objects
drexel = Team("Drexel", "Nick", 16)
grand_canyon = Team("Grand Canyon", "Josh", 15)
ucla = Team("UCLA", "Josh", 11)
liberty = Team("Liberty", "Devan", 13)
oklahoma = Team("Oklahoma", "Joe", 8)
arkansas = Team("Arkansas", "Josh", 3)
houston = Team("Houston", "Joe", 2)
clemson = Team("Clemson", "Brant", 8)
colorado = Team("Colorado", "Josh", 5)
north_texas = Team("North Texas", "Josh", 13)
colgate = Team("Colgate", "Devan", 14)
oregon_state = Team("Oregon St.", "Nick", 12)
wisconsin = Team("Wisconsin", "Joe", 9)
north_carolina = Team("North Carolina", "Jeremy", 8)
connecticut = Team("Connecticut", "Brant", 7)
virginia_tech = Team("Virginia Tech", "Devan", 10)
saint_bonaventure = Team("St. Bonaventure", "Josh", 9)
gonzaga = Team("Gonzaga", "Jeremy", 1)
kansas = Team("Kansas", "Josh", 3)
lsu = Team("LSU", "Justin", 8)
oregon = Team("Oregon", "Nick", 7)
georgetown = Team("Georgetown", "Devan", 12)
purdue = Team("Purdue", "Joe", 4)
unc_greensboro = Team("UNC Greensboro", "Devan", 13)
winthrop = Team("Winthrop", "Josh", 12)
virginia = Team("Virginia", "Nick", 4)
drake = Team("Drake", "Nick", 11)
mount_saint_marys = Team("Mount St. Mary's", "Justin", 16)
florida = Team("Florida", "Devan", 4)
vcu = Team("VCU", "Brant", 10)
georgia_tech = Team("Georgia Tech", "Josh", 9)
rutgers = Team("Rutgers", "Joe", 10)
byu = Team("BYU", "Devan", 6)
baylor = Team("Baylor", "Jeremy", 1)
iowa = Team("Iowa", "Nick", 2)
maryland = Team("Maryland", "Josh", 10)
ohio = Team("Ohio", "Nick", 13)
michigan = Team("Michigan", "Devan", 1)
syracuse = Team("Syracuse", "Josh", 11)
texas_tech = Team("Texas Tech", "Brant", 6)
loyola_chicago = Team("Loyola Chicago", "Nick", 8)
san_diego_state = Team("San Diego St.", "Brant", 6)
illinois = Team("Illinois", "Justin", 1)
morehead_state = Team("Morehead St.", "Devan", 14)
wichita_state = Team("Wichita St.", "Nick", 11)
texas = Team("Texas", "Joe", 3)
west_virginia = Team("West Virginia", "Justin", 3)
eastern_washington = Team("Eastern Washington", "Josh", 14)
missouri = Team("Missouri", "Devan", 9)
oral_roberts = Team("Oral Roberts", "Brant", 15)
ucsb = Team("UC Santa Barbara", "Brant", 12)
tennessee = Team("Tennessee", "Joe", 5)
alabama = Team("Alabama", "Justin", 2)
creighton = Team("Creighton", "Brant", 5)
cleveland_state = Team("Cleveland St.", "Jeremy", 15)
norfolk_state = Team("Norfolk St.", "Josh", 16)
utah_state = Team("Utah St.", "Devan", 11)
ohio_state = Team("Ohio St.", "Brant", 2)
michigan_state = Team("Michigan St.", "Jeremy", 11)
iona = Team("Iona", "Joe", 15)
usc = Team("USC", "Devan", 6)
abilene_christian = Team("Abilene Christian", "Joe", 14)
villanova = Team("Villanova", "Devan", 5)
texas_southern = Team("Texas Southern", "Josh", 16)
florida_state = Team("Florida St.", "Brant", 4)
appalachian_state = Team("Appalachian St.", "Nick", 16)
hartford = Team("Hartford", "Nick", 16)
oklahoma_state = Team("Oklahoma St.", "Nick", 4)

sim_many_tournaments(1000)

'''
sim_many_tournaments(5000)
THICKNESS = 2.5
# plot density function for owners with non-zero variance
legend_list = []
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
'''
