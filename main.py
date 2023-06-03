# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, jsonify
import openai, os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
	return 'Hello World'	

#response structure
# {
#     "choices": [
#         {
#             "finish_reason": "stop",
#             "index": 0,
#             "logprobs": null,
#             "text": "\n\nPython is a high-level programming language used for general-purpose programming. It is interpreted, object-oriented, and known for its simple, easy-to-learn syntax. Python is used for web development, software development, mathematics, system scripting, and media access."
#         }
#     ],
#     "created": 1685788111,
#     "id": "cmpl-7NImlrdZnImP2TZOVyg1psezLGlnk",
#     "model": "text-davinci-003",
#     "object": "text_completion",
#     "usage": {
#         "completion_tokens": 57,
#         "prompt_tokens": 4,
#         "total_tokens": 61
#     }
# }

def gpt_generate_response_api(prompt):
	start_sequence = "\nAI:"
	restart_sequence = "\nHuman: "

	openai.api_key = os.getenv('OPEN_API_KEY')

	response = openai.Completion.create(
	model="text-davinci-003",
	prompt=prompt,
	temperature=0.9,
	max_tokens=150,
	top_p=1,
	frequency_penalty=0,
	presence_penalty=0.6,
	stop=[" Human:", " AI:"]
	)
	return response

# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run()
