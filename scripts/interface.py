"""
@author: assanchez

para ejecutar este script
python -m streamlit run scripts/interface.py
"""
from main import Pipeline
import streamlit as st

def send_click():
    question = st.session_state.user_input
    if question:
        response, answer = st.session_state.pipe.invoke(question)
        st.session_state.history.insert(0, (question, response, answer))
        st.session_state.user_input = ""  # Clear input field

def init_pipeline():
    with st.spinner("Cargando modelo y base de datos..."):
        return Pipeline()


def main():
    # Initialize session state
    if "pipe" not in st.session_state:
        st.session_state.pipe = init_pipeline()
    if "history" not in st.session_state:
        st.session_state.history = []

    st.title("📊 Data Analysis Agent")

    # User input
    st.text_input("Ask Something about F1:", key="user_input", on_change=send_click)

    # Display chat history
    for question, sql, answer in st.session_state.history:
        st.write(f"**You:** {question}")
        st.write(f"**SQL:** {sql}")
        st.write(f"**Answer:** {answer}")
        # st.dataframe(answer, use_container_width=True)
        st.markdown("---")

if __name__ == "__main__":
    main()