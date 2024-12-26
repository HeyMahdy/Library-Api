from pydantic import BaseModel,ConfigDict
from typing import Optional

# Success Response Model
class SuccessResponse(BaseModel):
    status: str
    message: str
    model_config = ConfigDict(from_attributes=True)# You can include additional data if necessary

# Error Response Model
class ErrorResponse(BaseModel):
    status: str
    message: str
    model_config = ConfigDict(from_attributes=True)
