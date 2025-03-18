import streamlit as st
import requests
from streamlit_lottie import st_lottie

def app():
    # opening para

    # use lottie file
    # def loadlottie(url):
        # r = requests.get(url)
        # if r.status_code != 200: 
            # return None
        # return r.json()

    with st.container():
        text_col, img_col = st.columns((3,2))
        with text_col:
            st.title("About Me")
            st.write("""Hello, I'm Akanksha, a dedicated Software Engineer with a strong foundation in astrophysics and automation. I specialize in developing efficient, scalable software solutions and 
            have a proven track record in analytical research and technical project management. My diverse background allows me to approach complex problems from unique perspectives, driving innovation in 
            both software development and system optimization.""")
            st.write("""I am always eager to collaborate on challenging projects and contribute my skills to solve real-world problems. Feel free to connect with me through the Contact page or 
                    [LinkedIn](https://www.linkedin.com/in/akanksha-ramabadran/) if you're interested in working together or discussing opportunities.""")
        # with img_col:
            # add headshot
            # lot = loadlottie("https://lottie.host/6aa16f90-6007-467f-b8c1-438d7f4d26dd/WDII2HGGD4.json")
            # st_lottie(lot, height=300)

    with st.container():
        st.write("---")
        st.subheader("What I Do")
        st.write("")
        st.write(
            """
            I specialize in software development with expertise in Python, C++, and UiPath, focusing on delivering efficient solutions in the following areas:
            - **Automation**: In my current role at Wells Fargo, I work on optimizing and enhancing UiPath automation workflows to address evolving business needs, improving efficiency and scalability.
            - **Data Analysis**:  I have hands-on experience in analyzing complex scientific datasets, utilizing Python and specialized libraries for data manipulation and visualization. My work includes developing 
            models to analyze astronomical data, supporting research through data-driven insights, and applying statistical methods to interpret scientific phenomena.
            - **Project Management**: I lead multidisciplinary teams in executing complex projects, from conceptualizing Mars mission designs to driving impactful research in astronomy and other scientific fields.
            
            To explore my work further, please visit the Research and Projects pages.""")
        
