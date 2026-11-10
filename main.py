
from dbm import error

from ollama import chat
import json 
from schemas import BAResponse
from pydantic import ValidationError
from pathlib import Path
from uuid import uuid4
from datetime import datetime, timezone
from llm_client import analyse_requirement
from storage import save_analysis
from ollama import ResponseError

output_dir = Path("outputs")
output_dir.mkdir(exist_ok=True)
analysis_id = uuid4().hex

output_file = output_dir / f"ba_analysis_{analysis_id}.json"

system_prompt = """
You are an experienced Business Analyst.

Your responsibilities:
- Analyse business requirements.
- Write clear user stories.
- Define testable acceptance criteria.
- Identify missing information.

Rules:
- Do not invent business rules or numerical limits.
- Do not make unsupported assumptions.
- If information is missing, ask clarification questions.
- Use professional English.
"""

business_requirement = input(
    "Enter a business requirement: "
)

user_prompt = f"""
Analyse the following business requirement:

{business_requirement}

Create:
1. One user story.
2. Exactly two acceptance criteria.
3. Exactly three clarification questions.

Do not invent unsupported business rules.
"""



try:
    validated = analyse_requirement(
        system_prompt,
        user_prompt
    )

    output_file = save_analysis(
        business_requirement,
        validated
    )

    print("Analysis saved to:", output_file)

except ConnectionError:
    print("Cannot connect to Ollama.")
    print("Please check that Ollama is running.")

except ResponseError as error:
    print("Ollama API error:", error)

except ValidationError as error:
    print("Invalid LLM response:")
    print(error)
