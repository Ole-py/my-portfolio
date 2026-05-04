import streamlit as st


# The first call mainly because it is the page configuration, and the second one is for the page content.
# Setting the broweser tab title, icon and layout width
st.set_page_config(
    page_title="Oletilwe|Portfolio",
    page_icon="👩🏾‍💻",  # Can be an emoji or it can be a URL to an image
    layout="wide",  # "wide" uses full width of the page, while "centered" centers the content and uses a fixed width
)
# User clicks "About" in the sidebar
# -> st.session_state["page"] = "About" (session_state is a dictionry that persists between theh reruns)
# -> app reruns (Streamlit always reruns on inyteraction)\
# ->if/elif checks if the page is stored and renders only that section's content

# """
# Hey! i see you have stopped by; i hope you stick around - there really isn't much to see and read but
# I believe that you will find the few mintues spent here worth while! 💘🎓
# """
# st.divider()

if "page" not in st.session_state:
    st.session_state.page = "Home"

# ---Sidebar navigation
with st.sidebar:
    st.title("Oletilwe.portfolio")
    st.divider()
    if st.button("Home", use_container_width=True):
        st.session_state.page = "Home"
    if st.button("About", use_container_width=True):
        st.session_state.page = "About"
    if st.button("Projects", use_container_width=True):
        st.session_state.page = "Projects"
    if st.button("Skills", use_container_width=True):
        st.session_state.page = "Skills"
    if st.button("Contact", use_container_width=True):
        st.session_state.page = "Contact"
    st.divider()
    st.caption("Built with Streamlit")

# --PAGE RENDERE---
if st.session_state.page == "Home":
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(
            "C:\\Users\\Oletilwe\\Desktop\\Instagram\\IMG_20241113_174208_242.webp",
            width=300,
        )
    with col2:
        st.title("Oletilwe Molepo")
        st.subheader("Junior Developer · Johannesburg 🇿🇦")
        st.write(
            "I build things with Python and i'm currently learning my way through the tech world."
        )

    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Coffee", "∞")
    with col2:
        st.metric("Languages", "3")
elif st.session_state.page == "About":
    st.header("All about me")
    st.write(
        "I am a junior developer with a passion for creating innovative solutions. "
        "I have a strong foundation in Python and Java,"
        " and I am always eager to learn new technologies and improve my skills."
        "I am a team player and enjoy collaborating with others to achieve common goals. "
        "I am excited to continue growing as a developer and making a positive impact in the tech industry. "
        "In my free time, I enjoy playing games like Sudoku as it helps me to think critically and improve my problem-solving skills. "
        "After Christ jazz has a special place in my heart, as it reminds me of the beauty and complexity of music, and how it can evoke emotions and tell stories without words. "
    )

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("images/JAZZ - CENK.jpeg", width=150)
    with col2:
        st.image("images/Coder.jpeg", width=155)
    with col3:
        st.image("images/📖.jpeg", width=150)
    with col4:
        st.image("images/Sudoku puzzle.jpeg", width=150)
    st.write(
        "Puzzles and music are my go-to activities for relaxation and inspiration. They help me to unwind and recharge, while also stimulating my creativity and critical thinking skills. "
        "Whether I'm solving a challenging Sudoku puzzle or listening to a soulful jazz tune, I find that these activities provide a much-needed break from the demands of work and help me to stay motivated and focused on my goals."
        "What keeps my ship steady is prayer and meditation, as they help me to find inner peace and clarity amidst the chaos of life. "
        "Through prayer and meditation, I am able to connect with my inner self and find a sense of calm and balance that allows me to navigate life's challenges with grace and resilience."
    )
elif st.session_state.page == "Projects":
    st.header("Projects")
    st.write("Here are some of the projects I've worked on:")
    st.markdown("""
    - **Student Grade Tracker**: Command-line Java app — student management, grade stats, ranking, file I/O
        - Concepts covered: OOP, ArrayLists, sorting algorithms, Comparators, file I/O, exception handling
        - Tech stack: Java, IntelliJ IDEA, JSON storage
        - Status: Nearly complete (main file remaining)
        """)
    st.divider()
    st.header("Hackathon Achievements")
    col1, col2 = st.columns(2)
    with col1:
        st.image("images/mukuru.png", width=400)
    with col2:
        st.markdown("""
    - **SheHacks Hackathon**: Got second place, hosted by Wethinkcode x Mukuru
        - Project Built: Rewards system for money transfer customers (McDonald's-style points per transaction)
        - My role: 	Coded the AI chatbot (rule-based, JavaScript), built front-end sections (HTML/CSS/JS), co-presented to judges
        - Duration: 2-day buid
        """)
