from datetime import datetime
from typing import List, Optional
from camel_model import CamelModel

class EventIn(CamelModel):
    name: str
    start_time: str
    end_time: str

class EventOut(EventIn):
    name: str
    start_time: str
    end_time: str

class EventUpdate(EventIn):
    name: str
    start_time: str
    end_time: str

# class EventIn(CamelModel):
#     name: str
#     start_time: datetime
#     end_time: datetime

# class EventOut(EventIn):
#     id: int

# class EventUpdate(EventIn):
#     name: Optional[str] = None
#     start_time: Optional[datetime] = None
#     end_time: Optional[datetime] = None
