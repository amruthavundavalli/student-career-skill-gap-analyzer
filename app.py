import streamlit as st
import pandas as pd

# --------------------------------
# PAGE CONFIGURATION
# --------------------------------

st.set_page_config(
    page_title="Student Career Analyzer",
    page_icon="🎓",
    layout="wide"
)

# --------------------------------
# CUSTOM DESIGN
# --------------------------------

st.title("🎓 Student Career & Skill Gap Analyzer")

st.markdown(
    """
    Discover your career path, identify your skill gaps,
    and receive practical learning recommendations.
    """
)

st.divider()

# --------------------------------
# CAREER SKILLS DATABASE
# --------------------------------

career_skills = {
    "Python Developer": [
        "Python", "OOP", "SQL", "Git"
    ],

    "Data Analyst": [
        "Python", "SQL", "Excel", "Power BI"
    ],

    "Web Developer": [
        "HTML", "CSS", "JavaScript", "Python"
    ],

    "AI Engineer": [
        "Python", "Machine Learning", "Mathematics"
    ],

    "Software Engineer": [
        "Python", "DSA", "SQL", "Git"
    ]
}

# --------------------------------
# LEARNING RESOURCES
# --------------------------------

resources = {
    "Python":
        "https://www.python.org/about/gettingstarted/",

    "SQL":
        "https://www.w3schools.com/sql/",

    "HTML":
        "https://www.w3schools.com/html/",

    "CSS":
        "https://www.w3schools.com/css/",

    "JavaScript":
        "https://www.w3schools.com/js/",

    "Excel":
        "https://support.microsoft.com/excel",

    "Power BI":
        "https://learn.microsoft.com/power-bi/",

    "Machine Learning":
        "https://www.kaggle.com/learn",

    "Mathematics":
        "https://www.khanacademy.org/math",

    "OOP":
        "https://www.geeksforgeeks.org/object-oriented-programming-in-python/",

    "Git":
        "https://git-scm.com/doc",

    "DSA":
        "https://www.geeksforgeeks.org/data-structures/"
}

# --------------------------------
# PROJECT RECOMMENDATIONS
# --------------------------------

projects = {
    "Python":
        "Build a Student Attendance Tracker",

    "SQL":
        "Create a Student Database Management System",

    "HTML":
        "Build a Student Portfolio Website",

    "CSS":
        "Design a Responsive College Website",

    "JavaScript":
        "Create an Interactive Quiz Application",

    "Excel":
        "Build a Student Performance Dashboard",

    "Power BI":
        "Create a Student Analytics Dashboard",

    "Machine Learning":
        "Build a Student Performance Prediction Model",

    "Mathematics":
        "Practice Statistical Analysis Using Python",

    "OOP":
        "Create a Library Management System",

    "Git":
        "Upload a Python Project to GitHub",

    "DSA":
        "Build a Sorting Visualizer"
}

# --------------------------------
# STUDENT DETAILS
# --------------------------------

st.header("👩‍🎓 Student Information")

name = st.text_input(
    "Enter your full name",
    placeholder="Example: Student Name"
)

email = st.text_input(
    "Enter your email (optional)",
    placeholder="student@example.com"
)

# --------------------------------
# CAREER SELECTION
# --------------------------------

st.header("💼 Choose Your Target Career")

career = st.selectbox(
    "Select your dream career",
    list(career_skills.keys())
)

st.info(
    f"Required skills for {career}: "
    + ", ".join(career_skills[career])
)

# --------------------------------
# STUDENT SKILLS
# --------------------------------

st.header("🧠 Your Current Skills")

skills = st.multiselect(
    "Select the skills you already know",
    list(resources.keys())
)

# --------------------------------
# ANALYSIS BUTTON
# --------------------------------

if st.button("🚀 Analyze My Skills", use_container_width=True):

    if not name.strip():

        st.warning("Please enter your name.")

    else:

        # Required skills
        required = career_skills[career]

        # Matching skills
        matched = [
            skill for skill in required
            if skill in skills
        ]

        # Missing skills
        missing = [
            skill for skill in required
            if skill not in skills
        ]

        # Calculate percentage
        percentage = (
            len(matched) / len(required)
        ) * 100

        st.divider()

        # --------------------------------
        # ANALYSIS RESULTS
        # --------------------------------

        st.header("📊 Your Career Analysis")

        st.success(
            f"Welcome, {name}! Your analysis is ready."
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Skill Match",
                f"{percentage:.0f}%"
            )

        with col2:
            st.metric(
                "Skills Learned",
                len(matched)
            )

        with col3:
            st.metric(
                "Skills Remaining",
                len(missing)
            )

        # Progress bar
        st.subheader("Your Career Readiness Progress")

        st.progress(
            int(percentage)
        )

        # --------------------------------
        # MATCHED SKILLS
        # --------------------------------

        st.subheader("✅ Skills You Already Know")

        if matched:

            for skill in matched:
                st.write(f"✔️ {skill}")

        else:

            st.write("No matching skills selected yet.")

        # --------------------------------
        # MISSING SKILLS
        # --------------------------------

        st.subheader("📚 Skills You Need to Learn")

        if missing:

            for skill in missing:

                st.markdown(f"### 📌 {skill}")

                st.markdown(
                    f"[Learn {skill}]({resources[skill]})"
                )

                st.write(
                    "**Recommended practical project:**"
                )

                st.write(projects[skill])

                st.divider()

        else:

            st.success(
                "You have selected all the required skills!"
            )

        # --------------------------------
        # PROGRESS CHART
        # --------------------------------

        st.header("📈 Skill Progress Chart")

        chart_data = pd.DataFrame({
            "Category": [
                "Skills Learned",
                "Skills Remaining"
            ],

            "Count": [
                len(matched),
                len(missing)
            ]
        })

        st.bar_chart(
            chart_data.set_index("Category")
        )

        # --------------------------------
        # CAREER REPORT
        # --------------------------------

        st.header("📄 Download Your Career Report")

        report = f"""
STUDENT CAREER & SKILL GAP ANALYSIS
===================================

Student Name: {name}
Email: {email}

Target Career: {career}

Skill Match: {percentage:.0f}%

-----------------------------------
SKILLS ALREADY KNOWN
-----------------------------------

{chr(10).join(matched) if matched else "None"}

-----------------------------------
SKILLS TO LEARN
-----------------------------------

{chr(10).join(missing) if missing else "None"}

-----------------------------------
LEARNING RECOMMENDATIONS
-----------------------------------
"""

        for skill in missing:

            report += f"""

Skill: {skill}

Learning Resource:
{resources[skill]}

Recommended Project:
{projects[skill]}

-----------------------------------
"""

        report += """

Note:
This report provides learning guidance.
Skill match is based on selected skills
and listed career requirements.
"""

        st.download_button(
            label="📥 Download My Career Report",

            data=report,

            file_name="student_career_report.txt",

            mime="text/plain",

            use_container_width=True
        )

        st.success(
            "Your career analysis is complete!"
        )

# --------------------------------
# FOOTER
# --------------------------------

st.divider()

st.caption(
    "Student Career & Skill Gap Analyzer | "
    "A Student Real-World Problem Solving Project"
)