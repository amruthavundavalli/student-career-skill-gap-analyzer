import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Student Career & Skill Gap Analyzer",
    page_icon="🎓",
    layout="wide"
)

# ---------------- LANGUAGE TEXT ----------------

TEXT = {
    "English": {
        "home": "Home",
        "analysis": "Skill Analysis",
        "chat": "Career Chat",
        "welcome": "Student Career & Skill Gap Analyzer",
        "tagline": "Discover your skills. Explore your career. Plan your learning.",
        "intro": "A simple tool to compare your skills with sample career requirements.",
        "start": "Start Analysis",
        "choose_page": "Choose a page",
        "language": "Choose language",
        "details": "Student Details",
        "name": "Enter your name",
        "email": "Email (optional)",
        "career": "Choose your career goal",
        "skills": "Select the skills you already have",
        "analyze": "Analyze My Skills",
        "results": "Your Skill Analysis",
        "match": "Skill Match",
        "matched": "Skills Matched",
        "missing": "Skills to Learn",
        "have": "Skills You Have",
        "learn": "Skills You Can Learn",
        "chart": "Skill Comparison",
        "download": "Download My Report",
        "chat_title": "Career Chat Assistant",
        "chat_intro": "Ask me about careers, skills, learning resources, or project ideas.",
        "question": "Type your question",
        "send": "Send",
        "back": "Back to Home",
        "resource": "Learning resource",
        "project": "Project idea",
        "no_skills": "You have not selected any matching skills yet.",
        "all_skills": "You selected all the sample skills for this career!",
        "note": "This is an educational prototype using sample career requirements."
    },
    "తెలుగు": {
        "home": "హోమ్",
        "analysis": "నైపుణ్యాల విశ్లేషణ",
        "chat": "కెరీర్ చాట్",
        "welcome": "విద్యార్థుల కెరీర్ & నైపుణ్యాల విశ్లేషణ",
        "tagline": "మీ నైపుణ్యాలను తెలుసుకోండి. కెరీర్‌ను అన్వేషించండి.",
        "intro": "మీ నైపుణ్యాలను కెరీర్ అవసరాలతో పోల్చే సరళమైన సాధనం.",
        "start": "విశ్లేషణ ప్రారంభించండి",
        "choose_page": "పేజీని ఎంచుకోండి",
        "language": "భాషను ఎంచుకోండి",
        "details": "విద్యార్థి వివరాలు",
        "name": "మీ పేరు నమోదు చేయండి",
        "email": "ఈమెయిల్ (ఐచ్ఛికం)",
        "career": "మీ కెరీర్ లక్ష్యాన్ని ఎంచుకోండి",
        "skills": "మీకు తెలిసిన నైపుణ్యాలను ఎంచుకోండి",
        "analyze": "నా నైపుణ్యాలను విశ్లేషించండి",
        "results": "మీ నైపుణ్యాల విశ్లేషణ",
        "match": "నైపుణ్యాల సరిపోలిక",
        "matched": "సరిపోయిన నైపుణ్యాలు",
        "missing": "నేర్చుకోవాల్సిన నైపుణ్యాలు",
        "have": "మీకు తెలిసిన నైపుణ్యాలు",
        "learn": "మీరు నేర్చుకోగల నైపుణ్యాలు",
        "chart": "నైపుణ్యాల పోలిక",
        "download": "నా నివేదికను డౌన్‌లోడ్ చేయండి",
        "chat_title": "కెరీర్ చాట్ సహాయకుడు",
        "chat_intro": "కెరీర్లు, నైపుణ్యాలు, నేర్చుకునే వనరులు లేదా ప్రాజెక్టుల గురించి అడగండి.",
        "question": "మీ ప్రశ్నను టైప్ చేయండి",
        "send": "పంపండి",
        "back": "హోమ్‌కు తిరిగి వెళ్లండి",
        "resource": "నేర్చుకునే వనరు",
        "project": "ప్రాజెక్ట్ ఆలోచన",
        "no_skills": "మీరు ఇంకా సరిపోయే నైపుణ్యాలను ఎంచుకోలేదు.",
        "all_skills": "ఈ కెరీర్‌కు సంబంధించిన నమూనా నైపుణ్యాలన్నీ మీరు ఎంచుకున్నారు!",
        "note": "ఇది నమూనా కెరీర్ అవసరాలతో రూపొందించిన విద్యా ప్రాజెక్ట్."
    },
    "हिन्दी": {
        "home": "होम",
        "analysis": "कौशल विश्लेषण",
        "chat": "करियर चैट",
        "welcome": "छात्र करियर और कौशल अंतर विश्लेषक",
        "tagline": "अपने कौशल जानें। करियर खोजें। सीखने की योजना बनाएं।",
        "intro": "अपने कौशल की करियर आवश्यकताओं से तुलना करने का सरल साधन।",
        "start": "विश्लेषण शुरू करें",
        "choose_page": "पेज चुनें",
        "language": "भाषा चुनें",
        "details": "छात्र विवरण",
        "name": "अपना नाम लिखें",
        "email": "ईमेल (वैकल्पिक)",
        "career": "अपना करियर लक्ष्य चुनें",
        "skills": "अपने मौजूदा कौशल चुनें",
        "analyze": "मेरे कौशल का विश्लेषण करें",
        "results": "आपका कौशल विश्लेषण",
        "match": "कौशल मिलान",
        "matched": "मिले हुए कौशल",
        "missing": "सीखने वाले कौशल",
        "have": "आपके कौशल",
        "learn": "जिन कौशलों को आप सीख सकते हैं",
        "chart": "कौशल तुलना",
        "download": "मेरी रिपोर्ट डाउनलोड करें",
        "chat_title": "करियर चैट सहायक",
        "chat_intro": "करियर, कौशल, सीखने के संसाधनों या प्रोजेक्ट के बारे में पूछें।",
        "question": "अपना सवाल लिखें",
        "send": "भेजें",
        "back": "होम पर वापस जाएं",
        "resource": "सीखने का संसाधन",
        "project": "प्रोजेक्ट विचार",
        "no_skills": "आपने अभी तक कोई मेल खाने वाला कौशल नहीं चुना है।",
        "all_skills": "आपने इस करियर के सभी नमूना कौशल चुन लिए हैं!",
        "note": "यह नमूना करियर आवश्यकताओं पर आधारित शैक्षिक प्रोटोटाइप है।"
    },
    "ಕನ್ನಡ": {
        "home": "ಮುಖಪುಟ",
        "analysis": "ಕೌಶಲ್ಯ ವಿಶ್ಲೇಷಣೆ",
        "chat": "ವೃತ್ತಿ ಚಾಟ್",
        "welcome": "ವಿದ್ಯಾರ್ಥಿ ವೃತ್ತಿ ಮತ್ತು ಕೌಶಲ್ಯ ವಿಶ್ಲೇಷಕ",
        "tagline": "ನಿಮ್ಮ ಕೌಶಲ್ಯಗಳನ್ನು ತಿಳಿಯಿರಿ. ವೃತ್ತಿಯನ್ನು ಅನ್ವೇಷಿಸಿ.",
        "intro": "ನಿಮ್ಮ ಕೌಶಲ್ಯಗಳನ್ನು ವೃತ್ತಿಯ ಅಗತ್ಯಗಳೊಂದಿಗೆ ಹೋಲಿಸುವ ಸರಳ ಸಾಧನ.",
        "start": "ವಿಶ್ಲೇಷಣೆ ಪ್ರಾರಂಭಿಸಿ",
        "choose_page": "ಪುಟವನ್ನು ಆಯ್ಕೆಮಾಡಿ",
        "language": "ಭಾಷೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ",
        "details": "ವಿದ್ಯಾರ್ಥಿ ವಿವರಗಳು",
        "name": "ನಿಮ್ಮ ಹೆಸರನ್ನು ನಮೂದಿಸಿ",
        "email": "ಇಮೇಲ್ (ಐಚ್ಛಿಕ)",
        "career": "ನಿಮ್ಮ ವೃತ್ತಿ ಗುರಿಯನ್ನು ಆಯ್ಕೆಮಾಡಿ",
        "skills": "ನಿಮಗೆ ತಿಳಿದಿರುವ ಕೌಶಲ್ಯಗಳನ್ನು ಆಯ್ಕೆಮಾಡಿ",
        "analyze": "ನನ್ನ ಕೌಶಲ್ಯಗಳನ್ನು ವಿಶ್ಲೇಷಿಸಿ",
        "results": "ನಿಮ್ಮ ಕೌಶಲ್ಯ ವಿಶ್ಲೇಷಣೆ",
        "match": "ಕೌಶಲ್ಯ ಹೊಂದಾಣಿಕೆ",
        "matched": "ಹೊಂದಾಣಿಕೆಯ ಕೌಶಲ್ಯಗಳು",
        "missing": "ಕಲಿಯಬೇಕಾದ ಕೌಶಲ್ಯಗಳು",
        "have": "ನಿಮಗೆ ತಿಳಿದಿರುವ ಕೌಶಲ್ಯಗಳು",
        "learn": "ನೀವು ಕಲಿಯಬಹುದಾದ ಕೌಶಲ್ಯಗಳು",
        "chart": "ಕೌಶಲ್ಯ ಹೋಲಿಕೆ",
        "download": "ನನ್ನ ವರದಿಯನ್ನು ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ",
        "chat_title": "ವೃತ್ತಿ ಚಾಟ್ ಸಹಾಯಕ",
        "chat_intro": "ವೃತ್ತಿ, ಕೌಶಲ್ಯ, ಕಲಿಕಾ ಸಂಪನ್ಮೂಲ ಅಥವಾ ಯೋಜನೆಗಳ ಬಗ್ಗೆ ಕೇಳಿ.",
        "question": "ನಿಮ್ಮ ಪ್ರಶ್ನೆಯನ್ನು ಟೈಪ್ ಮಾಡಿ",
        "send": "ಕಳುಹಿಸಿ",
        "back": "ಮುಖಪುಟಕ್ಕೆ ಹಿಂತಿರುಗಿ",
        "resource": "ಕಲಿಕಾ ಸಂಪನ್ಮೂಲ",
        "project": "ಯೋಜನೆಯ ಕಲ್ಪನೆ",
        "no_skills": "ನೀವು ಇನ್ನೂ ಹೊಂದಾಣಿಕೆಯ ಕೌಶಲ್ಯಗಳನ್ನು ಆಯ್ಕೆಮಾಡಿಲ್ಲ.",
        "all_skills": "ಈ ವೃತ್ತಿಗೆ ಸಂಬಂಧಿಸಿದ ಎಲ್ಲಾ ಮಾದರಿ ಕೌಶಲ್ಯಗಳನ್ನು ಆಯ್ಕೆಮಾಡಿದ್ದೀರಿ!",
        "note": "ಇದು ಮಾದರಿ ವೃತ್ತಿ ಅಗತ್ಯಗಳನ್ನು ಬಳಸುವ ಶೈಕ್ಷಣಿಕ ಮಾದರಿ."
    }
}

