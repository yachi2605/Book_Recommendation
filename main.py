
import streamlit as st
st.set_page_config(
    page_title="Book Recommender",
    page_icon="📔",
    layout="wide",
    initial_sidebar_state="auto"
)

from component.analysis import analysis_page
from component.mainLogic import algorithm_page
from component.about import app as about_app

from streamlit_option_menu import option_menu

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    @staticmethod
    def main():
        with st.sidebar:
            app = option_menu(
                menu_title='Books',
                options=['Home', 'Analysis', 'About'],
                icons=['house-fill', 'chat-fill', 'info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

        if app == 'Home':
            algorithm_page()

        elif app == 'About':
            about_app()

        elif app == 'Analysis':
           analysis_page()


if __name__ == "__main__":
    MultiApp.main()
