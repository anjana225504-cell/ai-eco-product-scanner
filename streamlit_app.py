import streamlit as st

st.title("🌱 Eco Product Scanner")

product = st.text_input("Enter product name")

def analyze_product(product):

    product = product.lower()

    if "plastic" in product:
        return "Material: Plastic\nRecyclable: Sometimes\nImpact: High plastic pollution\nSuggestion: Use reusable alternatives\nEco Score: Low"

    elif "paper" in product:
        return "Material: Paper\nRecyclable: Yes\nImpact: Biodegradable\nSuggestion: Use recycled paper\nEco Score: High"

    elif "glass" in product:
        return "Material: Glass\nRecyclable: Yes\nImpact: Low environmental impact\nSuggestion: Reuse glass containers\nEco Score: High"

    elif "metal" in product or "steel" in product:
        return "Material: Metal\nRecyclable: Highly recyclable\nImpact: Durable and reusable\nSuggestion: Use stainless steel products\nEco Score: High"

    else:
        return "Material: Unknown\nRecyclable: Unknown\nImpact: Needs further analysis\nSuggestion: Prefer eco-friendly materials\nEco Score: Medium"

if st.button("Scan Product"):

    if product == "":
        st.write("Please enter a product name")
    else:
        result = analyze_product(product)
        st.subheader("🌍 Result")
        st.text(result)
