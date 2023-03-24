from flask import Flask, request

from lib.prompter import generate_response

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello!"

# make an API endpoint that accepts GET requests
@app.route('/run_prompt/<question>', methods=["GET"])
def run_prompt(question):
    # print the request type
    print(f"Received {request.method} request for question: {question}")

    return { "answer": generate_response(question)[0] }


if __name__ == '__main__':
    app.run(debug=False, port=5174)
