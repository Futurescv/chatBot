import os

import openai
from flask import request

# Initialize the OpenAI API key


def chat_method():
    while True:
        # Get the user's input
        user_input = input("你: ")

        # Generate a response from GPT-3
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt="你: " + user_input,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        ).choices[0].text

        # Extract the first sentence from the response
        # Print the response
        print(response)


def chat():
    message = request.form['message']

    # openai.api_key = os.environ['API_KEY']
    key_front = "sk-h3nxTq5ZCYzLOLc"
    key_end = "K9l4aT3BlbkFJ9O0VyxyCMlTvMSCZz34w"
    openai.api_key = key_front+key_end

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt='你: ' + message,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response['choices'][0]['text']
