"""Streamlit UI for the Prompt-Builder Assistant."""

import os

import streamlit as st

from promtistry.agents.chat_agent import ChatAgent


def main() -> None:
    """Streamlit UI entry point for chatting with ChatAgent."""
    st.title("Chat with ChatBot")

    if "history" not in st.session_state:
        st.session_state.history = []

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        st.error("OPENAI_API_KEY environment variable is not set")
        return
    agent = ChatAgent(api_key)

    with st.form(key="chat_form", clear_on_submit=True):
        user_input = st.text_input("You:")
        submitted = st.form_submit_button("Send")
        if submitted and user_input:
            response = agent.run(user_input)
            st.session_state.history.append(("You", user_input))
            st.session_state.history.append(("Bot", response))

    for speaker, message in st.session_state.history:
        if speaker == "You":
            st.markdown(f"**You:** {message}")
        else:
            st.markdown(f"**Bot:** {message}")


if __name__ == "__main__":
    main()
