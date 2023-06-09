import pandas as pd

class Team():
    def __init__(self, name, owner, seed):
        self.owner = owner
        self.name = name
        self.seed = seed
        self.adjO = df.loc[name, "AdjOE"]
        self.adjD = df.loc[name, "AdjDE"]
        self.pts = 0
        self.championships = 0
        

# read in the excel file of kenpom data
df = pd.read_csv("data/summary2.csv")
df.set_index("TeamName", inplace=True)


# create team objects
oral_roberts = Team("Oral Roberts", "Josh", 12)
vcu = Team("VCU", "Brant", 12)
louisiana = Team("Louisiana", "Justin", 13)
northwestern = Team("Northwestern", "Josh", 7)
southeast_missouri_state = Team("Southeast Missouri St.", "Jeremy", 16)
marquette = Team("Marquette", "Brant", 2)
florida_atlantic = Team("Florida Atlantic", "Josh", 9)
tcu = Team("TCU", "Justin", 6)
texas = Team("Texas", "Joe", 2)
vermont = Team("Vermont", "Devan", 15)
uc_santa_barbara = Team("UC Santa Barbara", "Nick", 14)
grand_canyon = Team("Grand Canyon", "Justin", 14)
arizona_state = Team("Arizona St.", "Nick", 11)
providence = Team("Providence", "Jeremy", 11)
memphis = Team("Memphis", "Devan", 8)
duke = Team("Duke", "Nick", 5)
howard = Team("Howard", "Devan", 16)
boise_state = Team("Boise St.", "Justin", 10)
colgate = Team("Colgate", "Nick", 15)
maryland = Team("Maryland", "Nick", 8)
kentucky = Team("Kentucky", "Brant", 6)
alabama = Team("Alabama", "Nick", 1)
fairleigh_dickinson = Team("Fairleigh Dickinson", "Jeremy", 16)
penn_state = Team("Penn St.", "Joe", 10)
kansas_state = Team("Kansas St.", "Justin", 3)
indiana = Team("Indiana", "Jeremy", 4)
kent_state = Team("Kent St.", "Nick", 13)
auburn = Team("Auburn", "Josh", 9)
northern_kentucky = Team("Northern Kentucky", "Joe", 16)
furman = Team("Furman", "Josh", 13)
san_diego_state = Team("San Diego St.", "Devan", 5)
connecticut = Team("Connecticut", "Jeremy", 4)
nevada = Team("Nevada", "Nick", 11)
west_virginia = Team("West Virginia", "Joe", 9)
illinois = Team("Illinois", "Josh", 9)
baylor = Team("Baylor", "Justin", 3)
pittsburgh = Team("Pittsburgh", "Jeremy", 11)
houston = Team("Houston", "Devan", 1)
xavier = Team("Xavier", "Jeremy", 3)
unc_asheville = Team("UNC Asheville", "Josh", 15)
texas_am = Team("Texas A&M", "Josh", 7)
drake = Team("Drake", "Brant", 12)
michigan_state = Team("Michigan St.", "Joe", 7)
iowa_state = Team("Iowa St.", "Josh", 6)
kennesaw_state = Team("Kennesaw St.", "Jeremy", 14)
mississippi_state = Team("Mississippi St.", "Justin", 11)
utah_state = Team("Utah St.", "Devan", 10)
ucla = Team("UCLA", "Devan", 2)
texas_southern = Team("Texas Southern", "Jeremy", 16)
saint_marys = Team("Saint Mary's", "Josh", 5)
miami = Team("Miami FL", "Nick", 5)
texas_am_corpus_christi = Team("Texas A&M Corpus Chris", "Jeremy", 16)
purdue = Team("Purdue", "Joe", 1)
arizona = Team("Arizona", "Brant", 2)
creighton = Team("Creighton", "Nick", 6)
usc = Team("USC", "Josh", 10)
montana_state = Team("Montana St.", "Nick", 14)
arkansas = Team("Arkansas", "Joe", 8)
iowa = Team("Iowa", "Joe", 8)
tennessee = Team("Tennessee", "Josh", 4)
princeton = Team("Princeton", "Justin", 15)
north_carolina_state = Team("N.C. State", "Joe", 11)
gonzaga = Team("Gonzaga", "Brant", 3)
kansas = Team("Kansas", "Jeremy", 1)
charleston = Team("Charleston", "Josh", 12)
iona = Team("Iona", "Justin", 13)
virginia = Team("Virginia", "Justin", 4)
missouri = Team("Missouri", "Justin", 7)

team_list = [oral_roberts, vcu, louisiana, northwestern, southeast_missouri_state, marquette, florida_atlantic, tcu, texas, vermont, uc_santa_barbara, grand_canyon, arizona_state, providence, memphis, duke, howard, boise_state, colgate, maryland, kentucky, alabama, fairleigh_dickinson, penn_state, kansas_state, indiana, kent_state, auburn, northern_kentucky, furman, san_diego_state, connecticut, nevada, west_virginia, illinois, baylor, pittsburgh, houston, xavier, unc_asheville, texas_am, drake, michigan_state, iowa_state, kennesaw_state, mississippi_state, utah_state, ucla, texas_southern, saint_marys, miami, texas_am_corpus_christi, purdue, arizona, creighton, usc, montana_state, arkansas, iowa, tennessee, princeton, north_carolina_state, gonzaga, kansas, charleston, iona, virginia, missouri]
