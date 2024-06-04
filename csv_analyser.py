import os
import pandas as pd
import streamlit as st
import pandas
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import matplotlib
import key


matplotlib.use('TkAgg') #using python tkinter API


# os.environ['OPENAI_API_KEY'] = key.key_openai
llm = OpenAI(temperature=0.7)
pandas_ai = PandasAI(llm)
st.title("Prompt Driven CSV Analyser")

uploaded_file = st.file_uploader('Upload a CSV file for analysis', type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head(3))

    prompt = st.text_area("Enter your prompt:")

    if st.button("Generate"):
        if prompt:
            with st.spinner('Generating Response...'):
            # st.write("Generating answer please wait...")
             st.write(pandas_ai.run(df, prompt=prompt))
        else:
            st.warning('Please enter a prompt')




