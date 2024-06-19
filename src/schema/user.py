from pydantic import BaseModel, Field


class UserBase(BaseModel):
    id: str = Field(examples=["321808401533890002944"], description="User ID")
    username: str = Field(examples=["Taro Yamada"], description="User Name")
    profile_image: str = Field(
        examples=["https://www.xxxxxx.com"], description="Profile Image URL"
    )


class UserUpdate(BaseModel):
    username: str = Field(examples=["Taro Yamada"], description="User Name")
    profile_image: str = Field(
        examples=["https://www.xxxxxx.com"], description="Profile Image URL"
    )


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    pass

    class Config:
        orm_mode = True
