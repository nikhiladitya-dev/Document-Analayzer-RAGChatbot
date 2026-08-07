import streamlit as st

from services.api_client import APIClient

from components.layout import render as render_layout
from components.sidebar import render as render_sidebar
from components.header import render as render_header
from components.process_document import render as render_process
from components.processing_status import animate
from components.success_card import render as render_success
from components.error_card import render as render_error
from components.conversation import render as render_conversation

api = APIClient()


def render_home():

    if "document_ready" not in st.session_state:
        st.session_state.document_ready = False

    left, right = render_layout()

    with left:

        render_sidebar()

    with right:

        render_header()

        uploaded_file, process = render_process()

        if process:

            if uploaded_file is None:

                render_error(
                    "Please upload a PDF, DOCX, or TXT document."
                )

            else:

                try:

                    animate()

                    response = api.process_document(
                        uploaded_file
                    )

                    st.session_state.document_ready = True

                except Exception as e:

                    render_error(str(e))

        if st.session_state.document_ready:

            render_success()

            question = render_conversation()

            if question:

                st.session_state.messages.append(
                    {
                        "role": "user",
                        "content": question,
                        "sources": [],
                    }
                )

                response = api.chat(
                    question=question,
                )

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": response["answer"],
                        "sources": response["sources"],
                    }
                )

                st.rerun()