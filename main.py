import streamlit as st
from groq import Groq

client = Groq(api_key="")

def calculate_bmi(weight, height):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 1)

def get_body_type(bmi):
    if bmi < 18.5:
        return "Underweight 😟"
    elif bmi < 25:
        return "Normal 💪"
    elif bmi < 30:
        return "Overweight ⚠️"
    else:
        return "Obese 🚨"

def get_bmi_color(bmi):
    if bmi < 18.5:
        return "#6366f1"
    elif bmi < 25:
        return "#a855f7"
    elif bmi < 30:
        return "#f59e0b"
    else:
        return "#ef4444"

def get_ai_plan(name, age, weight, height, bmi, body_type):
    prompt = f"""
    You are a professional Indian fitness coach and nutritionist.
    Create a personalized fitness plan for:
    Name: {name}
    Age: {age} years
    Weight: {weight} kg
    Height: {height} cm
    BMI: {bmi}
    Body Type: {body_type}

    IMPORTANT RULES:
    - Only suggest foods available in EVERY Indian household
    - Common foods only: roti, dal, rice, sabzi, dahi, eggs, milk, banana, peanuts, sprouts, poha, upma, besan, paneer
    - NO avocado, quinoa, greek yogurt, protein bars or expensive items
    - NO gym equipment for exercises — home workout only
    - Use simple Hindi food names where possible
    - Minimum emojis
    - Write in simple English

    Please give:
    1. DIET PLAN - Breakfast, Mid morning snack, Lunch, Evening snack, Dinner
    2. EXERCISE PLAN - Monday to Sunday with sets and reps
    3. TOP 5 HEALTH TIPS - Simple and practical for Indian lifestyle
    """
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


