import streamlit as st


def render():

    st.markdown(
"""
<div class="success-card">

<h3>

✅ Video Ready

</h3>

<p>

Diva has successfully extracted the document.

You can now ask questions below.

</p>

</div>
""",
        unsafe_allow_html=True,
    )