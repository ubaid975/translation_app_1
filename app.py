import streamlit as st

import streamlit as st
import langchain
from langchain.prompts import PromptTemplate,ChatPromptTemplate


import os
from langchain_groq import ChatGroq
load_dotenv()
api_url = "http://your-chatgroq-model-api-endpoint.com"  # ChatGroq API endpoint
api=os.getenv('groq_api')




llm=ChatGroq(model='mixtral-8x7b-32768',api_key=api)


st.title("Translation App")
st.write("Made by Ubaid")

# Input text

languages = ["english", "france", "urdu", "punjabi", "hindi", "russain", "memon", "sindhi",'tamil','marathi']
  # Add more languages as needed
target_languages=[]
source_language = st.selectbox("Source Language", languages)
for i,var in enumerate(languages):
    if source_language!=var:
        target_languages.append(languages[i])



target_language = st.selectbox("Target Language",target_languages)

input_text = st.text_area("Enter text to translate:", height=200)
template="""Follwing Sentence Translate the {source} to {target} only {target}:{question}"""
chat_template=PromptTemplate.from_template(template=template)
chain=chat_template|llm
print(chain.invoke({'source':source_language,'target':target_language,'question':input_text}).content)



if st.button("Translate"):
    if input_text:
        try:
            translated_text = chain.invoke({'source':source_language,'target':target_language,'question':input_text}).content
            st.subheader("Translated Text:")
            print(translated_text)
            st.write(translated_text)
        except Exception as e:
            st.error(f"Error during translation: {e}")
    else:
        st.warning("Please enter text to translate.")
# Language selection



# Footer
st.markdown("---")
st.caption("Translation app built using Streamlit and LLM APIs.")




    
