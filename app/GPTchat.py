import openai
import re


# Initialize the OpenAI API key
openai.api_key = "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"

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