import os
import streamlit as st
import gdown

MODEL_FILE = "best_model_params.pt"
FILE_ID = "1hSoHBeV7FSAsYNzT2Q2ixCGaN3pFIC8m"

if not os.path.exists(MODEL_FILE):
    with st.spinner("Downloading model weights..."):
        gdown.download(
            f"https://drive.google.com/uc?id={FILE_ID}",
            MODEL_FILE,
            quiet=False
        )

from inference import generate_text

st.set_page_config(
    page_title="TinyStories GPT",
    page_icon="🤖"
)

st.title("🤖 TinyStories GPT")

prompt = st.text_area(
    "Enter Prompt",
    value="Once upon a time",
    height=150
)

temperature = st.slider(
    "Temperature",
    0.1,
    2.0,
    0.8
)

max_tokens = st.slider(
    "Max New Tokens",
    10,
    300,
    100
)

if st.button("Generate"):

    with st.spinner("Generating..."):

        output = generate_text(
            prompt=prompt,
            max_new_tokens=max_tokens,
            temperature=temperature
        )

    st.subheader("Output")
    st.write(output)