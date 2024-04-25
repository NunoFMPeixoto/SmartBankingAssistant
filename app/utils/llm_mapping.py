from app.controllers.llama2_controller import replicate_llama2, langchain_llama2
from app.controllers.gpt4_controller import replicate_gpt4, langchain_gpt4

llm_mapping = {
    'llama2': {
        'provider': {
            'replicate': replicate_llama2,
            'langchain': langchain_llama2
        }
    },
    'gpt4': {
        'provider': {
            'replicate': replicate_gpt4,
            'langchain': langchain_gpt4
        }
    }
}