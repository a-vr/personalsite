import streamlit as st

def app():
    st.title("Research Showcase")
    st.write("""Throughout my career, I have contributed to a range of impactful research projects across various scientific and technical domains. These projects highlight my ability to tackle complex problems, 
    develop innovative solutions, and derive meaningful conclusions.""")

    research_projects = [
        {
            "title": "Using Optical Hyperspectral Data to Identify Sediment Size and Concentration in Water",
            "organization": "WHIRLab at Rutgers",
            "role": "Research Assistant",
            "description": """Analyzed over 100 hyperspectral images of water samples mixed with sediment to discern changes in the 
            visible spectrum induced by sedimentation, employing Python for comprehensive comparison between polluted and clean samples 
            and presented findings at the annual Rutgers Undergraduate Research Symposium.""",
            "link": "https://drive.google.com/file/d/1OW7BDW172qtV0Io6irdiOCU9Lr3wmOev/view?usp=sharing",
            "linkname": "Research Poster",
            "skills": ["Python", "Matplotlib", "Independent Research", "Spectral Analysis", "Science Communication"],
            "image": "rsrchimages/arestypresentation.png",
            "caption": "Photo of me presenting my findings at the Annual Rutgers Undergraduate Research Symposium in 2023."
        },
        {
            "title": "Structure Formation Simulation with GADGET-IV",
            "organization": None,
            "role": None,
            "description": """Executed structure formation simulation of 50 Mpc box of dark matter particles with group to model the formation 
            of the cosmic web (using the Max Planck Institute’s GADGET-IV simulation) on Rutgers’ Amarel supercomputer cluster to compare 
            to other simulations and theories on formation of the cosmic web.""",
            "link": "https://docs.google.com/presentation/d/14tk_rmN7h6Fr55B55anaqjZFyzEWtR_afKt0iVIm3-g/edit?usp=sharing",
            "linkname": "Google Slides Presentation",
            "skills": ["Python", "Numpy", "Matplotlib", "Scipy", "Simulation and Modeling", "Supercomputing", "Jupyter Notebooks"],
            "image": "rsrchimages/densityofbox.png",
            "caption": "Density map of 50 Mpc box facing the x-axis at end of simulation, showing web structure, rendered with Matplotlib."
        },
        # Add more projects as needed
        {
            "title": "Analysis of FIRST sources in COSMOS Field",
            "organization": None,
            "role": None,
            "description": """The FIRST (Faint Images of the Radio Sky at Twenty-Centimeters) Survey takes radio images of the sky that can 
            be used to detect distant galaxies. Using masking, our group removed noise from the specified field and identified 68 unique radiometric 
            sources. Then by calculating the 1.4 GHz Flux Density and comparing those values and sources to known objects in the COSMOS (Cosmic Evolution Survey), 
            we were able to identify our sources as distant galaxies and stars. Our most interesting finding was that though some sources looked like quasars 
            in our initial mask layers, they were instead either binary systems or galaxies.""",
            "link": "https://docs.google.com/presentation/d/1cdA3LgU1jiTyIYHY6VMy1aqzXMcBJT09/edit?usp=sharing&ouid=101338707413142955563&rtpof=true&sd=true",
            "linkname": "Group Google Slides Presentation",
            "skills": ["Python", "Numpy", "Pandas", "Matplotlib", "Astropy", "Observational Research", "Google Colab"],
            "image": "rsrchimages/exsource.png",
            "caption": "Example of source that we expected to be a quasar, located at 151.02903717 deg, 2.71621923 deg, rendered with Matplotlib"
        },
    ]

    st.markdown("---")
    for project in research_projects:
        st.subheader(f"***{project['title']}***")
        left, right = st.columns((3,2))
        with left:
            if project['role'] and project['organization']:
                st.write(f"**Role:** {project['role']} at {project['organization']}")
            if project['description']:
                st.write(f"**Description:** {project['description']}")
            if project['link'] and project['linkname']:
                st.write(f"**Link:** [{project['linkname']}]({project['link']})")
            if project['skills']:
                st.write(f"**Skills:** *{', '.join(project['skills'])}*")
        with right:
            if project['image']:
                st.image(project['image'], width=350, caption=project['caption'])
        st.markdown("---")
