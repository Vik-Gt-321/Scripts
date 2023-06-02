### Familiarizing with the api. Free access has ended, so couldn't test.
import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")
response = openai.Completion.create(
engine="davinci",
prompt="Blog topics dealing with daily life living on Mars\n\n1.",
temperature=0.3,
max_tokens=2    ,
top_p=1,
frequency_penalty=0.5,
presence_penalty=0)
print(response)


# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai

openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)