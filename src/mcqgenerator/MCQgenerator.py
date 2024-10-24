import os
import json
import pandas as pd
import traceback
import PyPDF2
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file, get_table_data
from src.mcqgenerator.logger import logging

from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.callbacks import get_openai_callback

# Load environment variables from the .env file
load_dotenv()

# Access environment variable
KEY = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(openai_api_key=KEY, model_name="gpt-3.5-turbo", temperature=0.6)

QUIZ_TEMPLATE = """
Text:{text}
You are an expert MCQ maker. By giving above text, it is your job to \
create an exam  of {number} multiple choice questions for {subject} students in {difficulty_level} level. 
Make sure the questions are not repeated and check all the questions to be conforming the text as well.
Also make sure that the questions are in the field of mentioned above subject.
Make sure to format your response like  RESPONSE_JSON_TEMPTLATE below  and use it as a guide. \
Ensure to make {number} MCQs
### RESPONSE_JSON_TEMPLATE
{response_json_template}
"""

quiz_prompt = PromptTemplate(
    input_variables=["text","number","subject","difficulty_level","response_json_template"],
    template=QUIZ_TEMPLATE
)

quiz_chain = LLMChain(llm=llm, prompt=quiz_prompt, output_key="quiz", verbose=True)

EVALUATION_TEMPLATE = """
You are an expert in English grammar and writing. 
Review the Multiple Choice Quiz for {subject} students.
Analyze the question complexity in no more than 50 words.
If the quiz doesn’t match the students' cognitive and analytical abilities,\
update the questions and adjust the difficulty to suit them better.
Quiz_MCQs: {quiz}
Please check the quiz as an expert English writer:
"""
quiz_evaluation_prompt = PromptTemplate(
input_variables=["subject","quiz"],
template=EVALUATION_TEMPLATE
)

evaluation_chain = LLMChain(llm=llm, prompt=quiz_evaluation_prompt, output_key="evaluation", verbose=True)

generate_evaluate_quiz_chain = SequentialChain(chains=[quiz_chain, evaluation_chain], 
                                               input_variables=["text","number","subject","difficulty_level","response_json_template"],
                                               output_variables=["quiz","evaluation"], verbose=True)