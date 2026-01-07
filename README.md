## 🤖 TalentScout Hiring Assistant

An AI-powered chatbot built using Streamlit and LLM (Groq API) to assist in the initial screening of job candidates.
The chatbot collects candidate information, identifies their technical skill set, and generates relevant technical interview questions based on their responses.

This project is designed to simulate the first round of a technical hiring process, making recruitment faster, structured, and more efficient.

## 📌 Project Overview

The TalentScout Hiring Assistant is a conversational chatbot that:

Collects essential candidate details (name, email, phone, experience, location, position).

Asks candidates about their technical skill stack.

Automatically generates technical interview questions based on the technologies mentioned.

Provides a smooth chat-based interface with a modern UI.

Can be deployed online using Streamlit Cloud (Free).

## 🎯 Objective

To automate the initial screening process by replacing static forms with an interactive AI-driven interview assistant.

## ⚙️ Installation Instructions

Follow these steps to set up and run the project on your system:

1️⃣ Clone the Repository

    git clone https://github.com/Sulekha10/talentscout-chatbot.git

    cd talentscout-chatbot

2️⃣ Create a Virtual Environment (Optional but Recommended)

    python -m venv venv

    source venv/bin/activate       # For Linux/Mac

    venv\Scripts\activate          # For Windows

3️⃣ Install Dependencies

    pip install -r requirements.txt

4️⃣ Set Up API Key (Groq)

   Create a .env file in the project root:

GROQ_API_KEY=your_api_key_here

Or set it as an environment variable in your system.

5️⃣ Run the Application

    streamlit run app.py

The application will open in your browser.

## 🧭 Usage Guide

## 🗨 How to Use the Chatbot

1. Launch the application.

2. The chatbot greets you and asks for:

. Full Name

. Email Address

. Phone Number

. Years of Experience

. Job Position

. Location

. Tech Stack (e.g., Python, ML, SQL)

3. Based on your tech stack, the chatbot:

. Generates relevant technical interview questions.

4. After questions are displayed, the chatbot ends the session politely.

## 👩‍💼 Intended Users

. Recruiters

. HR teams

. Hiring managers

. Internship coordinators

## 🛠 Technical Details

## 📚 Libraries & Tools Used

    Streamlit
    Groq API
    Python
    Custom Regex (email & phone)

## 🧠 Model Details

The chatbot uses Large Language Models (LLMs) provided by Groq API to:

. Interpret the candidate’s tech stack.

. Generate context-aware technical questions.

The model dynamically adapts the questions based on:

. Programming languages

. Frameworks

. Databases

. AI/ML tools

## 🏗 Architecture Design

Flow:

1.User enters details via chat interface.

2.Python backend manages conversation flow using session_state.

3.Tech stack is sent to LLM.

4.LLM returns customized interview questions.

5.Questions are displayed to the user.

## ✍️ Prompt Design

The prompt design ensures structured and meaningful AI responses.

## 🎯 Goals of Prompt Design:

. Collect accurate candidate information.

. Generate domain-specific technical questions.

. Maintain professional recruiter tone.

## 🧩 Example Prompt Logic:

For tech stack input:

"Python, Machine Learning, SQL"

The prompt instructs the model to:

. Act as a technical interviewer.

. Generate concise, relevant interview questions.

. Focus on fundamentals and practical knowledge.

## 📌 Design Strategy:

. Separate prompts for:

   . Candidate information gathering

   . Technical question generation

. Avoid ambiguous instructions to maintain consistency.

. Ensure polite and professional chatbot tone.

## ⚠️ Challenges & Solutions

## 1️⃣ API Key Security

Problem:
Hardcoding the API key caused errors and security risks.

Solution:
Used environment variables and Streamlit Secrets to store the API key securely.

## 2️⃣ Session Handling in Streamlit

Problem:
Chat history was getting reset after each interaction.

Solution:
Implemented st.session_state to store:

. Chat history

. Candidate data

. Conversation stage

## 3️⃣ Input Field Behavior

Problem:
User input was persisting across messages and causing UI issues.

Solution:
Used controlled input handling with proper session management and reruns.

## 4️⃣ Dynamic Question Generation

Problem:
Single prompt was not handling multiple technologies effectively.

Solution:
Split tech stack input and generated questions per technology to improve relevance.

## 🌍 Deployment

The application can be deployed using Streamlit Cloud:

1.Push project to GitHub.

2.Connect GitHub repository to Streamlit Cloud.

3.Add GROQ_API_KEY in Streamlit Secrets.

4.Launch the app with a public URL.

✔ No server setup required
✔ Free hosting
✔ Ideal for internships and demos

## 📈 Future Enhancements

✅ Candidate answer evaluation and scoring

✅ Sentiment analysis of responses

✅ Recruiter dashboard

✅ PDF interview report generation

✅ Multi-language support

## 👩‍💻 Author

Sulekha Patel

B.Tech CSE (AI & ML) | Aspiring AI/ML Engineer & Full Stack Developer

LinkedIn: https://linkedin.com/in/sulekhapatel/

