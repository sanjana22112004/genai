import streamlit as st
import openai
import os

# Get OpenAI API key from environment variable
openai.api_key = os.getenv("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")

st.title("Text to Image Generator - Colab + Streamlit")

prompt = st.text_input("Enter your image description:")

if st.button("Generate Image"):
    if prompt:
        with st.spinner("Generating image..."):
            response = openai.Image.create(
                prompt=prompt,
                n=1,
                size="512x512"
            )
            image_url = response['data'][0]['url']
            st.image(image_url, caption=prompt)
    else:
        st.warning("Please enter a text prompt.")
