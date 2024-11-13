import os
from dotenv import load_dotenv
import google.generativeai as genai
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key = os.environ.get("OPENAI_API_KEY"))

#Base for chat generation
response = client.chat.completions.create(
    #Set model
    model='gpt-4o-mini',
    #prompts for API. Must start with system.
    messages=[
        {"role":"system",
         "content":"""You are mathematics teacher giving lessons 
         to 12 year old students. You will be given a topic and design
         a 2-week lesson plan based on the topic.
         The lesson plan should include:
         1. Sub topics
         2. Suggested time spent
         
         Here is the output format:
         ----------------------
         |Sub topic 1 | 2 hours |
         ----------------------"""},
        {"role":"user",
         "content":"Fractions"},
        {"role":"assistant",
         "content":""""
         ----------------------------
         | Week 1                    |
         ----------------------------
         |Proper fractions | 1 hr    |
         ----------------------------
         | More topics here | 1 her  |
         ----------------------------
         | Week 2                    |
         ----------------------------
         |Improper Fractions         |
         ----------------------------
         """},
        {"role":"user",
         "content":"imaginary numbers"}
    ]
)

print(response.choices[0].message.content)