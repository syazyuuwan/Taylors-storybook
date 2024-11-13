import streamlit as st
from openai import OpenAI


client = OpenAI(api_key=st.secrets['OPENAI_API_KEY'])

def story_generator(prompt):
  system_prompt = """You are a world renowned storyteller.
  You are famous for writing short mystery stories for ages between 12-16.
  You will be provided with a concept or setting to write a proper story with fitting themes
  """

  response = client.chat.completions.create(
      model = 'gpt-4o-mini',
      messages = [
          {"role":"system",
           "content":system_prompt},
          {"role":"user",
           "content":prompt}
      ]
  )
  return response.choices[0].message.content

def cover_generator(prompt):
  response = client.images.generate(
      model = 'dall-e-2',
      prompt=prompt,
      size = '512x512',
      n=1
  )
  return response.data[0].url

def cover_prompt(story):
  system_prompt = """You will be given a full story to shorten into about
                      1000 tokens to fit into the dall e 2 model.
                    Generate a prompt that results in a highly relevant image"""
  response = client.chat.completions.create(
      model = 'gpt-4o-mini',
      messages = [
          {"role":"system",
           "content":system_prompt},
          {"role":"user",
           "content":story}
      ]
  )
  return response.choices[0].message.content

def storybook(prompt):
  story = story_generator(prompt)
  cover = cover_generator(cover_prompt(story))

  #Display image and story
  st.image(cover)
  st.write(story)
  
#Text input and UI
prompt = st.text_input("Give me a concept")
#Button to start generating
if st.button("Generate"):
    with st.spinner():
      storybook(prompt)
    