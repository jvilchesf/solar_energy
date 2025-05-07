from pydantic import BaseModel
from datetime import datetime


class tp_record(BaseModel):
    mRID: str
    businessType: str
    objectAggregation: str
    inBiddingZone_Domain: str
    quantity_Measure_Unit: str
    MktPSRType: str
    Period: str
    Point: list[Point]        

class Point(BaseModel):
    position: str
    quantity: str
