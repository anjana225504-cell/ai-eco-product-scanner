import streamlit as st

st.title("🌱 AI Eco Product Scanner")

product = st.text_input("Enter a product name")

if st.button("Analyze"):
    
    if "plastic" in product.lower():
        st.success("Material: Plastic")
        st.write("Recyclable: Yes")
        st.write("Suggestion: Use reusable bottles")

    elif "paper" in product.lower():
        st.success("Material: Paper")
        st.write("Recyclable: Yes")
        st.write("Suggestion: Recycle properly")

    elif "battery" in product.lower():
        st.error("Material: Chemical")
        st.write("Recyclable: Special recycling required")
        st.write("Suggestion: Dispose at e-waste center")

    else:
        st.warning("Eco impact unknown. Try plastic, paper, or battery.")
