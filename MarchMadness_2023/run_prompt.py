from lib.database import run_query
from lib.prompter import generate_response

if __name__ == '__main__':
    query = generate_response("When the winner of the tournament is Houston and the East region winner is Michigan State, what are the win percentages for each of the players?")[0]

    #replace new line characters with spaces

    query = query.replace('/n', ' ')
    #get rid of any string of triple quotes

    query = query.replace("'''", '')

    print(query + "\n")

    #run the query using run_query function from database.py
    df = run_query(query, fetch="one")
    print(df)