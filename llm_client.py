from ollama import chat
from schemas import BAResponse

def analyse_requirement(system_prompt, user_prompt):
    response = chat(
        model="qwen3:8b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        format=BAResponse.model_json_schema(),
        options={"temperature": 0},
        think=False
    )

    return BAResponse.model_validate_json(
        response.message.content
    )
