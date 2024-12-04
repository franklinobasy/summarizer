from typing import Optional
from fastapi import APIRouter, Form, HTTPException, UploadFile
from app.lorax_service import lorax_generate, generate_text
from app.utilities.file_process import extract_text_from_docx, extract_text_from_pdf

router = APIRouter()

# Default adapter_id for broader public category
DEFAULT_ADAPTER_ID = "broader_public_summary_finetune_llama3_adapter/2"

@router.post("/broader_public/")
async def simplify_for_public(
    article: Optional[str] = Form(None),
    file: Optional[UploadFile] = None,
    adapter_id: str = Form(DEFAULT_ADAPTER_ID),
):
    """
    Simplify an article's findings for the broader public.

    Args:
        article (str): The input article to be simplified.
        file (UploadFile): An optional uploaded file (PDF or DOC/DOCX).
        adapter_id (str): The adapter ID for the broader public summarization model.
                          Default: "broader_public_summary_finetune_llama3_adapter/2"

    Returns:
        dict: A simplified explanation including background, research question, findings, and additional notes.

    Raises:
        HTTPException: If simplification fails or input is invalid.
    """
    try:
        if file:
            if file.content_type == "application/pdf":
                article = extract_text_from_pdf(file)
            elif file.content_type in ["application/msword", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"]:
                article = extract_text_from_docx(file)
            else:
                raise HTTPException(status_code=400, detail="Unsupported file type. Upload a PDF or DOC/DOCX file.")
        elif not article:
            raise HTTPException(status_code=400, detail="Either 'article' or 'file' must be provided.")

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
        result = generate_text(prompt, adapter_id)
        return {"summary": result}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating public summary: {e}")
    