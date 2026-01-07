import streamlit as st
from llm import generate_questions
from utils import is_exit_command, validate_email, validate_phone
from prompts import GREETING_MESSAGE, END_MESSAGE, FALLBACK_MESSAGE

# -------------------- Page Config --------------------
st.set_page_config(page_title="TalentScout Hiring Assistant", layout="centered")

st.markdown('<div class="title">🤖 TalentScout Hiring Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">An AI-powered chatbot for initial candidate screening</div>', unsafe_allow_html=True)

# -------------------- Custom CSS for Dark Theme & Chat Bubbles --------------------
st.markdown("""
<style>
    body {
        background-color: #0e1117;
        color: #ffffff;
    }

    .stApp {
        background: linear-gradient(180deg, #0e1117 0%, #0b0f14 100%);
    }

    .chat-container {
        max-width: 900px;
        margin: auto;
        padding: 10px;
    }

    .chat-bubble {
        padding: 12px 16px;
        border-radius: 18px;
        margin: 8px 0;
        max-width: 70%;
        line-height: 1.5;
        font-size: 15px;
    }

    .bot {
        background: #1f2937;
        color: #ffffff;
        border-top-left-radius: 4px;
        text-align: left;
    }

    .user {
        background: #2563eb;
        color: #ffffff;
        border-top-right-radius: 4px;
        margin-left: auto;
        text-align: right;
    }

    .title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 16px;
        color: #9ca3af;
        margin-bottom: 25px;
    }

    .input-box {
        margin-top: 20px;
    }

    button[kind="primary"] {
        background-color: #2563eb !important;
        border-radius: 8px !important;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)


# -------------------- Session State --------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "candidate_data" not in st.session_state:
    st.session_state.candidate_data = {}

if "stage" not in st.session_state:
    st.session_state.stage = "greeting"
    
# -------------------- Auto Greeting on First Load --------------------
if st.session_state.stage == "greeting" and len(st.session_state.chat_history) == 0:
    st.session_state.chat_history.append(("bot", GREETING_MESSAGE))
    st.session_state.chat_history.append(("bot", "May I know your **Full Name**?"))
    st.session_state.stage = "name"


# -------------------- Display Chat --------------------
def display_chat():
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)

    for role, message in st.session_state.chat_history:
        if role == "bot":
            st.markdown(
                f'<div class="chat-bubble bot">🤖 <b>TalentScout:</b><br>{message}</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f'<div class="chat-bubble user">👤 <b>You:</b><br>{message}</div>',
                unsafe_allow_html=True
            )

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------- Bot Response Logic --------------------
def bot_response(user_input):
    # Exit condition
    if is_exit_command(user_input):
        st.session_state.chat_history.append(("bot", END_MESSAGE))
        st.session_state.stage = "ended"
        return

    stage = st.session_state.stage

    # ---------- GREETING ----------
    if stage == "greeting":
        st.session_state.chat_history.append(("bot", GREETING_MESSAGE))
        st.session_state.chat_history.append(("bot", "May I know your **Full Name**?"))
        st.session_state.stage = "name"

    # ---------- NAME ----------
    elif stage == "name":
        st.session_state.candidate_data["name"] = user_input
        st.session_state.chat_history.append(("bot", "Please provide your **Email Address**."))
        st.session_state.stage = "email"

    # ---------- EMAIL ----------
    elif stage == "email":
        if not validate_email(user_input):
            st.session_state.chat_history.append(("bot", "That doesn't look like a valid email. Please enter a valid email address."))
            return
        st.session_state.candidate_data["email"] = user_input
        st.session_state.chat_history.append(("bot", "Please provide your **Phone Number**."))
        st.session_state.stage = "phone"

    # ---------- PHONE ----------
    elif stage == "phone":
        if not validate_phone(user_input):
            st.session_state.chat_history.append(("bot", "That doesn't look like a valid phone number. Please enter a valid number."))
            return
        st.session_state.candidate_data["phone"] = user_input
        st.session_state.chat_history.append(("bot", "How many **years of experience** do you have?"))
        st.session_state.stage = "experience"

    # ---------- EXPERIENCE ----------
    elif stage == "experience":
        st.session_state.candidate_data["experience"] = user_input
        st.session_state.chat_history.append(("bot", "What **position(s)** are you applying for?"))
        st.session_state.stage = "position"

    # ---------- POSITION ----------
    elif stage == "position":
        st.session_state.candidate_data["position"] = user_input
        st.session_state.chat_history.append(("bot", "What is your **current location**?"))
        st.session_state.stage = "location"

    # ---------- LOCATION ----------
    elif stage == "location":
        st.session_state.candidate_data["location"] = user_input
        st.session_state.chat_history.append(("bot", "Please list your **tech stack** (e.g., Python, Django, MySQL, Git)."))
        st.session_state.stage = "tech_stack"

    # ---------- TECH STACK ----------
    elif stage == "tech_stack":
        st.session_state.candidate_data["tech_stack"] = user_input
        st.session_state.chat_history.append(("bot", "Thank you! Based on your tech stack, here are some technical questions:"))

        # Split tech stack by commas
        tech_list = [tech.strip() for tech in user_input.split(",") if tech.strip()]

        for tech in tech_list:
            st.session_state.chat_history.append(("bot", f"📌 **{tech.upper()} Questions:**"))
            questions = generate_questions(tech)
            for q in questions:
                st.session_state.chat_history.append(("bot", q))

        st.session_state.chat_history.append(("bot", END_MESSAGE))
        st.session_state.stage = "ended"


    # ---------- FALLBACK ----------
    else:
        st.session_state.chat_history.append(("bot", FALLBACK_MESSAGE))

# -------------------- UI Input --------------------
display_chat()

if st.session_state.stage == "ended":
    st.text_input(
        "Conversation completed.",
        value="Thank you for your time!",
        disabled=True
    )
else:
    with st.form(key="chat_form", clear_on_submit=True):
        st.markdown('<div class="input-box">', unsafe_allow_html=True)

        user_input = st.text_input(
            "Type your response here...",
            key="user_input",
            label_visibility="collapsed"
        )
        send = st.form_submit_button("Send")

        st.markdown('</div>', unsafe_allow_html=True)

        if send:
            if user_input.strip() == "":
                st.warning("Please enter a message.")
            else:
                st.session_state.chat_history.append(("user", user_input))
                bot_response(user_input)
                st.rerun()
