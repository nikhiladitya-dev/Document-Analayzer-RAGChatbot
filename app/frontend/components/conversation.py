import streamlit as st
from components.message import (render_user,render_panda,)
from components.chat_input import render as render_chat_input

def render():

    st.markdown(
"""
<div class="conversation-title">

<h2>

💬 Conversation

</h2>

</div>
""",
        unsafe_allow_html=True,
    )

    if "messages" not in st.session_state:

        st.session_state.messages = []

    if not st.session_state.messages:

        render_panda(
"""
👋 Hello! I'm Diva ✨.
I answer questions strictly using the text of the processed document attached.
If the answer isn't present, I'll tell you honestly instead of guessing. 
Ask me your first question!
"""
        )

    else:

        for message in st.session_state.messages:

            if message["role"] == "user":

                render_user(message["content"])

            else:

                render_panda(
                    message["content"],
                    message["sources"],
                )

    return render_chat_input()