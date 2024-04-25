from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import torch

def sentence_transformer_search(query):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    intentions = [
        "search product",
        "product info",
        "add to cart",
        "go to shopping cart",
        "confirm order"
    ]
    intention_embeddings = model.encode(intentions)

    query_embedding = model.encode(query)
    similarities = cosine_similarity([query_embedding], intention_embeddings)[0]
    max_similarity_idx = similarities.argmax()
    return intentions[max_similarity_idx], similarities[max_similarity_idx]



def sentence_bard_search(query):
    model = SentenceTransformer('sentence-transformers/all-distilroberta-v1')
    intentions = [
        "search product",
        "product info",
        "add to cart",
        "go to shopping cart",
        "confirm order"
    ]
    intention_embeddings = model.encode(intentions, convert_to_tensor=True)

    query_embedding = model.encode(query, convert_to_tensor=True)
    query_embedding = query_embedding.unsqueeze(0)  # Add batch dimension

    similarities = torch.nn.functional.cosine_similarity(query_embedding, intention_embeddings)
    max_similarity_idx = torch.argmax(similarities).item()
    return intentions[max_similarity_idx], similarities[max_similarity_idx].item()