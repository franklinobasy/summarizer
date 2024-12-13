PROMPT_V1 = '''
Summarize the policy implications of the following article for decision-makers.

Article: {article}

Use this format in your response:
{{
    'intent': 'Policy Implications',
    'Background': '...',
    'Research Question': '...',
    'Global Alignment': '...',
    'Study Method': '...',
    'Findings': '...'
}}

Reply:
'''