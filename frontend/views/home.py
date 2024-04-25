import streamlit as st
from frontend.utils import classify_intention, load_mappings

def home():
    st.title("Smart Banking Intention Classifier")

    # Load mappings from files
    llm_api_mapping, similarity_search_mapping = load_mappings()

    # Get available models, providers, and similarity search methods
    models = list(llm_api_mapping.keys())
    providers = list(llm_api_mapping[models[0]]["provider"].keys())
    similarity_search_methods = list(similarity_search_mapping["method"].keys())

    # Create checklist options for model, provider, and similarity search method
    selected_model = st.selectbox("Select a model", models)
    selected_provider = st.selectbox("Select a provider", providers)
    selected_similarity_search_method = st.selectbox("Select a similarity search method", similarity_search_methods)

    phrase = st.text_input("Enter a phrase")

    if st.button("Classify"):
        intention = classify_intention(phrase, selected_model, selected_provider, selected_similarity_search_method)
        if intention:
            st.success(f"Intention: {intention}")
        else:
            st.error("An error occurred. Please try again.")