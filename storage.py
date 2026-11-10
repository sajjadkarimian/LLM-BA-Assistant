import json
from pathlib import Path
from datetime import datetime, timezone
from uuid import uuid4


def save_analysis(business_requirement, validated):
    analysis_id = uuid4().hex

    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    output_file = output_dir / f"ba_analysis_{analysis_id}.json"
    analysis_record = {
            "analysis_id": analysis_id,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "business_requirement": business_requirement,
            "model_name": "qwen3:8b",
            "review_status": "pending_review",
            "analysis": validated.model_dump()
    }
    with output_file.open("w", encoding="utf-8") as file:
            json.dump(
            analysis_record,
            file,
            indent=4,
            ensure_ascii=False
        )
    return output_file
            
