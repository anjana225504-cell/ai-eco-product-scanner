import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

st.title("🌱 AI Eco Product Scanner")

product = st.text_input("Enter a product name")

if st.button("Analyze"):
    if product:
        prompt = f"""
        Analyze the environmental impact of this product: {product}.
        Give:
        1. Material type
        2. Recyclability
        3. Environmental impact
        4. Eco-friendly suggestion
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        result = response.choices[0].message.content
        st.write(result)
