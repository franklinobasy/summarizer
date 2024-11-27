from fastapi import APIRouter, HTTPException
from app.models.request import TextInput
from app.config import lorax_client
from app.lorax_service import lorax_generate

router = APIRouter()

# Default adapter_id for academic category
DEFAULT_ADAPTER_ID = "academic_summary_finetune_llama3_adapter/5"

@router.post("/academic/")
async def summarize_for_academics(
    article: str, 
    adapter_id: str = DEFAULT_ADAPTER_ID
):
    """
    Summarize an article for academic purposes.

    Args:
        article (str): The input article to be analyzed.
        adapter_id (str): The adapter ID for the academic summarization model. 
                          Default: "academic_summary_finetune_llama3_adapter/5"

    Returns:
        dict: A structured summary for academics including background, research question,
              study method, findings, and limitations.

    Raises:
        HTTPException: If summarization fails.
    """
    try:
        prompt = f"""
        Request: Provide a detailed analysis of the following study for academic purposes.

        Article: {article}

        Use this format in your response:
        {{
            'intent': 'Detailed Analysis',
            'Background': '...',
            'Research Question': '...',
            'Study Method': '...',
            'Findings': '...',
            'Study Limitations': '...'
        }}

        Reply:
        """
        result = lorax_generate(lorax_client, prompt, adapter_id)
        return {"summary": result.generated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating academic summary: {e}")
