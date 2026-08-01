import streamlit as st
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.set_page_config(page_title="SnapSolve - Homework AI", layout="centered")
st.title("📸 SnapSolve")
st.write("Upload homework pic and I'll solve it with steps")

uploaded_file = st.file_uploader("Upload image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Your uploaded image", width='stretch')

    if st.button("Solve This"):
        with st.spinner("Thinking..."):
            model = genai.GenerativeModel('gemini-2.0-flash')
            #response = model.generate_content("Solve 2x+3=5 step by step")
            response = model.generate_content(
                ["Solve this homework problem. Show step by step solution.", image]
            )
            st.success("Answer:")
            st.write(response.text)