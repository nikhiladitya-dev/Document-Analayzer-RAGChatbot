import streamlit as st


def render():

    question = st.chat_input(
        "Ask ✨Diva anything about this video..."
    )

    return question