from flask import Flask, request

from lib.prompter import generate_response

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello!"

@app.route("/run_prompt")
def run_prompt():
    # generate a response given the question in the request
    question = request.args.get('question')
    answer = generate_response(question)[0]

    return {"answer": answer}


if __name__ == '__main__':
    app.run(debug=True, port=5174)