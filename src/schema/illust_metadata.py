from pydantic import BaseModel, Field
from uuid import UUID
from typing import List
from src.enum.genre_enum import GenreEnum



class IllustMetadataBase(BaseModel):
    id: UUID = Field(examples=["5c95a0b1-5785-438b-92b6-e3db0984459c"], description="Illustration Metadata ID")
    name: str = Field(max_length=20, examples=["サンプル イラスト"], description="Illustration Name")
    genre: GenreEnum = Field(examples=["乗り物"], description="Illustration Genre")
    original_image: str = Field(max_length=255, examples=["https://www.example.com/image.png"], description="Illustration original Image URL")
    badge_image: str = Field(max_length=255, examples=["https://www.example.com/image.png"], description="Illustration badge Image URL")
    contour_points: List[dict] = Field(description="List of contour points")


class IllustMetadataUpdate(BaseModel):
    name: str = Field(max_length=20, examples=["サンプル イラスト"], description="Illustration Name")
    genre: GenreEnum = Field(examples=["乗り物"], description="Illustration Genre")
    original_image: str = Field(max_length=255, examples=["https://www.example.com/image.png"], description="Illustration original Image URL")
    badge_image: str = Field(max_length=255, examples=["https://www.example.com/image.png"], description="Illustration badge Image URL")
    contour_points: List[dict] = Field(description="List of contour points")


class IllustMetadataCreate(IllustMetadataBase):
    pass


class IllustMetadataResponse(IllustMetadataBase):
    pass

    class Config:
        orm_mode = True


class IllustMetadataContourResponse(BaseModel):
    id: UUID = Field(examples=["5c95a0b1-5785-438b-92b6-e3db0984459c"], description="Illustration Metadata ID")
    contour_points: List[dict] = Field(description="List of contour points")
    
    class Config:
        orm_mode = True


class IllustMetadataBadgeImageResponse(BaseModel):
    id: UUID = Field(examples=["5c95a0b1-5785-438b-92b6-e3db0984459c"], description="Illustration Metadata ID")
    name: str = Field(max_length=20, examples=["サンプル イラスト"], description="Illustration Name")
    badge_image: str = Field(max_length=255, examples=["https://www.example.com/image.png"], description="Illustration badge Image URL")

    class Config:
        orm_mode = True


class IllustMetadataBasicInfoResponse(BaseModel):
    id: UUID = Field(examples=["5c95a0b1-5785-438b-92b6-e3db0984459c"], description="Illustration Metadata ID")
    name: str = Field(max_length=20, examples=["サンプル イラスト"], description="Illustration Name")
    genre: GenreEnum = Field(examples=["乗り物"], description="Illustration Genre")
    original_image: str = Field(max_length=255, examples=["https://www.example.com/image.png"], description="Illustration original Image URL")


    class Config:
        orm_mode = True