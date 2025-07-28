"""Streamlit UI for the Prompt-Builder Assistant (LangGraph Edition).

This UI uses the pre-compiled `runner` that you created in
`promtistry/flow/chat_flow.py`. The runner contains the
Bot-Agent and handles the `exit` routing - the interface only
handles the display.
"""

import os
from dataclasses import asdict

import streamlit as st

from promtistry.flow.langgraph import runner  # your LangGraph-Runner
from promtistry.flow.state import ChatState  # Dataclass-State


def main() -> None:  # (imperative is fine here)
    """Streamlit entry point that integrates the LangGraph runner."""
    st.set_page_config(page_title="Prompt-Builder Chat", page_icon="💬")
    st.title("💬 Chat with ChatBot")

    # --- API Key Check (informative) -------------------------------------
    if not os.getenv("OPENAI_API_KEY"):
        st.error("OPENAI_API_KEY environment variable is not set")
        return

    # --- Initialize Session State ----------------------------------------
    if "chat_state" not in st.session_state:
        st.session_state.chat_state = ChatState()  # empty
        st.session_state.history = []  # [(role, content), …]

    # --- Render History ---------------------------------------------------
    for role, msg in st.session_state.history:
        with st.chat_message(role):
            st.write(msg)

    # --- Input & Flow Invocation -----------------------------------------
    if prompt := st.chat_input("Write a message (type 'exit' to quit)"):
        # 1) Save & display user message
        st.session_state.history.append(("user", prompt))
        with st.chat_message("user"):
            st.write(prompt)

        # 2) Invoke runner
        state_dict = runner.invoke(
            asdict(st.session_state.chat_state.update(user_msg=prompt)),
        )
        new_state = ChatState(**state_dict)
        st.session_state.chat_state = new_state

        # 3) Display bot response
        bot_reply = new_state.bot_msg
        st.session_state.history.append(("assistant", bot_reply))
        with st.chat_message("assistant"):
            st.write(bot_reply)

        # 4) Optional: immediately stop if "exit"
        if prompt.strip().lower() == "exit":
            st.stop()

    # Judge button: rate the last bot response independently
    if st.session_state.chat_state.bot_msg and st.button("Bewerte", key="judge"):
        state_dict = runner.invoke(asdict(st.session_state.chat_state))
        new_state = ChatState(**state_dict)
        st.session_state.chat_state = new_state
        judge_reply = new_state.judge_msg
        st.session_state.history.append(("judge", judge_reply))
        with st.chat_message("assistant"):
            st.markdown(
                f"<div style='background-color:#EFEFEF;color:#FF5733;padding:10px;"
                f"border-radius:5px'>{judge_reply}</div>",
                unsafe_allow_html=True,
            )


if __name__ == "__main__":
    main()
