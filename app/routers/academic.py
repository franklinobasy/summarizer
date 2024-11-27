from fastapi import APIRouter, Depends
from app.models.request import TextInput
from app.config import lorax_client
from app.lorax_service import lorax_generate

router = APIRouter()

@router.post("/academic")
def academic_endpoint(input: TextInput):
    prompt_template = """
    Request: Provide a detailed analysis of the following study for academic purposes.:

    Article: {article}

    {output_format}

    Reply:
    """
    output_format = """\
    {'intent': 'Detailed Analysis', 'Background': '...', 'Research Question': '...', 'Study Method: '...', 'Findings': '...', 'Study Limitations': '...'}
    """
    adapter_id = "academic_summary_finetune_llama3_adapter/5"
    prompt = prompt_template.format(article=input.text, output_format=output_format)
    return {"response": lorax_generate(lorax_client, prompt, input.adapter_id)}
