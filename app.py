import streamlit as st 

#The first call mainly because it is the page configuration, and the second one is for the page content.
#Setting the broweser tab title, icon and layout width
st.set_page_config(
    page_title = "Oletilwe's Portfolio",
    page_icon = "👩🏾‍💻", #Can be an emoji or it can be a URL to an image
    layout = "wide" #"wide" uses full width of the page, while "centered" centers the content and uses a fixed width
)
#Header section of the page
#st.columns([ratio1, ratio2]) splits the page into columns
#The numbers are relative widths: 1 and 3 mean 25% and 75% respectively 
col1, col2 = st.columns([1,3])
with col1:
    #st.image() is used to display an image. Use a URL or a local file path 
    st.image("C:\\Users\\Oletilwe\\Desktop\\Instagram\\IMG_20241113_174208_242.webp", width = 180)

with col2:
    st.title("Oletilwe's Portfolio") #st.title renders a large H1 heading
    #st.subheader() is a much smaller heading 
    st.subheader("👩🏾‍💻 Junior Software Developer |Agile & SDLC | AWS certified | Documentation")
    st.write("Johannnesburg, South Africa 📍")
    st.write("oletilwemolepo06@gmail.com 📧")
    #st.markdown() lets you write proper Markdown for richer formatting 
    st.markdown ("[Github](https://github.com/OletilweM) | [LinkedIn](www.linkedin.com/in/oletilwe-molepo-11209a33b)", 
                 unsafe_allow_html = True) #This allows the markdown to render as HTML, which is necessary for the links to work
#A horizontal 
st.divider()
#---ABOUT ME---
st.header("About Me")
st.write("""I build solutions where technical rigor meets strategic coordination.
         Forged in the peer-to-peer intensity of WeThinkCode_, 
         I developed a foundation in Java and Python with a focus on clean code and robust systems.
          Beyond the IDE, I am passionate about the SDLC and the architecture of a project—ensuring that technical logic aligns with human objectives.""")        
st.divider()
#---SKILLS ---
st.header("Skills")
skill_col1, skill_col2, skill_col3 = st.columns(3)
with skill_col1:
    st.subheader("Languages")
    #st.markdown with a butllet list 
    st.markdown("""
            - Python
            - Java
            - SQLite
            - HTML
        """)
with skill_col2:
    st.subheader("Frameworks and Tools")
    st.markdown("""
            - Version control systems 
            - Intergrated development environment 
            - Testing frameworks
            - Containerisation
            """)
with skill_col3:
    st.subheader("Currently learning")
    st.markdown("""
            - Streamlit 
            - Database management software 
            - Software release management 
        """)
st.divider()
