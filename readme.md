🎯 InterviewAI — AI Voice Interview Coach

A real-time AI-powered mock interview platform that helps students practice and prepare for campus placements, internships, and college admissions using voice as the primary interface.


🏆 Built For
Murf AI Hackathon — Voice Agent Challenge
Use Case: AI Voice Interview Coach for Students

💡 Problem Statement
Many students struggle to perform well in interviews due to lack of realistic practice opportunities. Traditional preparation methods like reading books or watching tutorials do not simulate real interview conditions. Students face anxiety, poor communication, and difficulty structuring answers during actual interviews.
InterviewAI solves this by providing a realistic voice-based mock interview experience with personalized feedback — available 24/7, completely free.

✨ Features

Fully voice-based conversation — no typing needed
Real-time speech recognition using Deepgram Nova-2
Natural AI voice powered by Murf Falcon TTS
Three interview modes — Campus Placement, Internship, College Admission
Company specific questions — TCS, Google, Amazon, Microsoft, Deloitte, IITs and more
Detailed feedback report with scores, strengths, and improvement areas
Multilingual — English, Hindi, and Hinglish supported
Beautiful animated UI with gradient orb


🛠️ Tech Stack

Real-time Voice — LiveKit
Speech to Text — Deepgram Nova-2
AI Brain — Groq LLaMA 3.3 70B
Text to Speech — Murf Falcon
Voice Activity Detection — Silero VAD
Frontend — HTML + CSS + JavaScript
Backend — Python


📁 Project Structure
interview-bot/
├── agenst.py         ← AI Interview Agent
├── create_room.py    ← Room creator and token generator
├── index.html        ← Frontend UI
├── .env              ← API keys
└── README.md         ← This file

⚙️ Setup
Step 1 — Install dependencies
pip install livekit-agents livekit-murf livekit-plugins-deepgram livekit-plugins-silero livekit-plugins-groq python-dotenv
Step 2 — Add API keys to .env
LIVEKIT_URL=your_livekit_url
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret
DEEPGRAM_API_KEY=your_deepgram_api_key
MURF_API_KEY=your_murf_api_key
GROQ_API_KEY=your_groq_api_key
Step 3 — Run
python agenst.py dev
python create_room.py
Step 4 — Open index.html in Chrome, paste token, click Start Interview

🎯 How It Works
Student speaks → Deepgram transcribes → Groq AI processes → Murf Falcon speaks response → Student hears via LiveKit

Student joins the room via the web interface
AI interviewer greets and asks for name and interview type
Student mentions the company they are applying to
Agent asks 5 company specific questions
After each answer agent gives brief encouraging feedback
At the end agent delivers a detailed 8 point feedback report


👨‍💻 Team
Built with ❤️ for the Murf AI Hackathon