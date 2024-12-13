from typing import Optional
from fastapi import APIRouter, Form, HTTPException, UploadFile
from app.lorax_service import lorax_generate, generate_text
from app.utilities.file_process import extract_text_from_docx, extract_text_from_pdf
from app.prompts.decision_makers_prompts import PROMPT_V1

router = APIRouter()

# Default adapter_id for decision makers category
DEFAULT_ADAPTER_ID = "decision_makers_summary_finetune_llama3_adapter/2"

@router.post("/decision_makers/")
async def summarize_for_decision_makers(
    article: Optional[str] = Form(None),
    file: Optional[UploadFile] = None,
    adapter_id: str = Form(DEFAULT_ADAPTER_ID),
):
    """
    Summarize an article to highlight its policy implications for decision makers.

    Args:
        article (str): The input article to be summarized.
        file (UploadFile): An optional uploaded file (PDF or DOC/DOCX).
        adapter_id (str): The adapter ID for the decision-makers summarization model.
                          Default: "decision_makers_summary_finetune_llama3_adapter/2"

    Returns:
        dict: A summary for decision-makers including background, research question, global alignment,
              study method, and findings.

    Raises:
        HTTPException: If summarization fails or input is invalid.
    """
    try:
        if file:
            if file.content_type == "application/pdf":
                article = extract_text_from_pdf(file)
            elif file.content_type in [
                "application/msword", 
                "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            ]:
                article = extract_text_from_docx(file)
            else:
                raise HTTPException(
                    status_code=400, detail="Unsupported file type. Upload a PDF or DOC/DOCX file."
                )
        elif not article:
            raise HTTPException(
                status_code=400, detail="Either 'article' or 'file' must be provided."
            )

        prompt = PROMPT_V1.format(article=article)

        result = generate_text(prompt, adapter_id)
        
        return {"summary": result}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating decision-maker summary: {e}")
    