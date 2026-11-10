
import pytest

from pydantic import ValidationError
from schemas import BAResponse


def test_invalid_acceptance_criteria():

    invalid_data = {
        "user_story": "As a student, I want to see my assignments.",
        "acceptance_criteria": [
            "The system displays assignments."
        ],
        "clarification_questions": [
            "Who can access the assignments?",
            "Which courses are included?",
            "How often is the data updated?"
        ]
    }

    with pytest.raises(ValidationError):
        BAResponse.model_validate(invalid_data)


def test_valid_ba_response():

    valid_data = {
        "user_story": "As a student, I want to view my assignments.",
        "acceptance_criteria": [
            "The system displays all assignments.",
            "The system displays assignment deadlines."
        ],
        "clarification_questions": [
            "Which courses are included?",
            "Who can access assignments?",
            "How often is data updated?"
        ]
    }

    result = BAResponse.model_validate(valid_data)

    assert len(result.acceptance_criteria) == 2
    assert len(result.clarification_questions) == 3
