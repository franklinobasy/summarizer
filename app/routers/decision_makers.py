from fastapi import APIRouter
from app.models.request import TextInput
from app.config import lorax_client
from app.lorax_service import lorax_generate

router = APIRouter()

@router.post("/decision_makers")
def decision_makers_endpoint(input: TextInput):
    prompt_template = """
    Request: Summarize the policy implications of the following article for decision-makers.

    Article: {article}

    {output_format}

    Reply:
    """
    output_format = """\
    {'intent': 'Policy Implications',
    'Background': '...',
    'Research Question': '...',
    'Global Alignment': '...',
    'Study Method': '...',
    'Findings': '...'}
    """
    prompt = prompt_template.format(article=input.text, output_format=output_format)
    return {"response": lorax_generate(lorax_client, prompt, input.adapter_id)}
