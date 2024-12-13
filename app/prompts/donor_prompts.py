PROMPT_V1 = '''
Request: Describe the impact and funding needs based on the outcomes of the following article for potential donors.

Article: {article}

Use this format in your response:
{{
    'intent': 'Impact and Funding Needs',
    'Background': '...',
    'Research Question': '...',
    'Global Alignment': '...',
    'Findings': '...'
}}

Reply:
'''