elif st.session_state.page == "Skills":
    st.header("Skills")
    st.write("Here are some of the skills I have developed:")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.header("Technical skills")
        st.markdown("""
        - Object-Oriented Programming (OOP): Expert-level understanding of the four pillars (Encapsulation, Abstraction, Inheritance, and Polymorphism).
        - Java Development: Proficiency in Java syntax, memory management (static), and the Java Virtual Machine (JVM) execution model.
        - Python Programming: Experienced in using Python for problem-solving, numerical simulations, and rapid prototyping.
        - Data Structures & Algorithms: Solid grasp of efficiency (Time/Space complexity) using Arrays, Linked Lists, HashMaps, Stacks, and Trees.
        - Cloud Infrastructure: Foundation in AWS Cloud Practitioner and Generative AI implementation on the cloud.
                    """)
    with col2:
        st.header("Soft skills")
        st.markdown("""
        - Communication: Strong written and verbal communication skills, with experience presenting technical concepts to both technical and non-technical audiences.
        - Teamwork: Collaborative team player with experience working in agile development environments and cross-functional teams.
        - Problem-Solving: Analytical thinker with a passion for solving complex problems and finding innovative solutions.
        - Adaptability: Quick learner who thrives in fast-paced environments and is always eager to take on new challenges.
                    """)
    with col3:
        st.header("Software Process & Delivery")
        st.markdown("""
        - CI/CD Pipelines: Knowledge of Continuous Integration and Deployment/Delivery to automate code quality and release cycles.
        - Version Control: Professional use of Git for collaborative development and code history management.
        - Agile/Scrum Methodologies: Ability to work in peer-led, iterative environments (honed at WeThinkCode_).
        - SDLC Mastery: Understanding the full Software Development Life Cycle, from requirement gathering to maintenance.
                    """)
    with col4:
        st.header("Coordination and Professionalism")
        st.markdown("""
        - Technical Coordination: The ability to bridge the gap between complex engineering tasks and business project goals.
        - Technical Communication: Proficiency in translating "dev-speak" into clear concepts for stakeholders (as seen in our "About Me" drafts).
        - Analytical Problem Solving: A focus on "Systems Thinking"—looking at how individual components affect the entire business ecosystem.
        - Peer Mentorship: Experience in high-pressure, peer-to-peer learning environments.
                    """)
elif st.session_state.page == "Contact":
    st.header("Contact Me")
    st.write("Feel free to reach out to me through any of the following channels:")
    st.markdown(
        """
    - **Email**: oletilwemolepo06@gmail.com 📧
    - **LinkedIn**: [Oletilwe Molepo](www.linkedin.com/in/oletilwe-molepo-11209a33b) 
    - **GitHub**: [OletilweM](https://github.com/OletilweM) 
    """,
        unsafe_allow_html=True,
    )


# #Header section of the page
# #st.columns([ratio1, ratio2]) splits the page into columns
# #The numbers are relative widths: 1 and 3 mean 25% and 75% respectively
# col1, col2 = st.columns([1,3])
# with col1:
#     #st.image() is used to display an image. Use a URL or a local file path
#     st.image("C:\\Users\\Oletilwe\\Desktop\\Instagram\\IMG_20241113_174208_242.webp", width = 180)

# with col2:
#     st.title("Oletilwe's Portfolio") #st.title renders a large H1 heading
#     #st.subheader() is a much smaller heading
#     st.subheader("👩🏾‍💻 Junior Software Developer |Agile & SDLC | AWS certified | Documentation")
#     st.write("Johannnesburg, South Africa 📍")
#     st.write("oletilwemolepo06@gmail.com 📧")
#     #st.markdown() lets you write proper Markdown for richer formatting
#     st.markdown ("[Github](https://github.com/OletilweM) | [LinkedIn](www.linkedin.com/in/oletilwe-molepo-11209a33b)",
#                  unsafe_allow_html = True) #This allows the markdown to render as HTML, which is necessary for the links to work
# #A horizontal
# st.divider()
# #---ABOUT ME---
# st.header("About Me")
# st.write("""I build solutions where technical rigor meets strategic coordination.
#          Forged in the peer-to-peer intensity of WeThinkCode_,
#          I developed a foundation in Java and Python with a focus on clean code and robust systems.
#           Beyond the IDE, I am passionate about the SDLC and the architecture of a project—ensuring that technical logic aligns with human objectives.""")
# st.divider()
# #---SKILLS ---
# st.header("Skills")
# skill_col1, skill_col2, skill_col3 = st.columns(3)
# with skill_col1:
#     st.subheader("Languages")
#     #st.markdown with a butllet list
#     st.markdown("""
#             - Python
#             - Java
#             - SQLite
#             - HTML
#         """)
# with skill_col2:
#     st.subheader("Frameworks and Tools")
#     st.markdown("""
#             - Version control systems
#             - Intergrated development environment
#             - Testing frameworks
#             - Containerisation
#             """)
# with skill_col3:
#     st.subheader("Currently learning")
#     st.markdown("""
#             - Streamlit
#             - Database management software
#             - Software release management
#         """)
# st.divider()
# st.header("Projects")
# st.write("""
#    -Studet Grade tracker
# """)
