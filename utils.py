import streamlit as st
from streamlit.components.v1 import html


def make_intro():
    st.markdown(
        """
        <h1 style='text-align: center; padding-top:0 '>Welcome</h1>
        """,
        unsafe_allow_html=True,
    )
    html(
        """
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Centered Animation</title>
                <style>
                    .centered-container {
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh; /* This makes the container take the full height of the viewport */
                    }
                </style>
            </head>
            <body>
                <div class="centered-container">
                    <dotlottie-player src="https://lottie.host/4c620c8a-7490-4497-8a18-44b2f8637931/IMPt6mKSWx.json" background="transparent" speed="1" style="width: 500px;" loop autoplay></dotlottie-player>
                </div>
    
                <script src="https://unpkg.com/@dotlottie/player-component@latest/dist/dotlottie-player.mjs" type="module"></script>
            </body>
            </html>
            """,
        height=200,
    )
    
def reset_conversation():
  st.session_state.messages = []