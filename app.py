import streamlit as st
import requests
from PIL import Image
import io

st.set_page_config(
    page_title="Crisis Spiders",
    layout="wide"
)

st.sidebar.title("🕷️ Crisis Spiders")
page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Team"]
)

if page == "Dashboard":
    SERVER_URL = "http://SERVER_IP:8000"  
    robots = ["geopider", "neopider", "spydex"]

    st.title("🕷️ Crisis Spiders Control Center")
    st.subheader("Smart Robotic Swarm & Digital Twin System")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Active Robots", "3")
        st.metric("System Status", "Online")

    with col2:
        st.metric("AI Models Running", "2")
        st.metric("Detected Anomalies", "0")

    with col3:
        st.metric("Digital Twin", "Live")
        st.metric("Connection", "Stable")

    st.divider()
    st.subheader("📡 Live Monitoring")
    cols = st.columns(3)

    for col, robot in zip(cols, robots):
        with col:
            st.markdown(f"### 🤖 {robot.upper()}")
            try:
                response = requests.get(f"{SERVER_URL}/frame/{robot}", timeout=1)
                if response.content:
                    image = Image.open(io.BytesIO(response.content))
                    st.image(image, use_column_width=True)
                else:
                    st.warning("No data received yet")
            except:
                st.error("Robot Offline")

    st.metric("Cracks", "Not Detected")
    st.metric("Mineral", "Unknown")
    st.divider()
    st.subheader("🌍 Digital Twin (Live Map)")
    twin_data = {
        "lat": [21.3891, 21.3895, 21.3899],
        "lon": [39.8579, 39.8583, 39.8587]
    }
    st.map(twin_data)

elif page == "Team":
    st.title("👥 Crisis Spiders Team")

    team = [
        ("منار محمد الطويرقي", "s44208057@students.tu.edu.sa", "mnaraltwairgei@gmail.com"),
        ("جنى محمد السفياني", "s44251378@students.tu.edu.sa", "engjanals@gmail.com"),
        ("ابرار محمد البقمي", "s44204498@students.tu.edu.sa", "Abrar54132@outlook.sa"),
        ("شيهانه سليمان الجعيد", "s44201849@students.tu.edu.sa", "Shehana2255@gmail.com"),
        ("سميه عبدالله المالكي", "s44201735@students.tu.edu.sa", "sumayah.a.almalki@gmail.com"),
        ("هدى محمد البقمي", "s44200812@students.tu.edu.sa", "hudalbaqami@gmail.com"),
        ("دارين عالي الغامدي", "s44204996@students.tu.edu.sa", "dareen1aali@outlook.com"),
        ("وسن فايز الثبيتي", "s44201077@students.tu.edu.sa", "wasan14242@gmail.com"),
    ]

    for name, uni_email, personal_email in team:
        st.subheader(name)
        st.write(f"📧 University Email: {uni_email}")
        st.write(f"📧 Personal Email: {personal_email}")
        st.divider()