import requests
from frontend.config import API_URL
from app.utils.llm_mapping import llm_mapping
from app.utils.similarity_search_mapping import similarity_search_mapping

def load_mappings():
    return llm_mapping, similarity_search_mapping

def classify_intention(phrase, model, provider, similarity_search_method):
    try:
        response = requests.post(
            API_URL,
            json={
                "phrase": phrase,
                "model": model,
                "provider": provider,
                "similarity_search_method": similarity_search_method,
            },
        )

        if response.status_code == 200:
            data = response.json()
            return data["intention"]
        else:
            return None

    except requests.exceptions.RequestException:
        return None