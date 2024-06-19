from pydantic import BaseModel, Field


class ValidationErrorMessage(BaseModel):
    status: str = Field(examples=["400"])
    code: str = Field(examples=["validation_error"])


class ResourceNotFoundErrorMessage(BaseModel):
    status: str = Field(examples=["404"])
    code: str = Field(examples=["resource_not_found_error"])


class InternalServerErrorMessage(BaseModel):
    status: str = Field(examples=["500"])
    code: str = Field(examples=["internal_server_error"])
