import os
import json
import PyPDF2
import traceback

def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader=PyPDF2.PdfReader(file)
            text=""
            for page in pdf_reader.pages:
                text+=page.extract_text()
            return text
            
        except Exception as e:
            raise Exception("error reading the PDF file")
        
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    
    else:
        raise Exception(
            "unsupported file format only pdf and text file suppoted"
            )
    
def get_table_data(quiz_str):
    try:
        # convert the quiz from a str to dict
        quiz_dict=json.loads(quiz_str)
        print(f"quiz dict in utils {quiz_dict}")
        quiz_table_data=[]
        
        # iterate over the quiz dictionary and extract the required information
        for key,value in quiz_dict.items():
            mcq=value["mcq"]
            choices=" || ".join([
                    f"{choice}:{choice_value}" for choice, choice_value in value["choices"].items()
                 ])
            
            correct=value["correct"]
            quiz_table_data.append({"MCQ": mcq, "Choices": choices, "Correct": correct})
        
        return quiz_table_data
        
    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        return False