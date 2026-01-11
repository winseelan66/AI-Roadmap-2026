from pydantic import BaseModel

class SexCreate(BaseModel):
    name: str

class SexUpdate(BaseModel):
    name: str

class SexResponse(BaseModel):
    sex_id: int
    name: str

    class Config:
        from_attributes = True