st.set_page_config(page_title="AI Fitness Planner", page_icon="🏋️", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,400&display=swap');

/* ── GLOBAL RESET ── */
html, body, .stApp, .stApp > div,
[data-testid="stAppViewContainer"],
[data-testid="stAppViewBlockContainer"],
[data-testid="stVerticalBlock"],
[data-testid="stBottom"],
[data-testid="stBottom"] > div,
[data-testid="stBottom"] > div > div,
.main, .block-container {
    background-color: #0d0d1a !important;
    color: #f0eeff !important;
}
.stApp { font-family: 'DM Sans', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 0; padding-bottom: 6rem; max-width: 780px; }

/* ── ANIMATED HERO BACKGROUND ── */
.hero-section {
    background: linear-gradient(135deg, #1a0533 0%, #0d0d1a 40%, #1a0a2e 100%);
    border-bottom: 1px solid rgba(168,85,247,0.2);
    padding: 3.5rem 2rem 3rem;
    text-align: center;
    margin: -1rem -1rem 2rem -1rem;
    position: relative;
    overflow: hidden;
}
.hero-section::before {
    content: '';
    position: absolute;
    top: -60%; left: 50%;
    transform: translateX(-50%);
    width: 600px; height: 400px;
    background: radial-gradient(ellipse, rgba(168,85,247,0.2) 0%, transparent 70%);
    pointer-events: none;
}
.hero-section::after {
    content: '';
    position: absolute;
    bottom: -2px; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, #a855f7, #ec4899, #a855f7, transparent);
}

.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(168,85,247,0.15);
    border: 1px solid rgba(168,85,247,0.3);
    color: #d8b4fe;
    font-size: 0.7rem; font-weight: 700;
    letter-spacing: 0.18em; text-transform: uppercase;
    padding: 6px 16px; border-radius: 100px;
    margin-bottom: 1.5rem;
}
.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2.8rem, 7vw, 4.2rem);
    font-weight: 800; line-height: 1;
    letter-spacing: -0.04em;
    color: #ffffff;
    margin: 0 0 1rem;
    text-shadow: 0 0 60px rgba(168,85,247,0.3);
}
.hero-title .accent {
    background: linear-gradient(135deg, #a855f7 0%, #ec4899 50%, #f472b6 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-sub {
    font-size: 1rem; color: #a78bca;
    font-weight: 400; margin: 0;
    letter-spacing: 0.01em;
}

/* ── SECTION LABEL ── */
.section-label {
    font-size: 0.68rem; font-weight: 800;
    letter-spacing: 0.18em; text-transform: uppercase;
    color: #7c3aed; margin-bottom: 1.2rem; margin-top: 0.5rem;
    display: flex; align-items: center; gap: 8px;
}
.section-label::after {
    content: '';
    flex: 1; height: 1px;
    background: linear-gradient(90deg, rgba(124,58,237,0.3), transparent);
}

/* ── INPUTS ── */
.stTextInput > div > div > input,
.stNumberInput > div > div > input {
    background: #1a0a2e !important;
    border: 1.5px solid rgba(168,85,247,0.3) !important;
    border-radius: 12px !important;
    color: #f0eeff !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.95rem !important;
    padding: 12px 16px !important;
    transition: all 0.2s !important;
    -webkit-text-fill-color: #f0eeff !important;
    box-shadow: inset 0 0 0 9999px #1a0a2e !important;
}
/* FIX: browser autofill white background */
.stTextInput > div > div > input:-webkit-autofill,
.stTextInput > div > div > input:-webkit-autofill:hover,
.stTextInput > div > div > input:-webkit-autofill:focus,
.stNumberInput > div > div > input:-webkit-autofill,
.stNumberInput > div > div > input:-webkit-autofill:hover,
.stNumberInput > div > div > input:-webkit-autofill:focus {
    -webkit-box-shadow: 0 0 0px 1000px #1a0a2e inset !important;
    -webkit-text-fill-color: #f0eeff !important;
    border-color: rgba(168,85,247,0.3) !important;
    caret-color: #f0eeff !important;
}
.stTextInput > div > div > input::placeholder {
    color: #4a3570 !important;
}
.stTextInput > div > div > input:focus,
.stNumberInput > div > div > input:focus {
    background: rgba(168,85,247,0.1) !important;
    border-color: #a855f7 !important;
    box-shadow: 0 0 0 4px rgba(168,85,247,0.12), 0 0 20px rgba(168,85,247,0.1) !important;
}
.stTextInput label, .stNumberInput label {
    color: #9d7ec9 !important;
    font-size: 0.8rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.04em !important;
    text-transform: uppercase !important;
    font-family: 'DM Sans', sans-serif !important;
}
.stNumberInput button {
    background: rgba(168,85,247,0.1) !important;
    border: 1px solid rgba(168,85,247,0.2) !important;
    color: #c084fc !important;
    border-radius: 8px !important;
    transition: all 0.15s !important;
}
.stNumberInput button:hover {
    background: rgba(168,85,247,0.25) !important;
    border-color: #a855f7 !important;
    color: #e9d5ff !important;
}

/* ── CTA BUTTON ── */
.stButton > button {
    background: linear-gradient(135deg, #9333ea 0%, #ec4899 100%) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 14px !important;
    padding: 16px 32px !important;
    font-size: 1.05rem !important;
    font-weight: 700 !important;
    font-family: 'Syne', sans-serif !important;
    letter-spacing: 0.02em !important;
    transition: all 0.3s !important;
    box-shadow: 0 4px 20px rgba(147,51,234,0.4), 0 0 40px rgba(236,72,153,0.15) !important;
    position: relative !important;
}
.stButton > button:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 8px 32px rgba(147,51,234,0.55), 0 0 60px rgba(236,72,153,0.25) !important;
}
.stButton > button:active {
    transform: translateY(-1px) !important;
}

/* ── STAT CARDS ── */
.stats-row {
    display: grid; grid-template-columns: 1fr 1fr;
    gap: 1rem; margin: 1.5rem 0;
}
.stat-card {
    background: linear-gradient(135deg, rgba(147,51,234,0.12) 0%, rgba(236,72,153,0.06) 100%);
    border: 1px solid rgba(168,85,247,0.25);
    border-radius: 18px; padding: 1.6rem 1.8rem;
    position: relative; overflow: hidden;
    box-shadow: 0 4px 24px rgba(147,51,234,0.1), inset 0 1px 0 rgba(255,255,255,0.05);
}
.stat-card::before {
    content: ''; position: absolute;
    top: 0; left: 0; right: 0; height: 2px;
    background: linear-gradient(90deg, #9333ea, #ec4899);
}
.stat-card::after {
    content: '';
    position: absolute;
    top: -40px; right: -40px;
    width: 120px; height: 120px;
    background: radial-gradient(circle, rgba(168,85,247,0.1) 0%, transparent 70%);
    pointer-events: none;
}
.stat-label {
    font-size: 0.65rem; font-weight: 800;
    letter-spacing: 0.15em; text-transform: uppercase;
    color: #7c3aed; margin-bottom: 0.6rem;
}
.stat-value {
    font-family: 'Syne', sans-serif;
    font-size: 2.2rem; font-weight: 800;
    line-height: 1; margin-bottom: 0.3rem;
}
.stat-sub { font-size: 0.78rem; color: #6b4fa0; }

/* ── SUCCESS BANNER ── */
.success-banner {
    background: linear-gradient(135deg, rgba(147,51,234,0.12), rgba(236,72,153,0.08));
    border: 1px solid rgba(168,85,247,0.3);
    border-radius: 12px; padding: 14px 18px;
    color: #d8b4fe; font-size: 0.9rem;
    font-weight: 600; margin: 1rem 0;
    display: flex; align-items: center; gap: 10px;
    box-shadow: 0 2px 12px rgba(147,51,234,0.1);
}

/* ── PLAN CARD ── */
.plan-card {
    background: linear-gradient(135deg, rgba(147,51,234,0.07) 0%, rgba(13,13,26,0.8) 100%);
    border: 1px solid rgba(168,85,247,0.18);
    border-radius: 18px; padding: 2rem 2.2rem;
    margin: 1rem 0; line-height: 1.8;
    color: #c4b5d4; font-size: 0.92rem;
    box-shadow: 0 4px 24px rgba(147,51,234,0.08);
}

/* ── CHAT HEADER ── */
.chat-header {
    font-family: 'Syne', sans-serif;
    font-size: 1.15rem; font-weight: 800;
    color: #f0eeff; margin: 2rem 0 1rem;
    display: flex; align-items: center; gap: 10px;
}

/* ── CHAT MESSAGES ── */
.stChatMessage {
    background: rgba(147,51,234,0.07) !important;
    border: 1px solid rgba(168,85,247,0.15) !important;
    border-radius: 14px !important;
    margin-bottom: 0.6rem !important;
    box-shadow: 0 2px 8px rgba(147,51,234,0.06) !important;
}
[data-testid="stChatMessageContent"] p {
    color: #c4b5d4 !important;
    font-size: 0.93rem !important;
}

/* ── CHAT INPUT ── */
[data-testid="stBottom"],
[data-testid="stBottom"] > div,
[data-testid="stBottom"] > div > div {
    background-color: #0d0d1a !important;
    border-top: 1px solid rgba(168,85,247,0.15) !important;
}
.stChatInput > div {
    background: rgba(147,51,234,0.08) !important;
    border: 1.5px solid rgba(168,85,247,0.25) !important;
    border-radius: 14px !important;
    box-shadow: 0 2px 12px rgba(147,51,234,0.1) !important;
}
.stChatInput textarea {
    background: #0d0d1a !important;
    color: #f0eeff !important;
    -webkit-text-fill-color: #f0eeff !important;
    font-family: 'DM Sans', sans-serif !important;
    caret-color: #a855f7 !important;
}
.stChatInput textarea::placeholder { color: #4a3570 !important; }
.stChatInput > div > div {
    background: #0d0d1a !important;
}
.stChatInput > div:focus-within {
    border-color: #a855f7 !important;
    box-shadow: 0 0 0 3px rgba(168,85,247,0.12) !important;
}
.stChatInput button {
    background: linear-gradient(135deg, #9333ea, #ec4899) !important;
    border-radius: 10px !important; border: none !important;
}

/* ── MISC ── */
.stSpinner > div { border-top-color: #a855f7 !important; }
hr { border-color: rgba(168,85,247,0.12) !important; margin: 2rem 0 !important; }
.stAlert { border-radius: 12px !important; font-size: 0.88rem !important; }
[data-testid="stMetric"] { display: none !important; }

</style>
""", unsafe_allow_html=True)


# ── HERO ─────────────────────────────────────────────
st.markdown("""
<div class="hero-section">
    <div class="hero-badge">🇮🇳 Made for India</div>
    <h1 class="hero-title">AI <span class="accent">Fitness</span> Planner</h1>
    <p class="hero-sub">Your personalised Indian diet & workout plan — powered by AI</p>
</div>
""", unsafe_allow_html=True)

# ── INPUTS ───────────────────────────────────────────
st.markdown('<p class="section-label">Your Details</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    name   = st.text_input("Your Name", placeholder="e.g. Rahul Sharma")
    weight = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0, value=60.0, step=0.5)
with col2:
    age    = st.number_input("Age", min_value=10, max_value=100, value=20)
    height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0, value=170.0, step=0.5)

st.markdown('<br>', unsafe_allow_html=True)

if st.button("✨ Get My AI Fitness Plan", use_container_width=True):
    if name.strip() == "":
        st.error("Please enter your name to continue.")
    else:
        bmi       = calculate_bmi(weight, height)
        body_type = get_body_type(bmi)
        with st.spinner("Generating your personalised plan..."):
            plan = get_ai_plan(name, age, weight, height, bmi, body_type)
        st.session_state.plan      = plan
        st.session_state.bmi       = bmi
        st.session_state.body_type = body_type
        st.session_state.messages  = []

# ── RESULTS ──────────────────────────────────────────
if "plan" in st.session_state:
    bmi       = st.session_state.bmi
    body_type = st.session_state.body_type
    bmi_color = get_bmi_color(bmi)

    st.markdown(f"""
    <div class="stats-row">
        <div class="stat-card">
            <div class="stat-label">Your BMI</div>
            <div class="stat-value" style="color:{bmi_color}">{bmi}</div>
            <div class="stat-sub">Body Mass Index</div>
        </div>
        <div class="stat-card">
            <div class="stat-label">Body Type</div>
            <div class="stat-value" style="font-size:1.5rem;color:#f0eeff">{body_type}</div>
            <div class="stat-sub">Based on your BMI</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="success-banner">✅ Your personalised fitness plan is ready!</div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="plan-card">
        {st.session_state.plan.replace(chr(10), '<br>')}
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<hr>', unsafe_allow_html=True)

    # ── CHAT ─────────────────────────────────────────
    st.markdown('<div class="chat-header">💬 Chat with your AI Coach</div>', unsafe_allow_html=True)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_question = st.chat_input("Ask your AI coach anything...")

    if user_question:
        with st.chat_message("user"):
            st.markdown(user_question)
        st.session_state.messages.append({"role": "user", "content": user_question})

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "user",      "content": "Generate a fitness plan"},
                        {"role": "assistant", "content": st.session_state.plan},
                    ] + st.session_state.messages
                )
                answer = response.choices[0].message.content
                st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})

st.markdown('<hr>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center;color:#3b2c5a;font-size:0.78rem;font-family:DM Sans,sans-serif;">Built with Python · Groq · Streamlit</p>', unsafe_allow_html=True)