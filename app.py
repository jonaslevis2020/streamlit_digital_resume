from cgitb import small
from pathlib import Path
import streamlit as st
from PIL import Image




# --- PATH SETTING ---
current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
css_file = current_dir / 'styles' / 'main.css'
resume_file = current_dir / 'assets' / 'CV.pdf'
profile_picture = current_dir / 'assets' / 'profile-pic.png'

print(f'css_file: {css_file }')
print(f'resume_file: {resume_file }')
print(f'profile_pictre: {profile_picture }')

# GENERAl SETTINGS
PAGE_TITLE = 'Digital CV | John Doe'
PAGE_ICONE = ':wave:'
NAME = 'John Doe'
DESCRIPTION = """
    Senior Data Analyst, assisting enterprises by supporting data-driven decission-making
"""
EMAIL = 'johndoe@email.com'
SOCIAL_MEDIA = {
    'Youtube': 'https://youtube.com/c/codingisfun',
    'Linkedin': 'https://linkedin.com',
    'Github': 'https://github.com',
    'Tweeter': 'https://tweeter.com'
}
PROJECTS = {
    '🏆 Sales Dashboard - Comparing the sales accross the three stores': 'https://youtube.com/',
    '🏆 Income and Expanse Tracker - Web App with NoSQL Database':'https://youtu.be/qwd3233',
    '🏆 Desktop Application - excel2csv Converter with user settings and menubar':'https://yout.com/HjoiuY',
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICONE)
st.title('Hello there :)')

# ---- hide default footer and hamburger menu
hide_streamlit_style = """
            <style>
            # MainMenu {visibility: show;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ---- LOAD CSS, PDF & PROFILE PICTURE ----
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with open(resume_file, 'rb') as pdf_file:
    pdf_byte = pdf_file.read()

profile_pic = Image.open(profile_picture)


# ---- HERO SECTION ---
col1, col2 = st.columns(2, gap='small')

with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label='📝 Download Resume',
        data=pdf_byte,
        # file_name=resume_file.name,
        file_name=f'{"".join(NAME.split())}_resume.pdf',
        mime='application/octet-stream'
    )
    st.write('📧', EMAIL)

# ---- SOCIAL LINKS ----
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))

for i, (plateform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[i].write(f'[{plateform}]({link})')


# ---- EXPERIENCE AND QUALIFICATION ----
st.write("#")
st.subheader('Experience & Qualifications')
st.write(
    """
    - ✔️ 7 Years experience extracting actionnable insights from data
    - ✔️ Strong hands on experience and knowledge in Python including Excel
    - ✔️ Good understand of statistical principles and their respectives applications
    - ✔️ Excellent team-player and displaying strong sense of initiative on tasks
    """
)

# ---- HARD SKILLS ----
st.write("#")
st.subheader('Hard Skills')
st.write(
    """
    - ✔️ Programming: Python(sklearn, pandas), SQL, VBA
    - ✔️ Data Visualization: PowerBI, MS Excel, Plotly
    - ✔️ Modeling: Logistic regression, linear regression, decision trees
    - ✔️ Databases: Postgres, MongoDB, MySql
    """
)

# ---- WORK HISTORY ----
st.write('#')
st.subheader('Work History')

# ---- JOB 1
st.write('---')
st.write('**Senor Data Analyst | Ross Industries**')
st.write('02/2020 - present')
st.write("""
    - ➡️ Used PowerBI and SQL to redefine and track KPI's surrounding marketing initiatives and supply recommandations to boost landing page convertion rate by 38%.
    - ➡️ Led a team of 4 analysts to brainstorm potential marketing and sales imporvements and implemented A/B tests to generate 15% more client leads.
    - ➡️ Redesigned data model through iterations that imporoved prediction by 12%
""")

# ---- JOB 2
st.write('---')
st.write('**Senor Data Analyst | Ross Industries**')
st.write('02/2020 - present')
st.write("""
    - ➡️ Used PowerBI and SQL to redefine and track KPI's surrounding marketing initiatives and supply recommandations to boost landing page convertion rate by 38%.
    - ➡️ Led a team of 4 analysts to brainstorm potential marketing and sales imporvements and implemented A/B tests to generate 15% more client leads.
    - ➡️ Redesigned data model through iterations that imporoved prediction by 12%
""")

# ---- JOB 3
st.write('---')
st.write('**Senor Data Analyst | Chegg**')
st.write('04/2015 - 01/2018')
st.write("""
    - ➡️ Used PowerBI and SQL to redefine and track KPI's surrounding marketing initiatives and supply recommandations to boost landing page convertion rate by 38%.
    - ➡️ Led a team of 4 analysts to brainstorm potential marketing and sales imporvements and implemented A/B tests to generate 15% more client leads.
    - ➡️ Redesigned data model through iterations that imporoved prediction by 12%
""")


# ---- PROJECTS & ACCOMPLISHMENTS ----
st.write('#')
st.subheader('Projects & Accomplishments')
st.write('---')
for project, link in PROJECTS.items():
    st.write(f'[{project}]({link})')