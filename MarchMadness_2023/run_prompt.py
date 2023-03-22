from lib.database import run_query
from lib.prompter import generate_response

if __name__ == '__main__':
    #ask the user for a question
    while(question := input("Enter a question: ")):
        if question == "exit":
            break
        answer = generate_response(question)[0]
        
        if(answer): print(f"{answer}\n\n")
    