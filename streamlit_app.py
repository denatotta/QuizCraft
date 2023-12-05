import streamlit as st
from helpers.openai_utils import get_quiz_data
from helpers.quiz_utils import string_to_list, get_randomized_options
from helpers.toast_messages import get_random_toast


st.set_page_config(
    page_title="PWC QuizMaker",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Check if user is new or returning using session state.
# If user is new, show the toast message.
if 'first_time' not in st.session_state:
    message, icon = get_random_toast()
    st.toast(message, icon=icon)
    st.session_state.first_time = False

with st.sidebar:
    st.header("👨‍💻 About the Author")
    st.write("""
    **Dina Alomari** is an AI enthusias. Driven by passion and a love for this field, she's created this platform to make learning more interactive and fun.
    """)

    st.divider()
    st.subheader("🔗 Connect with Me", anchor=False)
    st.markdown(
        """
        - [🐙 Source Code](https://github.com/Sven-Bo/streamlit-quiztube)
        - [🎥 YouTube Channel](https://www.youtube.com/watch?v=-NOUOl5ddX0)
        - [🌐 Personal Website](https://denatotta.github.io/DinaOmari/)
        - [👔 LinkedIn](https://www.linkedin.com/in/dina-alomari-621585202/)
        """
    )

    st.divider()
    st.subheader("🏆 PWC Internship 2024", anchor=False)
    st.write("PWC QuizMaker, crafted with Python, Langchain, and Streamlit, offers an interactive quiz experience, enabling users to engage in custom-topic quizzes generated through the OpenAI Chat Completion API")

    st.divider()
    st.write("Made with ♥ by Dina Al Omari")



st.title(":red[QuizCraft] — Dive In. Learn. Compete. 🧠", anchor=False)
st.write("""
Have you learned about a new topic and want to know how much you understand? Try this fun way: Join **QuizCraft** and check your knowledge!

**What to do?** 🤓
1. Write the new topic you learned.
2. Choose how many questions you want.

⚠️ Remember: The number of questions must be a full number, like 5 or 10.

After you tell us these details, start answering special questions made for you. These questions help you know if you really understand the topic. Let's start and see how much you know!
""")

with st.expander("💡 Video Tutorial"):
    with st.spinner("Loading video.."):
        st.video("https://youtu.be/-NOUOl5ddX0", format="video/mp4", start_time=0)

with st.form("user_input"):
    TOPIC = st.text_input("Enter your favourite Topic:", value="AI")
    NUMBER_OF_QUESTIONS = st.text_input("Enter number of questions:", placeholder="5")
    submitted = st.form_submit_button("Craft my quiz!")

if submitted or ('quiz_data_list' in st.session_state):
    if not TOPIC:
        st.info("Please provide a valid Topic.")
        st.stop()
    elif not NUMBER_OF_QUESTIONS:
        st.info("Please enter a valid number.")
        st.stop()
        
    with st.spinner("Crafting your quiz...🤓"):
        if submitted:
            st.session_state.clear()
            quiz_data_str = get_quiz_data(TOPIC, NUMBER_OF_QUESTIONS)
            st.session_state.quiz_data_list = string_to_list(quiz_data_str)

            if 'user_answers' not in st.session_state:
                st.session_state.user_answers = [None for _ in st.session_state.quiz_data_list]
            if 'user_answers' in st.session_state and len(st.session_state.user_answers) < int(NUMBER_OF_QUESTIONS):
                st.session_state.user_answers = [None for _ in st.session_state.quiz_data_list]
            if 'correct_answers' not in st.session_state:
                st.session_state.correct_answers = []
            if 'randomized_options' not in st.session_state:
                st.session_state.randomized_options = []

            for q in st.session_state.quiz_data_list:
                options, correct_answer = get_randomized_options(q[1:])
                st.session_state.randomized_options.append(options)
                st.session_state.correct_answers.append(correct_answer)

        with st.form(key='quiz_form'):
            st.subheader("🧠 Quiz Time: Test Your Knowledge!", anchor=False)
            for i, q in enumerate(st.session_state.quiz_data_list):
                options = st.session_state.randomized_options[i]
                default_index = st.session_state.user_answers[i] if st.session_state.user_answers[i] is not None else 0
                response = st.radio(q[0], options, index=default_index)
                user_choice_index = options.index(response)
                st.session_state.user_answers[i] = user_choice_index  # Update the stored answer right after fetching it


            results_submitted = st.form_submit_button(label='Unveil My Score!')

            if results_submitted:
                score = sum([ua == st.session_state.randomized_options[i].index(ca) for i, (ua, ca) in enumerate(zip(st.session_state.user_answers, st.session_state.correct_answers))])
                st.success(f"Your score: {score}/{len(st.session_state.quiz_data_list)}")

                if score == len(st.session_state.quiz_data_list):  # Check if all answers are correct
                    st.balloons()
                else:
                    incorrect_count = len(st.session_state.quiz_data_list) - score
                    if incorrect_count == 1:
                        st.warning(f"Almost perfect! You got 1 question wrong. Let's review it:")
                    else:
                        st.warning(f"Almost there! You got {incorrect_count} questions wrong. Let's review them:")

                for i, (ua, ca, q, ro) in enumerate(zip(st.session_state.user_answers, st.session_state.correct_answers, st.session_state.quiz_data_list, st.session_state.randomized_options)):
                    with st.expander(f"Question {i + 1}", expanded=False):
                        if ro[ua] != ca:
                            st.info(f"Question: {q[0]}")
                            st.error(f"Your answer: {ro[ua]}")
                            st.success(f"Correct answer: {ca}")