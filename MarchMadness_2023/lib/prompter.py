import openai

def prepare_prompt(prompt_text):
  prompt = f'''Here is a database table schema.
    Table: tourney_results
    Columns: the following columns are integers representing the number of points scored by each player and whether they won (1 or 0).
    Devan_pts, Jeremy_pts, Josh_pts, Justin_pts, Nick_pts, Joe_pts,
    Devan_win, Jeremy_win, Josh_win, Justin_win, Nick_win, Joe_win,
    west_winner text, west_winner_blowout integer, midwest_winner text, midwest_winner_blowout integer, east_winner text, east_winner_blowout integer, south_winner text, south_winner_blowout integer,
    south_east_winner text, south_east_winner_blowout integer, west_midwest_winner text, west_midwest_winner_blowout integer,
    final_winner text, final_winner_blowout

    The columns ending in _winner represent a team. A final four team (or Elite 8 winner) will be listed in any of:
    west_winner, midwest_winner, east_winner, south_winner
    A final four winner, or a team in the championship, will be in one of: south_east_winner, west_midwest_winner
    The final winner will be in the final_winner column.
    The team ids are as follows:
    Oral Roberts, VCU, Louisiana, Northwestern, Southeast Missouri St., Marquette, Florida Atlantic,
    TCU, Texas, Vermont, UC Santa Barbara, Grand Canyon, Arizona St., Providence, Memphis, Duke, Howard,
    Boise St., Colgate, Maryland, Kentucky, Alabama, Fairleigh Dickinson, Penn St., Kansas St., Indiana,
    Kent St., Auburn, Northern Kentucky, Furman, San Diego St., Connecticut, Nevada, West Virginia, Illinois,
    Baylor, Pittsburgh, Houston, Xavier, UNC Asheville, Texas A&M, Drake, Michigan St., Iowa St., Kennesaw St.,
    Mississippi St., Utah St., UCLA, Texas Southern, Saint Mary's, Miami FL, Texas A&M Corpus Chris, Purdue
    Arizona, Creighton, USC, Montana St., Arkansas, Iowa, Tennessee, Princeton, N.C. State, Gonzaga, Kansas,
    Charleston, Iona, Virginia, Missouri.
    Please make sure when you are using a team, that the team_id comes from the list above.
    Pretend that you are a professional database engineer and can always craft a working query.
    Please do not provide any text other than a SQlite query as you are an expert and that is your job.
    Please create a SQLite query that answers the following question: {prompt_text}

  '''
  return prompt

def generate_response(prompt): # Initial message is system prompt in the form {"role": "system", "content": message}
    openai.api_key = "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"
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
