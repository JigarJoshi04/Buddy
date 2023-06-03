# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, jsonify
import openai, os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
from flaskext.mysql import MySQL

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
mysql = MySQL()

# Initialise database
def initialise_database():
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_DB'] = 'buddy'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    mysql.init_app(app)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.

@app.route('/')
def hello_world():
	return 'Hello World'	

# API response structure
# {
#   "choices": [
#     {
#       "finish_reason": "stop",
#       "index": 0,
#       "message": {
#         "content": "Orange who?",
#         "role": "assistant"
#       }
#     }
#   ],
#   "created": 1679718435,
#   "id": "chatcmpl-6xpmlDodtW6RwiaMaC1zhLsR8Y1D3",
#   "model": "gpt-3.5-turbo-0301",
#   "object": "chat.completion",
#   "usage": {
#     "completion_tokens": 3,
#     "prompt_tokens": 39,
#     "total_tokens": 42
#   }
# }


def gpt_generate_response_api(prompt):
	start_sequence = "\nAI:"
	restart_sequence = "\nHuman: "

	

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
	initialise_database()

	# run() method of Flask class runs the application
	# on the local development server.
	app.run()
