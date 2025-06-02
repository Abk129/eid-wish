import streamlit as st

st.set_page_config(page_title="Eid al-Kabir Greeting", page_icon="🐑")

st.title("🎉 Eid al-Kabir Greeting Generator 🎉")

name = st.text_input("Enter your name:")

if name:
    st.markdown("---")
    st.success(f"""🎊 **Eid Mubarak, {name}!** 🎊  
May this Eid al-Kabir bring peace, blessings,  
and joy to you and your loved ones.  
🐑 *Taqabbal Allahu minna wa minkum!* 🐑  
""")
