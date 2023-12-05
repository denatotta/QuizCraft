 


QuizCraft Documentation


Table of Contents
1.	Introduction
2.	System Requirements
3.	Design and Architecture
•	3.1 Backend Logic
•	3.2 Frontend Interface
4.	User Guide
•	4.1 Getting Started
•	4.2 Navigating the Application
5.	get_quiz_data Function
6.	Error Handling and Validation
7.	Additional Features
8.	Conclusion

 
Introduction
The MCQ Quiz Application is a cutting-edge educational tool that leverages the power of Python, Streamlit, Langchain, and the OpenAI Chat Completion API. It offers users an engaging and personalized quiz experience, enabling them to test their knowledge on various topics through dynamically generated questions.


System Requirements
•	Python 3.x: The programming language used for backend development.
•	Streamlit: An open-source app framework for rapid development.
•	Langchain: A library for building applications with language models.
•	OpenAI API Key: Required for accessing the OpenAI Chat Completion API.


Design and Architecture
Backend Logic
Integration of Technologies: The backend is powered by Python, utilizing Langchain and the OpenAI API for generating quiz content.
Dynamic Content Generation: The application dynamically generates quiz questions and answers based on the user's selected topic.
Structured Response Format: Ensures consistency and ease of processing for the quiz data.


Frontend Interface
User-Centric Design: Developed with Streamlit, the frontend boasts a user-friendly and interactive interface.
Intuitive Layout: Features a clear layout with a sidebar for author information and interactive quiz components.
Responsive Design: Ensures a seamless user experience across various devices.



User Guide
Getting Started
Installation: Users must have Python installed, along with Streamlit and Langchain. Access to the OpenAI API is essential.
Launch: The application is initiated through Streamlit, making it accessible via a web browser.


Navigating the Application
Topic Selection: Users input their desired quiz topic in a dedicated field.
Question Quantity: Users specify the number of questions for their quiz.
Completing the Quiz
Interaction: The quiz comprises multiple-choice questions generated based on the user's inputs.
Submission and Scoring: Upon completion, users submit their answers to receive an immediate score, along with a review of correct and incorrect responses.


________________________________________
get_quiz_data Function
The core of the quiz generation process is encapsulated in the get_quiz_data function. This function is responsible for interacting with the OpenAI Chat Completion API via Langchain to create the quiz content. Here's an overview of its logic and structure:

API Key Configuration:
The function begins by defining the OpenAI API key, which is crucial for authenticating and gaining access to the OpenAI services.
Dynamic Template Creation:
A template string is constructed dynamically based on the user's input for the topic ({topic}) and the number of questions ({number_of_questions}).
The template instructs the AI to generate quiz questions and answers in a specific format, tailored to the specified topic and number.
Template Structure:
The template is meticulously designed to ensure the AI's output is in the form of a Python list of lists.
Each inner list represents a question set, containing the question itself followed by one correct and three incorrect answers.



Langchain Integration:
The function utilizes SystemMessagePromptTemplate and HumanMessagePromptTemplate from Langchain to format the input and output for the AI.
A ChatPromptTemplate is created by combining the system and human message prompts.
An instance of LLMChain is initialized with the ChatOpenAI model and the prepared chat prompt.

Quiz Data Retrieval:
The function runs the chain with the provided input dictionary (containing the topic and number of questions) to generate the quiz data.
The output is a list of question sets, each adhering to the predefined structure.



Error Handling and Validation
Robust Error Management: The application includes comprehensive error handling for scenarios such as authentication failures and unexpected exceptions.
User Input Validation: Ensures that user inputs are valid and prompts corrective actions if necessary.

Additional Features
Welcome Toast: A friendly greeting for first-time users.
Resourceful Sidebar: Includes author information and helpful links.
Tutorial Availability: A video tutorial is available for user assistance.

Conclusion
This MCQ Quiz Application represents a fusion of modern technology and educational needs. It stands as a testament to innovative educational tools, providing a unique and interactive learning experience.

Done by: Dina Alomari
