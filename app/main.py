import os
from flask import render_template
from flask import Flask, request
import GPTchat
from datetime import datetime

app = Flask(__name__)

conversation = []


@app.route('/')
def chat():
    return render_template('chat.html', conversation=conversation)


@app.route('/', methods=['POST'])
def receive_message():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = request.form['message']
    response = GPTchat.chat()
    conversation.append({'time': now, 'input': message, 'output': response})
    return render_template('chat.html', conversation=conversation)


@app.route('/chat', methods=['POST', "GET"])
def gpt_chat_api():
    if request.method == 'POST':
        return render_template('chat.html', response_text=GPTchat.chat())
    return render_template('chat.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8082)))
