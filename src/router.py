from fastapi import APIRouter, HTTPException
from pathlib import Path
import json

router = APIRouter(prefix="")

JSON_PATH = Path("json.json")


@router.post("/browser-info")
async def fetch_browser_info(info: dict[str, object]) -> dict:
    # Create file if doesn't exist
    if not JSON_PATH.exists():
        JSON_PATH.write_text("[]", encoding="utf-8")

    try:
        # Read existing data
        with JSON_PATH.open("r", encoding="utf-8") as read_file:
            data = json.load(read_file)
            if not isinstance(data, list):
                raise ValueError("json.json must contain a list")

        # Append new info
        data.append(info)

        # Write back
        with JSON_PATH.open("w", encoding="utf-8") as write_file:
            json.dump(data, write_file, indent=2, ensure_ascii=False)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to write JSON: {e}")

    return {"ok": True}
