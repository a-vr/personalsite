import streamlit as st
from streamlit_option_menu import option_menu
import about 
import research
import projects
import contact
import bookstomusic


st.set_page_config(page_title="Akanksha's Webpage", page_icon="telescope", layout="wide")

# Define the HTML for the header with GitHub and LinkedIn links
header_html = """
    <div style="display: flex; justify-content: flex-end; align-items: center;">
        <div>
            <a href="https://drive.google.com/file/d/1t1AtNxI5BAtHSnB-A9ZdmjDDi6teEz44/view?usp=drive_linkhttps://drive.google.com/file/d/1t1AtNxI5BAtHSnB-A9ZdmjDDi6teEz44/view?usp=drive_link" target="_blank" style="margin-right: 15px;">
                <img src="https://img.icons8.com/ios-glyphs/30/4b4e54/pdf.png" width="30" height="30" alt="Resume">
            </a>
            <a href="https://github.com/a-vr" target="_blank" style="margin-right: 15px;">
                <img src="https://img.icons8.com/ios-filled/50/4b4e54/github.png" width="30" height="30">
            </a>
            <a href="https://www.linkedin.com/in/akanksha-ramabadran/" target="_blank">
                <img src="https://img.icons8.com/ios-filled/50/4b4e54/linkedin.png" width="30" height="30">
            </a>
        </div>
    </div>
"""

# Render the header HTML using st.markdown
st.markdown(header_html, unsafe_allow_html=True)

# hides streamlit logos
hide_default_format = """
       <style>
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)


# pages
PAGES = {"About": about, 
         "Research": research, 
         "Projects": projects,
         "Contact": contact,
         "Books to Music": bookstomusic}

# navigation menu settings
with st.sidebar:
        choose = option_menu("Navigation", list(PAGES.keys()),
                         icons=['info-circle', 'bar-chart', 'folder', 'send', 'music-note'],
                         menu_icon="dash", default_index=0,
                         styles={
        "container": {"padding": "5!important"},
        "icon": {"font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#fff"},
    }
    )

# allows navigation
page = PAGES[choose]
page.app()
    
