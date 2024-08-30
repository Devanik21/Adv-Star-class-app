import streamlit as st

# Set page configuration
st.set_page_config(page_title="Star Classification App", page_icon="🌟🔭", layout="wide")

st.title("Welcome to the Star Classification App")
st.markdown("""
    This app allows you to classify celestial objects into three categories:
    - **Galaxy**
    - **QSO**
    - **Star**

    Use the navigation bar on the left to explore different pages:
    - **Home**: Introduction to the app.
    - **Star Classification**: Input features to classify celestial objects.
    - **About**: Learn more about the app and its development.
    - **Contact**: Get in touch with us.
    - **Help**: Get help or view FAQs.
    - **Gallery**: View celestial images.
    - **Feedback**: Provide feedback on the app.
""")
