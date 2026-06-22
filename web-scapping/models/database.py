from pydantic import BaseModel
from datetime import date
from typing import Optional

class RegistrationData(BaseModel):
    domain: str
    registered_on: Optional[date]
    expires_on: Optional[date]
    updated_on: Optional[date]
    registrar: Optional[str] = None
    registrant_organization: Optional[str] = None
    registrant_country: Optional[str] = None
    status: Optional[list[str]] = None