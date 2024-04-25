from app.controllers.similarity_search_controller import sentence_bard_search, sentence_transformer_search

similarity_search_mapping = {
    'method': {
        'sentence_transformer': sentence_transformer_search,
        'sentence_bard': sentence_bard_search
    }
}