import streamlit as st
from langchain_ollama.llms import OllamaLLM
from langchain_core.output_parsers import StrOutputParser

# Initialize the parser and the language model
parser = StrOutputParser()
llm = OllamaLLM(
    model="llama3.2",
    top_k=3
)

# Streamlit app
st.title('Interview Assistant using LLM')
st.write('This application uses a language model to conduct interviews.')

# Upload job description file
job_description = st.text_area("Paste job description here")
submit = st.button('Submit')

# Generate interview questions based on job description
questions_prompt = f"""
    Based on the following job description, generate interview questions:
    {job_description}
    1. Provide most relevant Questions and Answers in multiple choice options limiting to 5 options in below format A, B, C, D
    2. Provide at least min 20 Questions and Answers span around 20 minutes duration
    3. Generate Real Use Case wise Questions and logical Question and avoid salary based questions
    4. Provide min 6 Code Sample Based Questions are mandatory based on job description
    """
if submit:
    # Generate questions using the language model
    result = llm.invoke(questions_prompt)
    print(result,"********************************")
    questions_list = [generation for generation in result]
    print(questions_list,"********************************")

    # Initialize session state to keep track of the current question index
    if 'question_index' not in st.session_state:
        st.session_state.question_index = 0

    # Display the current question
    current_question = questions_list[st.session_state.question_index]
    st.write(f"Question {st.session_state.question_index + 1}: {current_question}")

    # Input for user's answer
    user_answer = st.text_input('Enter your answer (A, B, C, D):')

    # Button to move to the next question
    if st.button('Next Question'):
        st.session_state.question_index += 1
        if st.session_state.question_index < len(questions_list):
            current_question = questions_list[st.session_state.question_index]
            st.write(f"Question {st.session_state.question_index + 1}: {current_question}")
        else:
            st.write("You have completed all the questions.")