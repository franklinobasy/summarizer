from fastapi import APIRouter, HTTPException
from app.models.request import TextInput
from app.config import lorax_client
from app.lorax_service import lorax_generate

router = APIRouter()

# Default adapter_id for broader public category
DEFAULT_ADAPTER_ID = "broader_public_summary_finetune_llama3_adapter/2"

@router.post("/broader_public/")
async def simplify_for_public(
    article: str, 
    adapter_id: str = DEFAULT_ADAPTER_ID
):
    """
    Simplify an article's findings for the broader public.

    Args:
        article (str): The input article to be simplified.
        adapter_id (str): The adapter ID for the broader public summarization model.
                          Default: "broader_public_summary_finetune_llama3_adapter/2"

    Returns:
        dict: A simplified explanation including background, research question, findings, and additional notes.

    Raises:
        HTTPException: If simplification fails.
    """
    try:
        prompt = f"""
        Request: Explain the findings of the following article in simple terms for the general public.

        Article: {article}

        Use this format in your response:
        {{
            'intent': 'Simplified Explanation',
            'Background': '...',
            'Research Question': '...',
            'Findings': '...',
            'Note': '...'
        }}

        Reply:
        """
        result = lorax_generate(lorax_client, prompt, adapter_id)
        return {"summary": result.generated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating public summary: {e}")
