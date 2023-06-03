# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request
from datetime import datetime
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from preprocessor import PreProcessor
from openAI import OpenAI

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/buddy'
db = SQLAlchemy(app)	

class Chat(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	role = db.Column(db.String(255))
	user_id = db.Column(db.String(255))
	age_category = db.Column(db.String(255))
	emotion = db.Column(db.String(255))
	content = db.Column(db.Text)
	created_at = db.Column(db.DateTime)
	updated_at = db.Column(db.DateTime)

@app.route('/new_message')
def new_message():
	role = 'user'
	user_id = request.args.get('user_id')
	age_category = request.args.get('age_category')
	emotion = request.args.get('emotion')
	content = request.args.get('content')

	save_chat(role, user_id, age_category, emotion, content)

	message_obj_list = fetch_all_conversation_of_a_user(user_id)
	messages = PreProcessor.prepare_messages(message_obj_list)
	ai_response = OpenAI.chat_completion_api(messages)
	return ai_response

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

def fetch_all_conversation_of_a_user(user_id):
	return Chat.query.filter_by(user_id=user_id).all()

def save_chat(role, user_id, age_category, emotion, content):
	new_chat = Chat(role=role, user_id=user_id, age_category=age_category, emotion=emotion,content=content, created_at=datetime.now(), updated_at=datetime.now())

	db.session.add(new_chat)
	db.session.commit()

# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run()
