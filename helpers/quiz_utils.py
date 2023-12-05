import random
import ast
import streamlit as st


#to_be_replaced_with_something_else
def string_to_list(s):
    try:
        print(s)
        quiz_list = ast.literal_eval(s)
        return quiz_list
    except (SyntaxError, ValueError) as e:
        st.error(f"Error: The provided input is not correctly formatted. {e}")
        st.stop()

def get_randomized_options(options):
    correct_answer = options[0]
    random.shuffle(options)
    return options, correct_answer