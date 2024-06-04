import streamlit as st

def app():
    st.title("Projects")
    st.write("I'll be displaying the highlights of programming projects I've worked on through years. Info about these can also be found on my resume in the top right corner of this page!")

    projects = [
        {
            "title": "Mars Polar Tracer",
            "organization": "NASA L'SPACE Mission Concept Academy",
            "role": "Lead Systems Engineer for Team 5",
            "description":
            ["""
            Given NASA guidelines for a scientific mission to the Mar polar caps, our team needed to create a Preliminary 
            Design Review (PDR) for the mission. Our tasks were to:         
            """, """- Determine requirements and subrequirements""", 
            """- Identify relevant science goals from the Decadal Survey""", 
            """- Conduct trade studies for site selection and instrumentation""", 
            """- Design subsystems (ie. power, thermal, electrical) and lander and create CAD drawings for all""", 
            """- Determine budget, timeline, and risks for the mission""", 
            """- Present PDR to panel of professionals for review""",
            """""",
            """As Lead Systems Engineer, I was involved in all CAD designs, site and instrumentation selection, risk assessment, 
            and presenting our engineering plan to a panel of reviewers."""],
            "link": "https://docs.google.com/document/d/16aqarZYkW6Itx2fy4Qk3siD16TSN3DDUCoxARzQZOVM/edit?usp=sharing",
            "linkname": "Final PDR",
            "skills": ["Siemens NX", "Project Management", "Leadership", "Systems Engineering Design"],
            "image": "prjctimages/landerleg.png",
            "caption": "Siemens CAD design for Mars Polar Tracer lander leg"
        },
        {
            "title": "Ferravana, BlockChain Based Ferrari Trading Platform",
            "organization": None,
            "role": None,
            "description":
            ["""
            Design a website to buy and sell Ferraris based on Carvana using Streamlit. My main responsibilites in the project were:""", 
            """- Implement a search page with working filters""", 
            """- Create user login page and manage login access""", 
            """- Design UI for car listings""", 
            """- Update user info and listings based on sales""", 
            """""",
            """This was my first attempt at a web application so it is rough but it was an amazing experience and inspired me 
            to explore more types of programming. The most challenging but interesting part of my work on this was
            figuring out a way for Streamlit to reload after button presses. I accomplished this by implementing a state key that would 
            trigger refreshes when changed."""],
            "link": None,
            "linkname": None,
            "skills": ["Python", "Streamlit", "UI/UX Design", "Project Management"],
            "image": "prjctimages/ferravanasearch.png",
            "caption": "Search page (hover over top right to zoom)"
        },
    ]
    st.markdown("---")
    for project in projects:
        st.subheader(f"***{project['title']}***")
        left, right = st.columns((3,2))
        with left:
            if project['role'] and project['organization']:
                st.write(f"**Role:** {project['role']} at {project['organization']}")
            if project['description']:
                st.write(f"**Description:**" + '\n\n'.join(project['description']))
            if project['link'] and project['linkname']:
                st.write(f"**Link:** [{project['linkname']}]({project['link']})")
            if project['skills']:
                st.write(f"**Skills:** *{', '.join(project['skills'])}*")
        with right:
            if project['image']:
                st.image(project['image'], caption=project['caption'])
        st.markdown("---")
