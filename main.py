# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, jsonify
import openai, os, json
from datetime import datetime
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/buddy'
db = SQLAlchemy(app)

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

class Chat(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	role = db.Column(db.String(255))
	user_id = db.Column(db.String(255))
	thread_id = db.Column(db.String(255))
	content = db.Column(db.Text)
	created_at = db.Column(db.DateTime)
	updated_at = db.Column(db.DateTime)

@app.route('/dummy_record')
def dummy_record():
	new_chat = Chat(role='admin', user_id='123', thread_id='456', content='Sample content', created_at=datetime.now(), updated_at=datetime.now())
	db.session.add(new_chat)
	db.session.commit()
	first_row = Chat.query.first()
	data = {
        'id': first_row.id,
        'role': first_row.role,
        'user_id': first_row.user_id,
        'thread_id': first_row.thread_id,
        'content': first_row.content,
        'created_at': first_row.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        'updated_at': first_row.updated_at.strftime('%Y-%m-%d %H:%M:%S')
    }
	return json.dumps(data)

# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run()
