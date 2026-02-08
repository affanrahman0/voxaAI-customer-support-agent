from groq import Groq
from backend.config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def groq_llm(prompt):
    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        # model = "llama-3.1-8b-instant"
        messages=[
            {"role": "system", "content": "You are a customer support AI for an e-commerce platform."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content
