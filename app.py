import streamlit as st

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="COMMAND TERMINAL v2.0",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. THE TACTICAL THEME (CSS)
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #050505;
        color: #00FF41;
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* Header/Text Shadows */
    h1, h2, h3 {
        color: #00FF41 !important;
        text-shadow: 0px 0px 12px #00FF41;
        text-transform: uppercase;
        letter-spacing: 3px;
    }

    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: #000;
        padding: 10px;
    }

    .stTabs [data-baseweb="tab"] {
        height: 60px;
        background-color: #111;
        border: 1px solid #333;
        color: #888;
        padding: 0 20px;
    }

    .stTabs [data-baseweb="tab"]:hover {
        border: 1px solid #00FF41;
        color: #00FF41;
    }

    .stTabs [aria-selected="true"] {
        background-color: #001a00 !important;
        border: 1px solid #00FF41 !important;
        color: #00FF41 !important;
    }

    /* Input Boxes */
    input, div[data-baseweb="select"] > div, div[data-baseweb="input"] > div {
        background-color: #000 !important;
        color: #00FF41 !important;
        border: 1px solid #00FF41 !important;
        border-radius: 0px !important;
    }

    /* Buttons */
    .stButton>button {
        background-color: #00FF41 !important;
        color: black !important;
        font-weight: bold !important;
        border-radius: 0px !important;
        border: none !important;
        width: 100%;
        height: 3em;
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        background-color: #000 !important;
        color: #00FF41 !important;
        border: 1px solid #00FF41 !important;
        box-shadow: 0px 0px 20px #00FF41;
    }

    /* Success/Warning Messages */
    .stAlert {
        background-color: #000 !important;
        border: 1px solid #00FF41 !important;
        color: #00FF41 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. SECURITY CLEARANCE (LOGIN)
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    st.title("🔒 SYSTEM LOCK")
    password = st.text_input("ENTER ACCESS KEY:", type="password")
    if st.button("AUTHENTICATE"):
        if password == "BOSTON6": # You can change this password
            st.session_state['auth'] = True
            st.rerun()
        else:
            st.error("ACCESS DENIED: INVALID KEY")
else:
    # 4. MAIN TERMINAL CONTENT
    st.title("⚡ EXECUTIVE COMMAND TERMINAL")
    st.write(f"SYSTEM STATUS: **OPERATIONAL** | USER: **ADMIN**")
    st.write("---")

    tab1, tab2, tab3, tab4 = st.tabs([
        "📡 LOGISTICS", 
        "⚖️ ENFORCEMENT", 
        "🧠 INTELLIGENCE",
        "📂 ARCHIVES"
    ])

    with tab1:
        st.header("Logistics Hub")
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Session Control")
            game_mod = st.selectbox("Active Math Module", ["Blackjack", "Poker", "Liar's Dice", "Probability Drill"])
            status = st.radio("Terminal Status", ["Standby", "Live", "Maintenance"])
        with col2:
            st.subheader("Vault Management")
            bank = st.number_input("Current House Bankroll ($)", value=1000)
            if st.button("SYNC LOGISTICS DATA"):
                st.success(f"LOGISTICS UPDATED: {game_mod} is now {status.upper()}.")

    with tab2:
        st.header("Enforcement Ledger")
        st.subheader("Log Negative Delta")
        target = st.selectbox("Identify Lead", ["Roman", "Drayden", "Levi", "Connor", "Liam", "Boston"])
        penalty = st.number_input("Math Error Amount", min_value=0, step=5)
        reason = st.text_area("Violation Details")
        if st.button("EXECUTE PENALTY"):
            st.warning(f"DEBT LOGGED: {target} penalized {penalty} for {reason}")

    with tab3:
        st.header("Intelligence Feed")
        st.subheader("IQ Leaderboard")
        # Example data - later we connect this to your Sheet
        st.table({
            "Lead": ["Boston", "Connor", "Liam", "Roman", "Drayden", "Levi"],
            "IQ Rank": ["98%", "94%", "91%", "89%", "88%", "85%"],
            "Status": ["Clear", "Clear", "Watchlist", "Clear", "Clear", "Warning"]
        })

    with tab4:
        st.header("Archives")
        st.write("Historical session data and bankroll logs are stored here.")
        if st.button("LOGOUT"):
            st.session_state['auth'] = False
            st.rerun()
