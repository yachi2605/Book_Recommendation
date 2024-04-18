# conda activate bookvenv
# python main.py
# streamlit run main.py

import streamlit as st
from pages import analysis,  mainLogic,about,home

from streamlit_option_menu import option_menu
import streamlit as st

from streamlit_option_menu import option_menu

# Set Streamlit page configurations
st.set_page_config(
    page_title="Book Recommender",
    page_icon="📔",
    layout="centered",
    initial_sidebar_state="auto"
)

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
                options=['Home','Analysis','About'],
                icons=['house-fill','chat-fill','info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
                    "icon": {"color": "white", "font-size": "23px"}, 
                    "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

        if app == 'Home':
            mainLogic.algorithm_page()
        
        if app == 'About':
            about.app()
        if app=='Analysis':
             analysis.analysis_page()

        


 
if __name__ == "__main__":
         MultiApp.main()   









        #  with st.sidebar:
        #         app = st.selectbox(
        #             'Navigation',
        #             ['Account','Home', 'Profile', 'About']
        #         )





       # # if app == "Home":
        # #    if st.session_state.user_id:
        # #         home.homepage()
        # #    else:
        # #         st.warning("You need to login to access the home page.")
        # # elif app== "Account":
        # #     if st.session_state.user_id:
        # #         profile.profile_page()
        # #     else:
        # #         login.login_form()
        # # elif app == "Profile":
        # #     if st.session_state.user_id:
        # #         profile.profile_page()
        # #     else:
        # #         st.warning("You need to login to access the profile.")
        # elif app == "About":
        #     about.app()