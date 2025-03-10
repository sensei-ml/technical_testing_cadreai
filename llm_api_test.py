import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
response = client.chat.completions.create(
    model='gpt-4o-mini-2024-07-18',
    messages=[
        {'role': 'user', 'content': 'write some funny'},
  ],
    temperature=0.1,
    stream=False
)

assistant_reply = response.choices[0].message.content