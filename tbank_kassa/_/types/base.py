from pydantic import BaseModel, ConfigDict


class TBankObject(BaseModel):
    model_config = ConfigDict(
        use_enum_values=True,
        validate_assignment=True,
        frozen=True,
        populate_by_name=True,
    )
