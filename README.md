# eid-wish
import streamlit as st
import time

# Page configuration
st.set_page_config(page_title="Eid al-Kabir Greeting", page_icon="🌙", layout="centered")

st.title("🎉 Eid al-Kabir Greeting Generator 🎉")

# Step 1 – User input
name = st.text_input("Enter your name to begin:")

if name:
    st.markdown("---")
    
    # Step 2 – Animation and personalized bold message
    with st.spinner("Summoning moon and stars..."):
        time.sleep(2)

    # Display a moon and star animation (via hosted GIF)
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNG1wcTdud3RxejB1YTh4MGJjcTZhZXh5NmZwdWtrMXN1Y3FyNTR5ZCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/r5gG4Ct3xmwZy/giphy.gif", use_column_width=True)

    # Bold message below the animation
    st.markdown(
        f"<h3 style='text-align: center; font-weight: bold; margin-top: 10px;'>{name.upper()} IS WISHING YOU EID MUBARAK</h3>",
        unsafe_allow_html=True
    )

    # Small pause before final step
    time.sleep(2)

    # Step 3 – Final greeting
    st.markdown("---")
    st.success(f"""
    🎊 **Eid Mubarak, {name}!** 🎊  
    May this Eid al-Kabir bring peace, blessings,  
    and joy to you and your loved ones.  
    🐑 *Taqabbal Allahu minna wa minkum!* 🐑  
    """)
