from pydantic import BaseModel, Field


class BAResponse(BaseModel):
    user_story: str = Field(min_length=10)

    acceptance_criteria: list[str] = Field(
        min_length=2,
        max_length=2
    )

    clarification_questions: list[str] = Field(
        min_length=3,
        max_length=3
    )
