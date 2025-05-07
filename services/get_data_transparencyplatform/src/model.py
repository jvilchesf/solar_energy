from pydantic import BaseModel
from datetime import datetime

class eco2grid(BaseModel):
    zone_code: str
    interval: datetime
    consumption_co2_intensity: float
    consumption_co2_emitted: float
    consumption_renewable_ratio: float
    production_renewable_ratio: float
    consumptions: dict
