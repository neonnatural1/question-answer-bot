import streamlit as st
from transformers import pipeline

answerbot = pipeline("question-answering")

st.title("🎈 QA Bot")
st.write(
    "This is a basic question answering bot. You have to give the context for it to guess the answer. For example:  \nQuestion: What color is apple?  \nContext: Apple is red.  \nAnswer: red"   
)
# Add a text input box
user_input1 = st.text_input("Enter some question:")
user_input2 = st.text_input("Enter the context:")

# Button to trigger action
if st.button("Submit"):
    answerraw = answerbot(question=f"{user_input1}", context=f"{user_input2}")
    answer = answerraw["answer"]
    st.write(f"Answer: {answer}")
    certainty = int(answerraw["score"]*100)
    st.write(f"Certainty:{certainty:}%")
