from flask import Flask, request, jsonify, session
from pymongo import MongoClient
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# MongoDB setup
client = MongoClient('mongodb://localhost:27017/')
db = client.chatbot_db
conversations = db.conversations

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    user_id = session.get('user_id', None)

    if not user_id:
        user_id = str(os.urandom(16))
        session['user_id'] = user_id

    # Save the user input to the database
    conversation = {
        'user_id': user_id,
        'message': user_input,
        'timestamp': datetime.utcnow()
    }
    conversations.insert_one(conversation)

    # Generate a response (you can replace this with your actual chatbot logic)
    response = generate_response(user_input, user_id)

    return jsonify({'response': response})

def generate_response(user_input, user_id):
    # Retrieve past conversations of the user
    past_conversations = list(conversations.find({'user_id': user_id}).sort('timestamp'))

    # For demo purposes, we'll just echo the input back
    # You can replace this with more sophisticated logic
    return f"You said: {user_input}. Your previous message was: {past_conversations[-2]['message'] if len(past_conversations) > 1 else 'This is your first message.'}"

if __name__ == '__main__':
    app.run(debug=True)
