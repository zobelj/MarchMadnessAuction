from lib.database import run_query
from lib.prompter import generate_response

if __name__ == '__main__':
    answer = generate_response("When the winner of the tournament is Houston and the East region winner is Michigan State, what are the win percentages for each of the players?")[0]
    print(answer)