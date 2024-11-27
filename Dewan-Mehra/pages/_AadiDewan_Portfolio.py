import streamlit as st
import AadiDewanInfo
import pandas as pd

st.title("Aadi's Portfolio")
st.write("""
This page showcases Aadi Raj Dewan's achievements throughout high school and co$
highlighting his academic journey and extracurricular milestones.
""")

# About Me
def about_me_section():
    st.header("🚀 About Me")
    st.image(AadiDewanInfo.profile_picture, width=500)
    st.write(AadiDewanInfo.about_me)
    st.write("---")

about_me_section()

# Links
def links_section():
    st.sidebar.header("My Links")
    st.sidebar.text("Connect with me on LinkedIn")
    linkedin_link = f'<a href="{AadiDewanInfo.my_linkedin_url}"><img src="{AadiDewanInfo.linkedin_image_url}" alt="LinkedIn" width="75" height="75"></a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)
    st.sidebar.text("Checkout my work")
    github_link = f'<a href="{AadiDewanInfo.my_github_url}"><img src="{AadiDewanInfo.github_image_url}" alt="GitHub" width="65" height="65"></a>'
    st.sidebar.markdown(github_link, unsafe_allow_html=True)
    st.sidebar.text("Contact Me")
    email_html = f'<a href="mailto:{AadiDewanInfo.my_email_address}"><img src="{AadiDewanInfo.email_image_url}" alt="Email" width="75" height="75"></a>'
    st.sidebar.markdown(email_html, unsafe_allow_html=True)

links_section()

# Education
def education_section(education_data, course_data):
    st.header("📚 Education")
    st.subheader(f"***{education_data['Institution']}***")
    st.write(f"**Degree:** {education_data['Degree']}")
    st.write(f"**Graduation Date:** {education_data['Graduation Date']}")
    st.write(f"**GPA:** {education_data['GPA']}")
    st.write("**Relevant Coursework:**")
    coursework = pd.DataFrame(course_data)
    st.dataframe(coursework, hide_index=True)
    st.write("---")

education_section(AadiDewanInfo.education_data, AadiDewanInfo.course_data)

# Professional Experience
def experience_section(experience_data):
    st.header("💼 Relevant Experience")
    for job_title, (job_description, image1, image2) in experience_data.items():
        expander = st.expander(f"{job_title}")
        if image1:
            expander.image(image1, width=350)
        if image2:
            expander.image(image2, width=350)
        for bullet in job_description:
            expander.write(bullet)
    st.write("---")

experience_section(AadiDewanInfo.experience_data)

# Projects
def project_section(projects_data):
    st.header("🛠 Projects")
    for project_name, project_description in projects_data.items():
        expander = st.expander(f"{project_name}")
        expander.write(project_description)
    st.write("---")

project_section(AadiDewanInfo.projects_data)

# Skills
def skills_section(programming_data, spoken_data):
    st.header("👨‍💻 Skills")

    st.subheader("Programming Languages")
    for skill, percentage in programming_data.items():
        st.markdown(f"{skill} {AadiDewanInfo.programming_icons.get(skill, '')}", unsafe_allow_html=True)
        st.progress(percentage)

    st.subheader("Spoken Languages")
    for spoken, proficiency in spoken_data.items():
        st.markdown(f"{spoken}: {proficiency}", unsafe_allow_html=True)

    st.write("---")

skills_section(AadiDewanInfo.programming_data, AadiDewanInfo.spoken_data)

# Activities
def activities_section(leadership_data, activity_data):
    st.header("🧗 Activities")
    tab1, tab2 = st.tabs(["Leadership", "Community Service"])

    with tab1:
        st.subheader("🥇 Leadership")
        for title, details in leadership_data.items():
            expander = st.expander(f"{title}")
            for bullet in details:
                expander.write(bullet)

    with tab2:
        st.subheader("🛠️ Community Service")
        for title, details in activity_data.items():
            expander = st.expander(f"{title}")
            for bullet in details:
                expander.write(bullet)

    st.write("---")

activities_section(AadiDewanInfo.leadership_data, AadiDewanInfo.activity_data)

