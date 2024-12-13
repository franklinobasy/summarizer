from typing import Optional
from fastapi import APIRouter, Form, HTTPException, UploadFile
from app.lorax_service import lorax_generate, generate_text
from app.utilities.file_process import extract_text_from_docx, extract_text_from_pdf
from app.prompts.academic_prompts import PROMPT_V1

router = APIRouter()

# Default adapter_id for academic category
DEFAULT_ADAPTER_ID = "academic_summary_finetune_llama3_adapter/8"

@router.post("/academic/")
async def summarize_for_academics(
    article: Optional[str] = Form(None),
    file: Optional[UploadFile] = None,
    adapter_id: str = Form(DEFAULT_ADAPTER_ID),
):
    """
    Summarize an article for academic purposes.

    Args:
        article (str): The input article to be analyzed.
        file (UploadFile): An optional uploaded file (PDF or DOC/DOCX).
        adapter_id (str): The adapter ID for the academic summarization model. 
                          Default: "academic_summary_finetune_llama3_adapter/5"

    Returns:
        dict: A structured summary for academics including background, research question,
              study method, findings, and limitations.

    Raises:
        HTTPException: If summarization fails or input is invalid.
    """
    try:
        if file:
            if isinstance(file, UploadFile):
                if file.content_type == "application/pdf":
                    article = extract_text_from_pdf(file)
                elif file.content_type in [
                    "application/msword",
                    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                ]:
                    article = extract_text_from_docx(file)
                else:
                    raise HTTPException(
                        status_code=400, detail="Unsupported file type. Upload a PDF or DOC/DOCX file."
                    )
            else:
                raise HTTPException(status_code=400, detail="Invalid file format. Expected an UploadFile.")
            
        if not article:
            raise HTTPException(status_code=400, detail="Either 'article' text or a valid 'file' must be provided.")

        prompt = PROMPT_V1.format(article=article)

        result = generate_text(prompt, adapter_id)
        return {"summary": result}

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating academic summary: {e}")
