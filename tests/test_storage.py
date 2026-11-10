import json
from schemas import BAResponse
from storage import save_analysis


def test_save_analysis(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    requirement = "A university needs an attendance system."

    validated = BAResponse(
        user_story="As an administrator, I want to track attendance.",
        acceptance_criteria=[
            "The system records attendance.",
            "The system displays attendance reports."
        ],
        clarification_questions=[
            "Who records attendance?",
            "Which reports are required?",
            "How often are reports generated?"
        ]
    )

    output_file = save_analysis(requirement, validated)

    assert output_file.exists()

    with output_file.open("r", encoding="utf-8") as file:
        data = json.load(file)

    assert data["business_requirement"] == requirement
    assert data["review_status"] == "pending_review"
    assert len(data["analysis"]["acceptance_criteria"]) == 2

