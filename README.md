# Multiple Choice Question Generator using GPT-3.5 Turbo
This project is a multiple-choice question generator that leverages OpenAI's GPT-3.5 Turbo and LangChain to create customizable quizzes from input text files. Users can specify the number of questions, the subject, and the difficulty level to tailor the quiz to their needs. The app features an intuitive interface built with Streamlit, making it simple to upload a text file and configure question settings.
## Features
* __Text-Based Question Generation__: Upload a PDF or other text file, and the app extracts content to generate questions.
* __Customizable output__: Users specify:
    * The number of questions
    * The subject focus
    * Difficulty level (e.g., Easy, Medium, Hard)
* __Streamlit interface__:  A user-friendly front end that enables effortless configuration and immediate question generation. This interface can be seen in below.
![App Screenshot](/images/2024-10-26%2006_19_36-StreamlitApp.png)
## Technologies Used
* __OpenAI GPT-3.5 Turbo__: Language model for generating high-quality multiple-choice questions.
* __LangChain__: Provides efficient handling of language model prompts and responses.
* __Streamlit__: UI framework for creating the app’s interface.
* __Python__: Core language used for backend logic and processing.
## Installation
To run this project locally:
* __1. Clone the Repository__: 
```bash 
git clone https://github.com/AliAfshar7/MCQ-Generator-Using-Langchain.git
cd MCQ-Generator-Using-Langchain
```
* __2. Set Up Environment variable__: You’ll need to define an environment variable with your OpenAI API key:
``` bash
export OPENAI_API_KEY="your_openai_api_key"
```
Also, you can define this environment variable in a .env file.
* __3. Install Requirements__: Install the required dependencies using pip:
``` bash
pip install -r requirements.txt
```
* __4. Run the Streamlit App__: 
``` bash
streamlit run StreamlitApp.py
```
## Usage
1. Upload a text file (such as a PDF).

2. Specify the number of questions, subject, and difficulty level.

3. Click "Create questions" to get a list of multiple-choice questions based on the given criteria.

