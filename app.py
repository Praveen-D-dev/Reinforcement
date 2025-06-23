# app.py 🧠 - Unified RL Dashboard Launcher

import streamlit as st

# Title
st.set_page_config(page_title="RL Dashboard", layout="wide")
st.title("🧠 Reinforcement Learning Dashboard")

# Sidebar Menu
menu = st.sidebar.selectbox(
    "📂 Select a Project",
    (
        "Home",
        "Q-Learning - Teach",
        "Q-Learning - My Model",
        "SARSA - Teach",
        "SARSA - My Model",
        "REINFORCE - Teach",
        "REINFORCE - My Model",
        "Other Projects (Coming Soon)"
    )
)

# Home Page
if menu == "Home":
    st.subheader("📘 Welcome, My Lord 👑")
    st.write("""
    This dashboard contains all your Reinforcement Learning projects with separate pages for:
    - 📚 Teaching the concept
    - 🧪 Training your own models
    """)
    st.info("Use the left sidebar to explore your projects.")

# Routing to project pages
elif menu == "Q-Learning - Teach":
    try:
        import qlearning_teach
        qlearning_teach.run()
    except:
        st.warning("🚧 This page is under construction.")

elif menu == "Q-Learning - My Model":
    try:
        import qlearning_mymodel
        qlearning_mymodel.run()
    except:
        st.warning("🚧 This page is under construction.")

elif "Teach" in menu or "My Model" in menu:
    st.warning("🚧 This section is not yet implemented.")
