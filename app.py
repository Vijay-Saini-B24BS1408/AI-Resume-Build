import streamlit as st
import google.generativeai as genai
from fpdf import FPDF

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="AI Resume Builder", layout="wide", page_icon="🚀")

# =======================================================
# 👇👇👇 ENTER YOUR GEMINI API KEY HERE 👇👇👇
# Bhai, apni KEY yahan daalna. (Maine apki key hata di hai security ke liye)
GOOGLE_API_KEY = "AIzaSyDcdtXzznstUqn3EYC2jG6jxNcvbmlSMLY"
# =======================================================

# --- HELPER FUNCTION: PDF GENERATOR (FIXED) ---
def create_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Text cleaning to avoid unicode errors
    try:
        clean_text = text.encode('latin-1', 'replace').decode('latin-1')
        pdf.multi_cell(0, 10, clean_text)
        
        # ✅ FIXED LINE: .encode('latin-1') HATA DIYA HAI
        return bytes(pdf.output(dest='S')) 
    except Exception as e:
        return f"PDF Error: {e}".encode()

# --- HELPER FUNCTION: AI GENERATOR ---
def get_gemini_response(prompt):
    try:
        genai.configure(api_key=GOOGLE_API_KEY)
        # Smart Model Selection
        try:
            model = genai.GenerativeModel('gemini-3-flash')
            response = model.generate_content(prompt)
        except:
            model = genai.GenerativeModel('gemini-2.5-flash')
            response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error connecting to AI: {e}"

# --- INITIALIZE SESSION STATE ---
if 'user_data' not in st.session_state:
    st.session_state.user_data = {
        "name": "", "email": "", "mobile": "", 
        "linkedin": "", "skills": "", "experience": "", 
        "projects": "", "achievements": ""
    }

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("📂 Dashboard")
menu = st.sidebar.radio("Go to:", 
    ["📝 My Profile", 
     "📄 Generate Resume", 
     "✉️ Generate Cover Letter", 
     "🎨 Generate Portfolio"])

st.sidebar.markdown("---")
st.sidebar.info("Quickly build your professional documents using AI!")

# =======================================================
# 1️⃣ MY PROFILE SECTION
# =======================================================
if menu == "📝 My Profile":
    st.title("📝 Fill Your Details Here")
    st.info("Fill once, use everywhere!")
    
    with st.form("profile_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Full Name", value=st.session_state.user_data["name"])
            email = st.text_input("Email", value=st.session_state.user_data["email"])
            linkedin = st.text_input("LinkedIn/GitHub", value=st.session_state.user_data["linkedin"])
        with col2:
            mobile = st.text_input("Mobile Number", value=st.session_state.user_data["mobile"])
            
        skills = st.text_area("Skills", value=st.session_state.user_data["skills"])
        experience = st.text_area("Experience", value=st.session_state.user_data["experience"])
        projects = st.text_area("Projects", value=st.session_state.user_data["projects"])
        achievements = st.text_area("Achievements", value=st.session_state.user_data["achievements"])

        if st.form_submit_button("💾 Save Profile"):
            st.session_state.user_data = {
                "name": name, "email": email, "mobile": mobile,
                "linkedin": linkedin, "skills": skills, 
                "experience": experience, "projects": projects,
                "achievements": achievements
            }
            st.success("Profile saved! Go to 'Generate Resume'.")

# =======================================================
# 2️⃣ RESUME GENERATOR
# =======================================================
elif menu == "📄 Generate Resume":
    st.title("📄 AI Resume Builder")
    
    if not st.session_state.user_data["name"]:
        st.warning("⚠️ Please fill your profile first!")
    else:
        target_role = st.text_input("Target Job Role (e.g. Data Scientist)")
        
        if st.button("Generate Resume"):
            data = st.session_state.user_data
            prompt = f"""
            Write a professional resume for {data['name']}.
            Role: {target_role}
            Contact: {data['email']}, {data['mobile']}, {data['linkedin']}
            Skills: {data['skills']}
            Experience: {data['experience']}
            Projects: {data['projects']}
            Achievements: {data['achievements']}
            Format: SUMMARY, SKILLS, EXPERIENCE, PROJECTS.
            """
            with st.spinner("Generating Resume..."):
                result = get_gemini_response(prompt)
                st.markdown(result)
                st.download_button("Download PDF", create_pdf(result), file_name="Resume.pdf", mime="application/pdf")

# =======================================================
# 3️⃣ COVER LETTER GENERATOR
# =======================================================
elif menu == "✉️ Generate Cover Letter":
    st.title("✉️ AI Cover Letter Generator")
    
    if not st.session_state.user_data["name"]:
        st.warning("⚠️ Please fill your profile first!")
    else:
        col1, col2 = st.columns(2)
        with col1:
            company_name = st.text_input("Company Name")
        with col2:
            hiring_manager = st.text_input("Manager Name", value="Hiring Manager")
        role = st.text_input("Job Position")

        if st.button("Generate Cover Letter"):
            data = st.session_state.user_data
            prompt = f"""
            Write a Cover Letter for {data['name']} to {company_name} for {role}.
            Manager: {hiring_manager}
            Skills: {data['skills']}
            Experience: {data['experience']}
            Tone: Professional.
            """
            with st.spinner("Writing Cover Letter..."):
                result = get_gemini_response(prompt)
                st.markdown(result)
                st.download_button("Download PDF", create_pdf(result), file_name="Cover_Letter.pdf", mime="application/pdf")

# =======================================================
# 4️⃣ PORTFOLIO GENERATOR
# =======================================================
elif menu == "🎨 Generate Portfolio":
    st.title("🎨 AI Portfolio Content")
    
    if not st.session_state.user_data["name"]:
        st.warning("⚠️ Please fill your profile first!")
    else:
        if st.button("Generate Portfolio Content"):
            data = st.session_state.user_data
            prompt = f"""
            Create Portfolio Website Content for {data['name']}.
            Intro: {data['skills']}
            Projects: {data['projects']}
            Style: Creative & Catchy.
            """
            with st.spinner("Creating Content..."):
                result = get_gemini_response(prompt)
                st.markdown(result)
                st.download_button("Download Text", result, file_name="Portfolio.txt", mime="text/plain")