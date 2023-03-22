from lib.database import run_query
from lib.prompter import generate_response

if __name__ == '__main__':
    #ask the user for a question
    while(True):
        question = input("Enter a question: ")
        answer = generate_response(question)[0]
        print(answer + "\n\n")