
PROMPT_V1 = """
Summarize the academic article below in a strict JSON format with the following keys only:
{{"intent": "Simplified Academic Explanation",
    "Background": "Brief historical context and initial situation",
    "Research Question": "Main objectives or questions addressed",
    "Findings": "Key results and data",
    "Note": "Important implications or challenges"
}}

Requirements:
- Provide ONLY the JSON output
- Do not include any additional text, markdown, or explanations
- Ensure all text values are properly escaped
- Keep each section concise but informative
- Format as valid JSON with proper quotes and commas

<article>

{article}

</article>
"""