from fastapi import APIRouter, Depends, HTTPException
from app.models.schemas import IntentionRequest
from app.services.intention_classifier import classify
from app.utils.llm_mapping import llm_mapping
from app.utils.similarity_search_mapping import similarity_search_mapping

router = APIRouter()

@router.post("/classify")
async def classify_intention(phrase_model_provider: IntentionRequest):
    model_name = phrase_model_provider.model.lower()
    provider_name = phrase_model_provider.provider.lower()
    similarity_search_method = phrase_model_provider.similarity_search_method.lower()
    
    if model_name not in llm_mapping or provider_name not in llm_mapping[model_name]['provider']:
        raise HTTPException(status_code=400, detail=f"Model '{model_name}' with provider '{provider_name}' is not available.")
    
    if similarity_search_method not in similarity_search_mapping['method']:
        raise HTTPException(status_code=400, detail=f"Similarity search method '{similarity_search_method}' is not available.")
    
    print(phrase_model_provider.phrase, model_name, provider_name, similarity_search_method)
    intention = classify(phrase_model_provider.phrase, model_name, provider_name, similarity_search_method)
    return {"intention": intention}