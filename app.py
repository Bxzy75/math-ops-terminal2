import streamlit as st

# Setup the Page
st.set_page_config(page_title="Math Ops Terminal", layout="wide")

# Terminal Styling
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #00ff00; }
    h1, h2, h3 { color: #00ff00 !important; font-family: 'Courier New', monospace; }
    .stButton>button { background-color: #262730; color: #00ff00; border: 1px solid #00ff00; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ STRATEGIC MATH OPERATIONS: TERMINAL")

# Navigation Tabs
tab1, tab2, tab3 = st.tabs(["Logistics", "Enforcement", "Intelligence"])

with tab1:
    st.header("Logistics Hub (Roman & Drayden)")
    col1, col2 = st.columns(2)
    with col1:
        game = st.selectbox("Current Module", ["Blackjack", "Poker", "Liar's Dice"])
    with col2:
        bank = st.number_input("Vault Balance ($)", value=1000)
    if st.button("Sync Logistics"):
        st.success(f"Logistics Updated: {game} Active.")

with tab2:
    st.header("Enforcement Ledger (Levi)")
    target = st.selectbox("Select Lead", ["Roman", "Drayden", "Levi", "Connor", "Liam", "Boston"])
    penalty = st.number_input("Math Error Penalty", min_value=0)
    reason = st.text_input("Violation Description")
    if st.button("Log Violation"):
        st.warning(f"Penalty logged against {target}")

with tab3:
    st.header("Intelligence Feed (Connor & Liam)")
    st.write("Live Leaderboard and Security Logs Standby...")
