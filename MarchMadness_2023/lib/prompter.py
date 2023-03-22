
import openai
from database import *


def prepare_prompt(prompt_text):
  prompt = f'''Here is a database table schema.
    Table: tourney_results
    Columns: Devan_pts, Jeremy_pts, Josh_pts, Justin_pts, Nick_pts, Joe_pts,
    Devan_win, Jeremy_win, Josh_win, Justin_win, Nick_win, Joe_win,
    west_winner text, west_winner_blowout integer, midwest_winner text, midwest_winner_blowout integer, east_winner text, east_winner_blowout integer, south_winner text, south_winner_blowout integer,
    south_east_winner text, south_east_winner_blowout integer, west_midwest_winner text, west_midwest_winner_blowout integer,
    final_winner text, final_winner_blowout

    The columns ending in _winner represent a team. A final four team (or Elite 8 winner) will be listed in any of:
    west_winner, midwest_winner, east_winner, south_winner
    A final four winner, or a team in the championship, will be in one of: south_east_winner, west_midwest_winner
    The final winner will be in the final_winner column.
    The team ids are as follows:
    oral_roberts, vcu, louisiana, northwestern, southeast_missouri_state, marquette, florida_atlantic, 
    tcu, texas, vermont, uc_santa_barbara, grand_canyon, arizona_state, providence, memphis, duke, 
    howard, boise_state, colgate, maryland, kentucky, alabama, fairleigh_dickinson, penn_state, 
    kansas_state, indiana, kent_state, auburn, northern_kentucky, furman, san_diego_state, 
    connecticut, nevada, west_virginia, illinois, baylor, pittsburgh, houston, xavier, 
    unc_asheville, texas_am, drake, michigan_state, iowa_state, kennesaw_state, mississippi_state,
    utah_state, ucla, texas_southern, saint_marys, miami, texas_am_corpus_christi, purdue, arizona, 
    creighton, usc, montana_state, arkansas, iowa, tennessee, princeton, north_carolina_state, gonzaga, 
    kansas, charleston, iona, virginia, missouri.
    Please make sure when you are using a team, that the team_id comes from the list above. 
    Please create a SQL query that answers the following question: {prompt_text}

  '''
  return prompt

def generate_response(prompt): # Initial message is system prompt in the form {"role": "system", "content": message}
    openai.api_key = KEY
    messages = []
    messages.append({"role": "system", "content": prepare_prompt(prompt)})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=300, # Changes how long the response is
        temperature=0.9, # Changes how creative the response is
    )
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})

    return reply, messages

query = generate_response("When the winner of the tournament is UConn, what percent of the time does Jeremy win")[0]

#replace new line characters with spaces

query = query.replace('/n', ' ')
#get rid of any string of triple quotes

query = query.replace("'''", '')

#run the query using run_query function from database.py

df = run_query(query)

print(df)