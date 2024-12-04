from typing import Optional
from fastapi import APIRouter, Form, HTTPException, UploadFile
from app.lorax_service import lorax_generate, generate_text
from app.utilities.file_process import extract_text_from_docx, extract_text_from_pdf

router = APIRouter()

# Default adapter_id for donor category
DEFAULT_ADAPTER_ID = "donor_summary_finetune_llama3_adapter/3"

@router.post("/donor/")
async def summarize_for_donors(
    article: Optional[str] = Form(None),
    file: Optional[UploadFile] = None,
    adapter_id: str = Form(DEFAULT_ADAPTER_ID),
):
    """
    Summarize an article to describe its impact and funding needs for potential donors.

    Args:
        article (str): The input article to be summarized.
        file (UploadFile): An optional uploaded file (PDF or DOC/DOCX).
        adapter_id (str): The adapter ID for the donor summarization model.
                          Default: "donor_summary_finetune_llama3_adapter/3"

    Returns:
        dict: A structured summary for donors, including background, research question,
              global alignment, and findings.

    Raises:
        HTTPException: If summarization fails or input is invalid.
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
        result = generate_text(prompt, adapter_id)
        return {"summary": result}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating donor summary: {e}")
    