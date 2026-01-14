# 🚀 AI Resume Builder

Live link  https://ai-resume-build-vijay.streamlit.app/
A powerful Streamlit-based application that uses Google's Gemini AI to generate professional resumes, cover letters, and portfolio content.

## Features

- 📝 **Profile Management**: Save your personal and professional details once, use everywhere
- 📄 **AI Resume Generator**: Create professional resumes tailored to specific job roles
- ✉️ **Cover Letter Generator**: Generate personalized cover letters for job applications
- 🎨 **Portfolio Content Generator**: Create engaging content for your portfolio website

## Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd AI_Resume_Builder
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Get your Gemini API Key:
   - Visit: https://makersuite.google.com/app/apikey
   - Sign in with your Google account
   - Create a new API key
   - **Note**: You'll enter this in the app's sidebar when you run it (no need to hardcode it!)

## Usage

### Local Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. Open your browser and navigate to the URL shown (usually `http://localhost:8501`)

3. Enter your Gemini API Key in the sidebar

4. Follow these steps:
   - Go to "📝 My Profile (Input Data)" and fill in your details
   - Click "💾 Save Profile"
   - Navigate to any section (Resume, Cover Letter, or Portfolio)
   - Generate and download your content!

### Deploy on Streamlit Cloud (Shareable)

1. Push your code to GitHub (already done!)

2. Go to [Streamlit Cloud](https://streamlit.io/cloud)

3. Sign in with your GitHub account

4. Click "New app"

5. Select your repository: `Vijay-Saini-B24BS1408/AI-Resume-Portfolio-Builder`

6. Click "Deploy"

7. Your app will be live at: `https://your-app-name.streamlit.app`

**Note**: Users will need to enter their own Gemini API key in the sidebar to use the app.

## Requirements

- Python 3.7+
- streamlit
- google-generativeai
- fpdf2

## Security

- **No hardcoded API keys**: Each user enters their own API key in the sidebar
- Safe to share: You can share this repository without exposing any API keys
- Users need their own Gemini API key to use the app

## Deployment

This app is ready to deploy on:
- ✅ Streamlit Cloud (Recommended - Free)
- ✅ Heroku
- ✅ AWS
- ✅ Any platform that supports Python/Streamlit

## License

This project is open source and available for personal and commercial use.
