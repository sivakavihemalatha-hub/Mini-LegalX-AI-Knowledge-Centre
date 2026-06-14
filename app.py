import streamlit as st
from legalx_ai import ask_legalx
from legalx_chat import ask_question
from audio_utils import generate_audio

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Mini LegalX AI Knowledge Centre",
    page_icon="⚖️",
    layout="wide"
)

# =========================
# DATA
# =========================
ACT_LIST = [
    "POCSO Act",
    "Consumer Protection Act",
    "Cyber Crime Laws",
    "Right to Information Act",
    "GST Registration"
]

CARD_DESCRIPTIONS = {
    "POCSO Act": "Protection of Children from Sexual Offences Act",
    "Consumer Protection Act": "Protects consumers from unfair trade practices",
    "Cyber Crime Laws": "Laws against online fraud and hacking",
    "Right to Information Act": "Right to access government information",
    "GST Registration": "Tax registration system under GST"
}

# =========================
# SESSION STATE FIX
# =========================
if "selected_act" not in st.session_state:
    st.session_state.selected_act = None

if "report" not in st.session_state:
    st.session_state.report = None

if "audio_file" not in st.session_state:
    st.session_state.audio_file = None

if "answer" not in st.session_state:
    st.session_state.answer = None

# =========================
# TITLE
# =========================
st.markdown(
    "<h1 style='text-align:center; font-weight:bold; color:#1f77b4;'>⚖️ Mini LegalX AI Knowledge Centre</h1>",
    unsafe_allow_html=True
)

st.write("Explore legal topics in simple structured format")

st.divider()

# =========================
# CARDS
# =========================
st.markdown("<h2 style='font-weight:bold;'>📚 Legal Topics</h2>", unsafe_allow_html=True)

cols = st.columns(3)

for i, act in enumerate(ACT_LIST):

    with cols[i % 3]:

        st.markdown(
            f"<h3 style='color:#1f77b4; font-weight:bold;'>⚖️ {act}</h3>",
            unsafe_allow_html=True
        )

        st.markdown(
            f"<p style='font-size:14px;'>• {CARD_DESCRIPTIONS[act]}</p>",
            unsafe_allow_html=True
        )

        if st.button("📖 Read More", key=act):

            st.session_state.selected_act = act
            st.session_state.report = None
            st.session_state.audio_file = None
            st.session_state.answer = None

            # AUTO GENERATE SUMMARY
            with st.spinner("Generating summary..."):
                st.session_state.report = ask_legalx(f"What is {act}?")

st.divider()

# =========================
# DETAIL VIEW
# =========================
if st.session_state.selected_act:

    act = st.session_state.selected_act

    st.markdown(
        f"<h2 style='font-weight:bold;'>📖 {act}</h2>",
        unsafe_allow_html=True
    )

    # =========================
    # SUMMARY DISPLAY
    # =========================
    if st.session_state.report:

        st.markdown("<h3 style='font-weight:bold;'>📄 Summary</h3>", unsafe_allow_html=True)

        for line in st.session_state.report.split("\n"):

            line = line.strip()

            if not line:
                continue

            if line.endswith(":"):
                st.markdown(f"## **{line}**")
            else:
                st.write(line)

        # =========================
        # AUDIO FIX (SESSION SAFE)
        # =========================
        if st.button("🔊 Play Audio"):

            st.session_state.audio_file = generate_audio(CARD_DESCRIPTIONS[act])

        if st.session_state.audio_file:
            st.audio(st.session_state.audio_file)

    # =========================
    # CHAT FIX (SESSION SAFE)
    # =========================
    st.divider()

    st.markdown("<h3 style='font-weight:bold;'>💬 Ask Questions</h3>", unsafe_allow_html=True)

    user_question = st.text_input("Ask anything about this law", key="chat_input")

    if st.button("Ask") and user_question:

        st.session_state.answer = ask_question(user_question)

    if st.session_state.answer:

        st.markdown("### Answer")
        st.write(st.session_state.answer)
