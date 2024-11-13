import os
from dotenv import load_dotenv
import google.generativeai as genai
from openai import OpenAI

load_dotenv()
#%%
# Exercise 2
"""
Make a code debugging app using gemini api

input == code snippet
output == explanation                

use openai API
"""
code_snippet = """
response = model.generate_content("How is tea made?",
                                  generation_config=genai.types.GenerationConfig(
                                      max_output_tokens=10))
"""

client = OpenAI(api_key = os.environ.get("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model = 'gpt-4o-mini',
    messages=[
        {'role':'system','content':'You are to help me explain/debug this code within 1 paragraph'},
        {'role':'user','content':code_snippet}
    ]
)

print(response.choices[0].message.content)
#%%