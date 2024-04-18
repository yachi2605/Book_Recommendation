import streamlit as st
from  pages import mainLogic
def homepage():
    st.title("Welcome to Book Recommender")
    mainLogic.algorithm_page()

 
            