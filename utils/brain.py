import os
from groq import Groq # type: ignore
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("groq_api_key")

client = Groq(api_key= api_key)

MODEL = "openai/gpt-oss-safeguard-20b"

def ask_ai(prompt):

    response = client.chat.completions.create(
        model = MODEL,
        messages= [
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    ai_response = response.choices[0].message.content

    return ai_response
