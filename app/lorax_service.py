from lorax.types import Response as LoraxResponse
from .config import API_TOKEN, lorax_client
import requests

def lorax_generate(prompt, adapter_id, **kwargs):
    lorax_response: LoraxResponse = lorax_client.generate(
        prompt=prompt,
        adapter_id=adapter_id,
        max_tokens=100,
        **kwargs,
    )
    return lorax_response.generated_text


def generate_text(prompt, adapter_id, **kwargs):
    """
    Sends a POST request to the Predibase API to generate text.

    Args:
        prompt (str): The input prompt for the model.
        adapter_id (str): The adapter ID to use.
        adapter_source (str): The adapter source.
        max_new_tokens (int): Maximum number of new tokens to generate.
        temperature (float): Sampling temperature.
        authorization_token (str): Bearer token for authentication.

    Returns:
        dict: The response from the API as a dictionary.
    """
    if not kwargs:
        adapter_source = "pbase"
        max_new_tokens = 1000
        temperature = 0.1
    
    else:
        adapter_source = kwargs.get("adapter_source")
        max_new_tokens = kwargs.get("max_new_tokens")
        temperature = kwargs.get("temperature")

    url = "https://serving.app.predibase.com/a2f486/deployments/v2/llms/llama-3-1-8b-instruct/generate"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_TOKEN}",
    }
    payload = {
        "inputs": prompt,
        "parameters": {
            "adapter_id": adapter_id,
            "adapter_source": adapter_source
        },
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json()['generated_text']
    else:
        response.raise_for_status()
