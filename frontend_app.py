import streamlit as st
from frontend.views.home import home

def main():
    # Set page config
    st.set_page_config(page_title="Smart Banking Intention Classifier", page_icon=":robot_face:")

    # Display the home view
    home()

if __name__ == "__main__":
    main()