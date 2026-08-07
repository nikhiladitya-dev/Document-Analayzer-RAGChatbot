import streamlit as st


def render_user(
    message: str,
):

    st.markdown(
        f"""
<div class="message-row user-row">
<div class="message-card user-card">

<div class="message-header">
👤 You
</div>

<div class="message-body">
{message}
</div>

</div>
</div>
""",
        unsafe_allow_html=True,
    )


def render_panda(
    message: str,
    sources: list | None = None,
):

    if sources is None:
        sources = []

    html = f"""
<div class="message-row assistant-row">

<div class="assistant-avatar">
✨
</div>

<div class="message-card assistant-card">

<div class="message-header">
Diva
</div>

<div class="message-body">
{message}
</div>
"""

    if sources:

        html += """

<div class="sources-title">
📄 Sources
</div>

<div class="sources-container">

"""

        grouped_sources = {}

        for source in sources:

            source_name = source.get(
                "source",
                "Unknown Document",
            )

            page = source.get("page")

            if source_name not in grouped_sources:
                grouped_sources[source_name] = set()

            if page is not None:
                grouped_sources[source_name].add(page)

        for source_name, pages in grouped_sources.items():

            if pages:

                pages = sorted(pages)

                if len(pages) == 1:

                    html += f"""
<div class="source-chip">
📄 {source_name} &nbsp;|&nbsp; 📑 Page {pages[0]}
</div>
"""

                else:

                    page_list = ", ".join(str(p) for p in pages)

                    html += f"""
<div class="source-chip">
📄 {source_name} &nbsp;|&nbsp; 📑 Pages {page_list}
</div>
"""

            else:

                html += f"""
<div class="source-chip">
📄 {source_name}
</div>
"""

        html += """

</div>

"""

    html += """

</div>

</div>

"""

    st.markdown(
        html,
        unsafe_allow_html=True,
    )