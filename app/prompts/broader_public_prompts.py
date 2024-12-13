PROMPT_V1 = '''
Request: Explain the findings of the following article in simple terms for the general public.

Article: {article}

Use this format in your response:
{{
    'intent': 'Simplified Explanation',
    'Background': '...',
    'Research Question': '...',
    'Findings': '...',
    'Note': '...'
}}

Reply:
'''