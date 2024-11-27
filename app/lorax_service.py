from lorax.types import Response as LoraxResponse

def lorax_generate(lorax_client, prompt, adapter_id, **kwargs):
    lorax_response: LoraxResponse = lorax_client.generate(
        prompt=prompt,
        adapter_id=adapter_id,
        **kwargs,
    )
    return lorax_response.generated_text
