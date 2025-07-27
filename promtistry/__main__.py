"""promtistry entrypoint."""

import os
import sys

from streamlit.web.cli import main as st_main

# Ensure OpenAI key is available before launching the app
if not os.getenv("OPENAI_API_KEY"):
    error_message = "OPENAI_API_KEY environment variable is not set"
    raise RuntimeError(error_message)

if __name__ == "__main__":
    sys.argv = ["streamlit", "run", "promtistry/ui/streamlit_ui.py"]
    sys.exit(st_main())
