from app.utils.llm_mapping import llm_mapping
from app.utils.similarity_search_mapping import similarity_search_mapping
from app.utils.preprocessor import clean_text


def classify(query, model_name, provider_name, similarity_search_method):
    cleaned_query = clean_text(query)
    
    similarity_search_func = similarity_search_mapping['method'][similarity_search_method]
    intention, similarity = similarity_search_func(cleaned_query)
    
    print(similarity)
    if similarity < 0.4:
        classify_func = llm_mapping[model_name]['provider'][provider_name]
        intention = classify_func(cleaned_query)
    
    return intention