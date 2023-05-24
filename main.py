import os

import streamlit as st
from dotenv import load_dotenv
from langchain.document_loaders import YoutubeLoader


def get_youtube_transcript(video_url):
  loader = YoutubeLoader.from_youtube_url(video_url, add_video_info=True)
  data = loader.load()

  st.subheader(data[0].metadata["title"])
  st.subheader(video_url)

  st.write("Author : ", data[0].metadata["author"])
  st.write("Content")
  st.write(data[0].page_content)




if __name__ == '__main__':
  # load_dotenv()
  # OPENAI_ENV_KEY = os.environ["OPENAI_API_KEY"]
  # print(OPENAI_ENV_KEY)
  st.header("Youtube Script Loader")
  video_url = st.text_input(label="youtube url", 
                placeholder="enter youtube video url", 
                help="https://www.youtube.com/watch?v=dtmJMLWI91y",
              )
  
  if len(video_url) > 0:
    get_youtube_transcript(video_url)
  
