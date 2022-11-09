# build a treamlit app to build a resume using python, and tags from job descriptions

import streamlit as st
import pandas as pd
import numpy as np
import random

# avoid duplicate keys in streamlit

st.set_option('deprecation.showfileUploaderEncoding', False)




# Title
st.title('Resume Builder')

# Sidebar
st.sidebar.header('User Input Features')  
job_desc = st.sidebar.text_area('Job Description', 'Type Here')

# Main
st.header('Information')
full_name = st.text_input('Full Name', "Ayoub ABRAICH")
email = st.text_input('Email', "abraich.admission+jobs@gmail.com   ")
phone = st.text_input('Phone', "06 00 00 00 00")
address = st.text_input('Address', "Paris, France")
position = st.text_input('Position', "Data Scientist")
summary = st.text_area('Summary', "I am a data scientist with 3 years of experience in the field. I have a master's degree in data science from the University of Paris. I am looking for a job in the field of data science.")

# Education
st.header('Education')
numb_education = st.number_input('Number of Education', 1, 10, 1)
d_edu = {}
d_edu['School'] = []
d_edu['Degree'] = []
d_edu['Start Date'] = []
d_edu['End Date'] = []
d_edu['Description'] = []

for i in range(numb_education):
    st.subheader(f'## Education {i+1} ##')
    school = st.text_input('School', "Ecole Polytechnique",key=f'edu_school_{i}')
    degree = st.text_input('Degree', "Master of Science",key=f'edu_degree_{i}')
    start_date = st.text_input('Start Date', "2019",key=f'edu_start_date_{i}')
    end_date = st.text_input('End Date', "2021" ,key=f'edu_end_date_{i}')
    description = st.text_area('Description', "Description",key=f'edu_description_{i}')
    d_edu['School'].append(school)
    d_edu['Degree'].append(degree)
    d_edu['Start Date'].append(start_date)
    d_edu['End Date'].append(end_date)
    d_edu['Description'].append(description)

    
# Experience
st.header('Experience')
numb_experience = st.number_input('Number of Experience', 1, 10, 1)
d_exp = {}
d_exp['Company'] = []
d_exp['Position'] = []
d_exp['Start Date'] = []
d_exp['End Date'] = []
d_exp['Description'] = []

for i in range(numb_experience):
    st.subheader(f'## Experience {i+1} ##')
    company = st.text_input('Company', "Company", key = f'exp_company_{i}')
    position = st.text_input('Position', "Position", key= f'exp_position_{i}')
    start_date_c = st.text_input('Start Date', "2019", key= f'exp_start_date_{i}')
    end_date_c = st.text_input('End Date', "2021", key= f'exp_end_date_{i}')
    description_c = st.text_area('Description', "Description", key= f'exp_description_{i}')
    d_exp['Company'].append(company)
    d_exp['Position'].append(position)
    d_exp['Start Date'].append(start_date_c)
    d_exp['End Date'].append(end_date_c)
    d_exp['Description'].append(description_c)
    
    
# Skills
st.header('Skills')
numb_skills = st.number_input('Number of Skills', 1, 10, 1)
d_skills = {}
d_skills['Skill'] = []
d_skills['Level'] = []

for i in range(numb_skills):
    st.subheader(f'## Skill {i+1} ##')
    skill = st.text_input('Skill', "Skill", key= f'skill_skill_{i}')
    level = st.text_input('Level', "Level", key= f'skill_level_{i}')
    d_skills['Skill'].append(skill)
    d_skills['Level'].append(level)
    
# Interests
st.header('Interests')
numb_interests = st.number_input('Number of Interests', 1, 10, 1)
d_interests = {}
d_interests['Interest'] = []

for i in range(numb_interests):
    st.subheader(f'## Interest {i+1} ##')
    interest = st.text_input('Interest', "Interest", key= f'interest_{i}')
    d_interests['Interest'].append(interest)

# References
st.header('References')
numb_references = st.number_input('Number of References', 1, 10, 1)
d_references = {}
d_references['Name'] = []
d_references['Position'] = []
d_references['Company'] = []
d_references['Email'] = []

for i in range(numb_references):
    st.subheader(f'## Reference {i+1} ##')
    name_ref = st.text_input('Name', "Name", key= f'ref_name_{i}')
    position_ref = st.text_input('Position', "Position", key= f'ref_position_{i}')
    company_ref = st.text_input('Company', "Company", key= f'ref_company_{i}')
    email_ref = st.text_input('Email', "Email", key= f'ref_email_{i}')   
    d_references['Name'].append(name_ref)
    d_references['Position'].append(position_ref)
    d_references['Company'].append(company_ref)
    d_references['Email'].append(email_ref)
    


