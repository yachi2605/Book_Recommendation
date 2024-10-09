import streamlit as st
from PIL import Image
# import cv2


def analysis_page():
       st.title("Glimpse of Recommendation 📈")
         

       # Load the PNG image
      #  image = Image.open(r"img\topRatedbg.png")
      #  # Display the image using Streamlit
      #  st.image(image, use_column_width=True)

      #  # Load the PNG image
      #  image = Image.open(r"img\mostbookauthor.png")
      #  # Display the image using Streamlit
      #  st.image(image, use_column_width=True)

       
       # Load the PNG image
       image = Image.open(r'img\Comparison.png')
       # Display the image using Streamlit
       st.image(image, use_column_width=True)

         # Load the PNG image
       image = Image.open(r"img\Techs.jpg")
       # Display the image using Streamlit
       st.image(image, use_column_width=True)


       






# def embed_power_bi_dashboard(embed_url):
#        html_code = f'''
#               <iframe width="1140" height="540" src="{embed_url}" frameborder="0" allowFullScreen="true"></iframe>
#        '''
#        st.markdown(html_code, unsafe_allow_html=True)