# ---------------- CAREER DATA ----------------

career_skills = {
    "Python Developer": [
        "Python", "SQL", "Git", "Problem Solving",
        "Object-Oriented Programming"
    ],
    "Data Analyst": [
        "Python", "SQL", "Excel", "Statistics",
        "Data Visualization"
    ],
    "Web Developer": [
        "HTML", "CSS", "JavaScript", "Python", "Git"
    ],
    "AI Engineer": [
        "Python", "Machine Learning", "Statistics",
        "SQL", "Deep Learning"
    ],
    "Software Engineer": [
        "Python", "Java", "Data Structures",
        "Algorithms", "Git"
    ]
}

learning_resources = {
    "Python": "https://www.python.org/about/gettingstarted/",
    "SQL": "https://www.w3schools.com/sql/",
    "Git": "https://git-scm.com/doc",
    "Problem Solving": "https://www.khanacademy.org/computing",
    "Object-Oriented Programming": "https://www.w3schools.com/python/python_classes.asp",
    "Excel": "https://support.microsoft.com/excel",
    "Statistics": "https://www.khanacademy.org/math/statistics-probability",
    "Data Visualization": "https://www.tableau.com/learn",
    "HTML": "https://www.w3schools.com/html/",
    "CSS": "https://www.w3schools.com/css/",
    "JavaScript": "https://www.w3schools.com/js/",
    "Machine Learning": "https://www.coursera.org/learn/machine-learning",
    "Deep Learning": "https://www.deeplearning.ai/",
    "Java": "https://dev.java/learn/",
    "Data Structures": "https://www.geeksforgeeks.org/data-structures/",
    "Algorithms": "https://www.khanacademy.org/computing/computer-science/algorithms"
}

