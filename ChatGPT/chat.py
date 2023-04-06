import os
import openai


openai.api_key = os.environ.get("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hi ChatGPT. Say hi back!"}],
)
answer = response.choices[0].message.content
print(answer)