# Build the resume
# dont show the borders of the tables, make table responsive
# Education
df_edu = pd.DataFrame(d_edu)
df_edu = df_edu[['School', 'Degree', 'Start Date', 'End Date', 'Description']]
df_edu= df_edu.set_index('School')
df_edu = df_edu.sort_values(by=['Start Date'], ascending=False)
df_edu = df_edu.style.set_table_styles([dict(selector='th', props=[('border', '0px')])])

df_edu = df_edu.set_table_attributes('class="table table-responsive"')

# Experience
df_exp = pd.DataFrame(d_exp)
df_exp = df_exp[['Company', 'Position', 'Start Date', 'End Date', 'Description']]
df_exp = df_exp.set_index('Company')
df_exp = df_exp.sort_values(by=['Start Date'], ascending=False)
df_exp = df_exp.style.set_table_styles([dict(selector='th', props=[('border', '0px')])])
df_exp = df_exp.set_table_attributes('class="table table-responsive"')


# Skills
df_skills = pd.DataFrame(d_skills)
df_skills = df_skills[['Skill', 'Level']]
df_skills = df_skills.set_index('Skill')
df_skills = df_skills.sort_values(by=['Level'], ascending=False)
df_skills = df_skills.style.set_table_styles([dict(selector='th', props=[('border', '0px')])])
df_skills = df_skills.set_properties(**{'border': '0px', 'border-collapse': 'collapse'})
df_skills = df_skills.set_table_attributes('border="0"')   

# Interests
df_interests = pd.DataFrame(d_interests)
#df_interests = df_interests[['Interest']]
df_interests = df_interests.style.set_table_styles([dict(selector='th', props=[('border', '0px')])])

df_interests = df_interests.set_properties(**{'border': '0px', 'border-collapse': 'collapse'})
df_interests = df_interests.set_table_attributes('border="0"')
df_interests = df_interests.set_table_attributes('class="table table-responsive"')
# References
df_references = pd.DataFrame(d_references)
df_references = df_references[['Name', 'Position', 'Company', 'Email']]
df_references = df_references.set_index('Name')
df_references = df_references.style.set_table_styles([dict(selector='th', props=[('border', '0px')])])

df_references = df_references.set_table_attributes('class="table table-responsive"')

# Build the resume / inside box

st.header('Resume')
# html : name and title, social media, summary
name = full_name
title = position
linkedin = 'https://www.linkedin.com/in/your-linkedin/'
github = 'https'
twitter = 'https'

html = f"""
<div class="row">
    <div class="col-md-6">
        <h1>{name}</h1>
        <h3>{title}</h3>
    </div>
    <div class="col-md-6">
        <ul style="list-style-type: none; text-align: right;">
            <li><a href="{linkedin}">LinkedIn</a></li>
            <li><a href="{github}">GitHub</a></li>
            <li><a href="{email}">Email</a></li>
        </ul>
    </div>
</div>
<div class="row">
    <div class="col-md-12">
        <h3>Summary</h3>
        <p>
            {summary}
        </p>
    </div>
</div>
"""
st.markdown(html, unsafe_allow_html=True)
              
st.markdown('<h3>Education</h3>', unsafe_allow_html=True)
#df_edu to html, responsive
df_edu_html = df_edu.render()
st.markdown(df_edu_html, unsafe_allow_html=True)    


st.markdown('<h3>Experience</h3>', unsafe_allow_html=True)
#df_exp to html
df_exp_html = df_exp.render()
st.markdown(df_exp_html, unsafe_allow_html=True)

st.markdown('<h3>Skills</h3>', unsafe_allow_html=True)
#df_skills to html
df_skills_html = df_skills.render()
st.markdown(df_skills_html, unsafe_allow_html=True)

st.markdown('<h3>Interests</h3>', unsafe_allow_html=True)
#df_interests to html
df_interests_html = df_interests.render()
st.markdown(df_interests_html, unsafe_allow_html=True)

st.markdown('<h3>References</h3>', unsafe_allow_html=True)
#df_references to html, responsive, without borders
df_references_html = df_references.render()

st.markdown(df_references_html, unsafe_allow_html=True)

