import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.chains import LLMChain


def get_quiz_data(topic, number_of_questions):

    openai_api_key = ''

    template = f"""
You are a helpful assistant programmed to generate questions based on any topic ({topic}) provided. You're tasked with designing a quiz contain specific number of questions ({number_of_questions}) and they need to be distinct questions. Each of these questions will be accompanied by 4 possible answers: one correct answer and three incorrect ones.

For clarity and ease of processing, please structure your response in a way that emulates a Python list of lists.

Your output MUST be shaped as follows:

1. An outer list that contains a number equals to the {number_of_questions} inner lists.
2. Each inner list represents a set of question and answers, and contains exactly 5 strings in this order:
   - The generated question.
   - The correct answer.
   - The first incorrect answer.
   - The second incorrect answer.
   - The third incorrect answer.

Your output MUST mirror this structure:
[
    ["Generated Question 1", "Correct Answer 1", "Incorrect Answer 1.1", "Incorrect Answer 1.2", "Incorrect Answer 1.3"],
    ["Generated Question 2", "Correct Answer 2", "Incorrect Answer 2.1", "Incorrect Answer 2.2", "Incorrect Answer 2.3"],
    ["Generated Question 3", "Correct Answer 3", "Incorrect Answer 3.1", "Incorrect Answer 3.2", "Incorrect Answer 3.3"]
    ........... so on, so forth.
]

It is a must that you adhere to this format as it's optimized for further Python processing. No additional text to be added.
"""
    try:
        input_dict = {
            'topic': topic,
            'number_of_questions': number_of_questions
        }

        system_message_prompt = SystemMessagePromptTemplate.from_template(template)
        human_message_prompt = HumanMessagePromptTemplate.from_template('{topic}')
        chat_prompt = ChatPromptTemplate.from_messages(
            [system_message_prompt, human_message_prompt]
        )
        chain = LLMChain(
            llm=ChatOpenAI(openai_api_key=openai_api_key),
            prompt=chat_prompt
        )
        return chain.run(input_dict)
    except Exception as e:
        if "AuthenticationError" in str(e):
            st.error("Incorrect API key provided. Please check and update your API key.")
            st.stop()
        else:
            st.error(f"An error occurred: {str(e)}")
            st.stop()