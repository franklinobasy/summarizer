from fastapi import APIRouter
from app.models.request import TextInput
from app.config import lorax_client
from app.lorax_service import lorax_generate

router = APIRouter()

@router.post("/donor")
def donor_endpoint(input: TextInput):
    prompt_template = """
    Request: Describe the impact and funding needs based on the outcomes of the following article for potential donors.

    Article: {article}

    {output_format}

    Reply:
    """
    output_format = """\
    {'intent': 'Impact and Funding Needs',
    'response': 'Background: ..., Research Question: ..., Global Alignment: ..., Findings: ...'}
    """
    prompt = prompt_template.format(article=input.text, output_format=output_format)
    return {"response": lorax_generate(lorax_client, prompt, input.adapter_id)}
