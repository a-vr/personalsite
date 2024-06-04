import streamlit as st
import requests
from streamlit_lottie import st_lottie

def app():
    # opening para

    # use lottie file
    def loadlottie(url):
        r = requests.get(url)
        if r.status_code != 200: 
            return None
        return r.json()

    with st.container():
        text_col, img_col = st.columns((3,2))
        with text_col:
            st.title("Hi! I'm Akanksha")
            st.write("""I'm a passionate software developer with a background in astrophysics and a knack for complex problem-solving. 
                     With hands-on experience in mission design, analytical research, and technical project management, I'm eager to apply 
                     my skills to new and creative software development projects.""")
            st.write("""Please feel free to reach out to me via the Contact page or [LinkedIn](https://www.linkedin.com/in/akanksha-ramabadran/) 
                     if you would like get in touch!""")
        with img_col:
            # add headshot
            lot = loadlottie("https://lottie.host/6aa16f90-6007-467f-b8c1-438d7f4d26dd/WDII2HGGD4.json")
            st_lottie(lot, height=300)

    with st.container():
        st.write("---")
        st.subheader("What I Do")
        st.write("")
        st.write(
            """
            I specialize in software development with a focus on Python, C++, and web technologies, including:
            - **Data Analysis and Automation**: Leveraging Python and its libraries (Pandas, NumPy) to automate data analysis.
            - **Web Development**: Designing and developing web platforms, such as a blockchain-based Ferrari trading platform and this website, both powered by Streamlit!
            - **Project Management**: Leading multidisciplinary teams to execute complex projects, from designing Mars mission concepts to spearheading research in astronomy and beyond.
            - **Technical Writing and Communication**: Communicating complex technical concepts clearly and effectively to anyone, regardless of their background.
            
            You can check out my Research and Projects pages to learn more!""")
        
