from pydantic import BaseModel, Field


class RoutingBase(BaseModel):
    index: int = Field(examples=["1"], description="Index")
    latitude: float = Field(examples=["35.705390"], description="Latitude")
    longitude: float = Field(examples=["139.664535"], description="Longitude")


class RoutingResponse(RoutingBase):
    pass

    class Config:
        orm_mode = True
