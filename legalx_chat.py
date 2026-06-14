
from legalx_backend import retrieve
from google import genai
import os

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


def ask_question(q):

    chunks = retrieve(q)
    context = "\n\n".join(chunks)

    prompt = f"""
Answer only using context.

CONTEXT:
{context}

QUESTION:
{q}
"""

    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=prompt
    )

    return response.text
