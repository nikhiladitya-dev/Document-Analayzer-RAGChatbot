import streamlit as st


def render():

    st.markdown(
        """
<div class="card">

<h3 class="card-title">
📄 Upload Document
</h3>

<p class="card-subtitle">
Supports .pdf, .docx, or .txt document and begin chatting with it.
</p>

</div>
""",
        unsafe_allow_html=True,
    )

    uploaded_file = st.file_uploader(
        "",
        type=["pdf", "docx", "txt"],
        label_visibility="collapsed",
    )

    process = st.button(
        "🚀 Process Document",
        use_container_width=True,
    )

    return uploaded_file, process