from fastapi import APIRouter, HTTPException
from app.models.request import TextInput
from app.config import lorax_client
from app.lorax_service import lorax_generate

router = APIRouter()

# Default adapter_id for decision makers category
DEFAULT_ADAPTER_ID = "decision_makers_summary_finetune_llama3_adapter/2"

@router.post("/decision_makers/")
async def summarize_for_decision_makers(
    article: str, 
    adapter_id: str = DEFAULT_ADAPTER_ID
):
    """
    Summarize an article to highlight its policy implications for decision makers.

    Args:
        article (str): The input article to be summarized.
        adapter_id (str): The adapter ID for the decision makers summarization model.
                          Default: "decision_makers_summary_finetune_llama3_adapter/2"

    Returns:
        dict: A summary for decision-makers including background, research question, global alignment,
              study method, and findings.

    Raises:
        HTTPException: If summarization fails.
    """
    try:
        prompt = f"""
        Summarize the policy implications of the following article for decision-makers.

        Article: {article}

        Use this format in your response:
        {{
            'intent': 'Policy Implications',
            'Background': '...',
            'Research Question': '...',
            'Global Alignment': '...',
            'Study Method': '...',
            'Findings': '...'
        }}

        Reply:
        """
        result = lorax_generate(lorax_client, prompt, adapter_id)
        return {"summary": result.generated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating decision-maker summary: {e}")
