from fastapi import APIRouter
from app.models.request import TextInput
from app.config import lorax_client
from app.lorax_service import lorax_generate

router = APIRouter()

@router.post("/broader_public")
def broader_public_endpoint(input: TextInput):
    prompt_template = """
    Request: Explain the findings of the following article in simple terms for the general public.

    Article: {article}

    {output_format}

    Reply:
    """
    output_format = """\
    {'intent': 'Simplified Explanation',
    'Background': '...',
    'Research Question': '...',
    'Findings': '...',
    'Note': '...'}
    """
    prompt = prompt_template.format(article=input.text, output_format=output_format)
    return {"response": lorax_generate(lorax_client, prompt, input.adapter_id)}
