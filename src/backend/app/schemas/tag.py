from pydantic import BaseModel, field_validator


class TagCreate(BaseModel):
    name: str

    @field_validator("name")
    @classmethod
    def validate_and_normalize_name(cls, value: str) -> str:
        value = value.strip().lower()
        if not value:
            raise ValueError("Tag name must not be empty or whitespace.")
        return value
