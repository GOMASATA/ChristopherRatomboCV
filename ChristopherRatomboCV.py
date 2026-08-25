import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Christopher Ratombo - Web CV", page_icon="💼", layout="wide")

# --- HEADER ---
    st.title("Christopher Ratombo")
    st.write("📧 abazingeli8012@gmail.com | 📱 081 578 1035 | 📍 Tembisa, Gauteng")
    st.markdown("**Customer Service & Technical Support Specialist | AI & Financial Markets Analyst**")

# --- PROFESSIONAL SUMMARY ---
st.subheader("Professional Summarsy")
st.write("""
Customer service and technical support specialist with 15+ years of experience across telecommunications, financial services, and retail. 
Proven track record in problem-solving, upselling, and workflow optimization. 
Currently expanding expertise in artificial intelligence and financial market analysis, combining technical knowledge with entrepreneurial drive.
""")

# --- PROJECTS ---
st.subheader("Latest Projects")
st.markdown("- [Knowledge Retrieval Bot](https://rrjubdr4qpktmqtnvpq4we.streamlit.app)")
st.markdown("- [Survey Bot](https://survey-bot-je4ximyl6ceran4chd2tda.streamlit.app)")
st.markdown("- AI-Powered Market Monitoring Bot (Python-based trading assistant with real-time alerts)")

# --- CORE SKILLS ---
st.subheader("Core Skills")
skills = {
    "Technical": ["Microsoft Excel", "Computer Programming", "Technical Support"],
    "Business": ["Problem Solving", "Planning", "Basic Accounting", "Sales"],
    "Customer Service": ["Communication", "Upselling", "Reservations", "Client Relations", "Customer Retention"]
}
for category, items in skills.items():
    st.markdown(f"**{category}:** " + ", ".join(items))

# --- EXPERIENCE ---
st.subheader("Work Experience")
st.write("""
**Independent Consultant – AI & Financial Markets Analysis (2018 – Present)**  
- Developing trading strategies and automation tools for financial markets.  
- Studying AI applications in business and analytics.  
- Managing entrepreneurial projects with focus on innovation and scalability.  

**PHILIPS – Contact Centre Coordinator (2013 – 2017)**  
- Delivered technical support and resolved finance queries.  
- Scheduled engineers efficiently, reducing service delays.  
- Improved customer satisfaction through proactive service delivery.  

**TOP TV / STARSAT – Technical Call Centre Agent (2011 – 2013)**  
- Handled customer queries, account issues, and technical support.  
- Consistently exceeded upselling targets.  
""")

# --- EDUCATION ---
st.subheader("Education & Certifications")
st.write("""
- National Senior Certificate  
- Diploma In Travel And Tourism  
- Proactive Communications, English For Business Communications  
- Practical Spreadsheet Processing, Voyager Ticketing (S.A.A)  
- Passenger Handling (S.A.A), HTML, CSS  
- Security Grade E,D,C
""")

# --- FOOTER ---
st.markdown("---")
st.write("References available upon request.")
