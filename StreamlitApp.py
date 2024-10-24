import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file, get_table_data
import streamlit as st
from langchain.callbacks import get_openai_callback
from src.mcqgenerator.MCQgenerator import generate_evaluate_quiz_chain
from src.mcqgenerator.logger import logging

with open('/home/aliaf/genai/mcqgen/Resp_temp.json','r') as file:
    response_template = json.load(file)

# Title of the app
st.title("📝 MCQ Generator with LangChain 🔗")

# Form in streamlit
with st.form("user_inputs"):
    # Upload a file
    uploaded_file = st.file_uploader("Upload a pdf or txt file")

    # Input number of questions
    question_count = st.number_input("Number of questions", min_value=1, max_value=20)

    # Input subject
    subject = st.text_input("Subject", max_chars=30)

    # Quiz difficulty level
    level = st.text_input("Difficulty level of questions", max_chars=30, placeholder="Simple")

    # Add submit button
    button = st.form_submit_button("Create questions")

if button and uploaded_file is not None and question_count and subject and level:
    with st.spinner("Please wait. Loading ..."):
        try:
            text = read_file(uploaded_file)
            # Count number of tokens and the cost of API
            with get_openai_callback() as cb:
                response = generate_evaluate_quiz_chain(
                    {
                    "text":text,
                    "number":question_count,
                    "subject":subject,
                    "difficulty_level":level,
                    "response_json_template":json.dumps(response_template)
                    }
                    )
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)
            st.error("Error")
        else:
            print(f"Total cost : {cb.total_cost}")
            print(f"Input tokens : {cb.prompt_tokens}")
            print(f"Output tokens : {cb.completion_tokens}")
            print(f"Total tokens : {cb.total_tokens}")
            if isinstance(response, dict):
                # Get evaluated quiz
                quiz = response.get("quiz", None)
                if quiz is not None:
                    table_data = get_table_data(quiz)
                    print(f"11 {table_data}")
                    if table_data is not None:
                        print(table_data)
                        df = pd.DataFrame(table_data)
                        df.index += 1
                        st.table(df)
                        st.text_area(label="Review", value=response["evaluation"])
                    else:
                        st.error("Error")
            else:
                st.write(response)



        