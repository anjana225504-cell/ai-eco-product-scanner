import streamlit as st
import openai

# Load API key from Streamlit secrets
openai.api_key = st.secrets["openai"]["api_key"]

st.title("🌱 AI Eco Product Scanner")
st.write("Type a product name and get its environmental impact and suggestions!")

# User input
product = st.text_input("Enter a product name:")

if st.button("Analyze"):
    if product:
        # Prepare AI prompt
        prompt = f"""
        Analyze the environmental impact of this product: {product}.
        Give:
        1. Material type
        2. Recyclability
        3. Environmental impact
        4. Eco-friendly suggestion
        """

        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        # Extract AI answer
        result = response['choices'][0]['message']['content']
        st.success("AI Analysis:")
        st.write(result)
