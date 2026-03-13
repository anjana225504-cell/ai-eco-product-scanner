import streamlit as st
from openai import OpenAI

# Connect to OpenAI using Streamlit secrets
client = OpenAI(api_key=st.secrets["sk-...GSUA"])

st.title("🌱 AI Eco Product Scanner")

product = st.text_input("Enter a product name")

if st.button("Scan"):

    if product == "":
        st.write("Please enter a product name")
    else:
        prompt = f"Tell the environmental impact, recyclability, and eco-friendly suggestion for {product}."

        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt
        )

        st.subheader("Result")
        st.write(response.output_text)
