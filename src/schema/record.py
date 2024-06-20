from pydantic import BaseModel, Field
from uuid import UUID


class RecordBase(BaseModel):
    id: UUID = Field(examples=["5c95a0b1-5785-438b-92b6-e3db0984459c"], description="Record ID")
    name: str = Field(examples=["Hachikou"], description="Record Name")
    profile_image: str = Field(
        examples=["https://www.xxxxxx.com"], description="Record Image URL"
    )
    owner_id: str = Field(examples=["321808401533890002944"], description="Owner ID")


class RecordUpdate(BaseModel):
    name: str = Field(examples=["Hachikou"], description="Record Name")
    profile_image: str = Field(
        examples=["https://www.xxxxxx.com"], description="Record Image URL"
    )


class RecordCreate(RecordBase):
    pass


class RecordResponse(RecordBase):
    pass

    class Config:
        orm_mode = True