project_ideas = {
    "Python": "Build a calculator or quiz application.",
    "SQL": "Create a student database project.",
    "Git": "Upload a project to GitHub.",
    "Problem Solving": "Practice beginner coding challenges.",
    "Object-Oriented Programming": "Build a library management system.",
    "Excel": "Create a student marks analysis sheet.",
    "Statistics": "Analyze a small dataset.",
    "Data Visualization": "Create a chart dashboard.",
    "HTML": "Build a personal portfolio page.",
    "CSS": "Style a personal portfolio page.",
    "JavaScript": "Build an interactive webpage.",
    "Machine Learning": "Build a simple prediction project.",
    "Deep Learning": "Explore an image classification project.",
    "Java": "Build a simple banking application.",
    "Data Structures": "Implement a stack or queue.",
    "Algorithms": "Practice sorting and searching."
}

# ---------------- LANGUAGE AND NAVIGATION ----------------

if "language" not in st.session_state:
    st.session_state.language = "English"

if "page" not in st.session_state:
    st.session_state.page = "Home"

language = st.sidebar.selectbox(
    "🌐 Language / భాష / भाषा / ಭಾಷೆ",
    ["English", "తెలుగు", "हिन्दी", "ಕನ್ನಡ"],
    index=["English", "తెలుగు", "हिन्दी", "ಕನ್ನಡ"].index(
        st.session_state.language
    )
)
st.session_state.language = language
t = TEXT[language]

