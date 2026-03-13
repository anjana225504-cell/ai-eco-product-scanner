import streamlit as st

st.title("🌱 AI Eco Product Scanner")
st.write("Type a product name and get its environmental impact and suggestions!")

# Input box for user
product = st.text_input("Enter a product name:")

# Button to run analysis
if st.button("Analyze"):
    if product:
        # For now, a simple placeholder response
        st.success(f"Analyzing: {product}")
        st.write("Material: Plastic (example)")
        st.write("Recyclable: Yes (example)")
        st.write("Suggestion: Use reusable alternatives (example)")
