from fastapi import APIRouter, HTTPException
from app.models.request import TextInput
from app.config import lorax_client
from app.lorax_service import lorax_generate

router = APIRouter()

# Default adapter_id for donor category
DEFAULT_ADAPTER_ID = "donor_summary_finetune_llama3_adapter/3"

@router.post("/donor/")
async def summarize_for_donors(
    article: str, 
    adapter_id: str = DEFAULT_ADAPTER_ID
):
    """
    Summarize an article to describe its impact and funding needs for potential donors.

    Args:
        article (str): The input article to be summarized.
        adapter_id (str): The adapter ID for the donor summarization model.
                          Default: "donor_summary_finetune_llama3_adapter/3"

    Returns:
        dict: A structured summary for donors, including background, research question,
              global alignment, and findings.

    Raises:
        HTTPException: If summarization fails.
    """
    try:
        prompt = f"""
        Request: Describe the impact and funding needs based on the outcomes of the following article for potential donors.

        Article: {article}

        Use this format in your response:
        {{
            'intent': 'Impact and Funding Needs',
            'Background': '...',
            'Research Question': '...',
            'Global Alignment': '...',
            'Findings': '...'
        }}

        Reply:
        """
        result = lorax_generate(lorax_client, prompt, adapter_id)
        return {"summary": result.generated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating donor summary: {e}")