page_names = ["Home", "Skill Analysis", "Career Chat"]
page_labels = {
    "Home": t["home"],
    "Skill Analysis": t["analysis"],
    "Career Chat": t["chat"]
}

selected_page = st.sidebar.radio(
    t["choose_page"],
    page_names,
    format_func=lambda x: page_labels[x],
    index=page_names.index(st.session_state.page)
)
st.session_state.page = selected_page

# ---------------- HOME PAGE ----------------

if selected_page == "Home":
    st.markdown(
        """
        <div style="text-align:center; padding:45px 10px;">
            <div style="font-size:85px;">🎓📊</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.title(t["welcome"])
    st.subheader(t["tagline"])
    st.write(t["intro"])

    st.write("")
    if st.button(t["start"], type="primary", use_container_width=True):
        st.session_state.page = "Skill Analysis"
        st.rerun()

    st.divider()
    st.subheader("📊 " + t["analysis"])
    st.write("Explore your current skills and compare them with career requirements.")

    st.subheader("💬 " + t["chat"])
    st.write(t["chat_intro"])

# ---------------- SKILL ANALYSIS PAGE ----------------

elif selected_page == "Skill Analysis":
    st.title("📊 " + t["analysis"])
    st.write(t["note"])

    st.subheader(t["details"])
    name = st.text_input(t["name"])
    email = st.text_input(t["email"])

    career = st.selectbox(
        t["career"],
        list(career_skills.keys())
    )

    all_skills = sorted({
        skill
        for skills in career_skills.values()
        for skill in skills
    })

    student_skills = st.multiselect(
        t["skills"],
        all_skills
    )

    if st.button(t["analyze"], type="primary"):
        required = career_skills[career]
        matched = [s for s in required if s in student_skills]
        missing = [s for s in required if s not in student_skills]
        percentage = round(len(matched) / len(required) * 100)

        st.session_state.analysis_result = {
            "name": name,
            "email": email,
            "career": career,
            "matched": matched,
            "missing": missing,
            "percentage": percentage
        }

    if "analysis_result" in st.session_state:
        result = st.session_state.analysis_result
        st.divider()
        st.header(t["results"])

        if result["name"]:
            st.write(f"Hello, **{result['name']}**!")

        st.write(f"Career goal: **{result['career']}**")

        c1, c2, c3 = st.columns(3)
        c1.metric(t["match"], f"{result['percentage']}%")
        c2.metric(t["matched"], len(result["matched"]))
        c3.metric(t["missing"], len(result["missing"]))

        st.progress(result["percentage"] / 100)

        st.subheader("✅ " + t["have"])
        if result["matched"]:
            for skill in result["matched"]:
                st.write("✔️ " + skill)
        else:
            st.info(t["no_skills"])

        st.subheader("📚 " + t["learn"])
        if result["missing"]:
            for skill in result["missing"]:
                st.markdown(f"**{skill}**")
                st.write(
                    f"{t['resource']}: "
                    f"[Open resource]({learning_resources[skill]})"
                )
                st.write(f"{t['project']}: {project_ideas[skill]}")
        else:
            st.success(t["all_skills"])

        st.subheader("📈 " + t["chart"])
        chart_data = pd.DataFrame({
            "Category": [t["matched"], t["missing"]],
            "Number": [len(result["matched"]), len(result["missing"])]
        })
        st.bar_chart(chart_data.set_index("Category"))

        report = f"""
STUDENT CAREER & SKILL GAP ANALYZER
Student: {result['name']}
Career: {result['career']}
Skill match: {result['percentage']}%

Matched skills:
{chr(10).join(result['matched'])}

Skills to learn:
{chr(10).join(result['missing'])}

Note: Educational prototype using sample career requirements.
"""
        st.download_button(
            t["download"],
            data=report,
            file_name="career_skill_analysis.txt",
            mime="text/plain"
        )

# ---------------- CAREER CHAT PAGE ----------------

elif selected_page == "Career Chat":
    st.title("💬 " + t["chat_title"])
    st.write(t["chat_intro"])

    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = []

    for message in st.session_state.chat_messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    prompt = st.chat_input(t["question"])

    if prompt:
        st.session_state.chat_messages.append({
            "role": "user",
            "content": prompt
        })

        lower_prompt = prompt.lower()

        if any(word in lower_prompt for word in [
            "python", "skill", "learn", "నైపుణ్య", "सीख", "ಕೌಶಲ್ಯ"
        ]):
            if language == "తెలుగు":
                answer = "మీ లక్ష్య కెరీర్‌కు అవసరమైన నైపుణ్యాలను ఎంచుకుని, ఒక్కొక్కటిగా నేర్చుకోండి. చిన్న ప్రాజెక్టులతో సాధన చేయండి."
            elif language == "हिन्दी":
                answer = "अपने करियर लक्ष्य के लिए जरूरी कौशल चुनें। उन्हें एक-एक करके सीखें और छोटे प्रोजेक्ट बनाकर अभ्यास करें।"
            elif language == "ಕನ್ನಡ":
                answer = "ನಿಮ್ಮ ವೃತ್ತಿ ಗುರಿಗೆ ಬೇಕಾದ ಕೌಶಲ್ಯಗಳನ್ನು ಆಯ್ಕೆಮಾಡಿ. ಒಂದೊಂದಾಗಿ ಕಲಿಯಿರಿ ಮತ್ತು ಸಣ್ಣ ಯೋಜನೆಗಳ ಮೂಲಕ ಅಭ್ಯಾಸ ಮಾಡಿ."
            else:
                answer = "Choose the skills needed for your career goal. Learn them one at a time and practise by building small projects."

        elif any(word in lower_prompt for word in [
            "career", "job", "కెరీర్", "करियर", "ವೃತ್ತಿ"
        ]):
            if language == "తెలుగు":
                answer = "మీకు ఆసక్తి ఉన్న రంగాన్ని ఎంచుకోండి. ఆ రంగంలోని ఉద్యోగ ప్రకటనలను పరిశీలించి అవసరమైన నైపుణ్యాలను గుర్తించండి."
            elif language == "हिन्दी":
                answer = "अपनी रुचि के क्षेत्र को चुनें। उस क्षेत्र की नौकरी की आवश्यकताओं को पढ़ें और जरूरी कौशलों की सूची बनाएं।"
            elif language == "ಕನ್ನಡ":
                answer = "ನಿಮಗೆ ಆಸಕ್ತಿ ಇರುವ ಕ್ಷೇತ್ರವನ್ನು ಆಯ್ಕೆಮಾಡಿ. ಆ ಕ್ಷೇತ್ರದ ಉದ್ಯೋಗಗಳ ಅಗತ್ಯಗಳನ್ನು ನೋಡಿ ಬೇಕಾದ ಕೌಶಲ್ಯಗಳ ಪಟ್ಟಿಯನ್ನು ತಯಾರಿಸಿ."
            else:
                answer = "Choose a field that interests you. Review job descriptions in that field and make a list of the skills they commonly request."

        else:
            if language == "తెలుగు":
                answer = "మంచి ప్రశ్న! మీ లక్ష్య కెరీర్ మరియు మీకు తెలిసిన నైపుణ్యాలను చెప్పండి. వాటి ఆధారంగా నేర్చుకునే ప్రణాళిక రూపొందించడంలో సహాయం చేస్తాను."
            elif language == "हिन्दी":
                answer = "अच्छा सवाल! अपना करियर लक्ष्य और मौजूदा कौशल बताएं। मैं आपके लिए सीखने की योजना बनाने में मदद कर सकता हूँ।"
            elif language == "ಕನ್ನಡ":
                answer = "ಒಳ್ಳೆಯ ಪ್ರಶ್ನೆ! ನಿಮ್ಮ ವೃತ್ತಿ ಗುರಿ ಮತ್ತು ಈಗಾಗಲೇ ತಿಳಿದಿರುವ ಕೌಶಲ್ಯಗಳನ್ನು ತಿಳಿಸಿ. ಕಲಿಕೆಯ ಯೋಜನೆ ರೂಪಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತೇನೆ."
            else:
                answer = "Good question! Tell me your career goal and the skills you already know. I can help you make a learning plan."

        st.session_state.chat_messages.append({
            "role": "assistant",
            "content": answer
        })
        st.rerun()

    if st.button("Clear Chat"):
        st.session_state.chat_messages = []
        st.rerun()