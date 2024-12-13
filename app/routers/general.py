from typing import Optional
from fastapi import APIRouter, Form, HTTPException, UploadFile
from app.lorax_service import generate_text
from app.utilities.file_process import (
    extract_text_from_docx,
    extract_text_from_pdf
)

router = APIRouter()


@router.post("/general/get_text_from_file")
async def get_text_from_file(
    file: UploadFile
):
    """
    Extract text from PDF or DOC/DOCX file.


    Args:
        file (UploadFile): Uploaded file (PDF or DOC/DOCX)

    
    Returns:
        dict: Extracted text.

    
    Raises:
        HTTPException: If text extraction fails or input is invalid.
    """


    try:
        if file:
            if file.content_type == "application/pdf":
                text = extract_text_from_pdf(file)
            elif file.content_type in [
                "application/msword",
                "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            ]:
                text = extract_text_from_docx(file)
            else:
                raise HTTPException(
                    status_code=400, detail="Unsupported file type. Upload a PDF or DOC/DOCX file."
                )
            
            return {text: text}
        else:
            raise HTTPException(status_code=400, detail="Invalid file format. Expected an UploadFile.")
        
    except HTTPException as e:
        raise e
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error encountered while extracting text: {e}")
    

@router.post("/general/manual_prompting")
async def manual_prompt(prompt: str, adapter_id: str):
    """
    Generate a summary using custom prompt.

    Args:
        prompt (str): The input prompt
        adapter_id (str): The adapter ID for the summarisation model.

    Returns:
        dict: A structured summary.

    Raises:
        HTTPException: If summarization fails or input is invalid.
    """
    try:
        if not prompt:
            raise HTTPException(
                status_code=400, detail="'prompt' must be provided, it should not be empty."
            )
        
        if not adapter_id:
            raise HTTPException(
                status_code=400, detail="'adapter_id' must be provided, it should not be empty."
            )
        
        result = generate_text(
            prompt=prompt, adapter_id=adapter_id
        )

        return {
            "Summary": result
        }

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error generating summary: {e}"
        )
