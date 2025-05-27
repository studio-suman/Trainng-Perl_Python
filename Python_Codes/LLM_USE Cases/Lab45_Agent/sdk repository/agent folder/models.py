from pydantic import BaseModel, Field
from typing import Any, Dict

class ExecuteRequest(BaseModel):
    user_id: str  = "00000000-0000-0000-0000-0000000000a0"
    tenant_id: str = "00000000-0000-0000-0000-0000000000b0"
    session_id: str | None = None
    message: str | None = None
    api_key: str | None = None
    dataset_id: str | None = None  # optional
    files: list[str] | None = None  # optional
