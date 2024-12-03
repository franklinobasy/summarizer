import requests

def generate_text(input_text, adapter_id, adapter_source, max_new_tokens, temperature, authorization_token):
    """
    Sends a POST request to the Predibase API to generate text.

    Args:
        input_text (str): The input prompt for the model.
        adapter_id (str): The adapter ID to use.
        adapter_source (str): The adapter source.
        max_new_tokens (int): Maximum number of new tokens to generate.
        temperature (float): Sampling temperature.
        authorization_token (str): Bearer token for authentication.

    Returns:
        dict: The response from the API as a dictionary.
    """
    url = "https://serving.app.predibase.com/a2f486/deployments/v2/llms/llama-3-1-8b-instruct/generate"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {authorization_token}",
    }
    payload = {
        "inputs": input_text,
        "parameters": {
            "adapter_id": adapter_id,
            "adapter_source": adapter_source,
            "max_new_tokens": max_new_tokens,
            "temperature": temperature,
        },
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

# Example usage
if __name__ == "__main__":
    input_text = "What is your name?"
    adapter_id = "academic_summary_finetune_llama3_adapter/5"
    adapter_source = "pbase"
    max_new_tokens = 20
    temperature = 0.1
    authorization_token = "pb_Jw-99QJiXqGqZMWTibNOGA"

    try:
        result = generate_text(input_text, adapter_id, adapter_source, max_new_tokens, temperature, authorization_token)
        print(result['generated_text'])
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
