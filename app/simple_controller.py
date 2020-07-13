from events import EventIn, EventOut, EventUpdate
from fastapi.logger import logger
import events_service

async def receive_do_something_and_return(payload: EventIn):
    logger.debug(f"simple_controller: receive_do_something_and_return {payload}")
    return await events_service.receive_do_something_and_return(payload)

# async def get_all_events():
#     logger.debug(f"Controller: Getting all events")
#     return await events_service.get_all_events()

# async def get_event(id):
#     logger.debug(f"Controller: Getting event {id}")
#     return await events_service.get_event(id)

# async def delete_event(id: int):
#     logger.debug(f"Controller: Deleting event {id}")
#     return await events_service.delete_event(id)

# async def update_event(id: int, payload: EventIn):
#     logger.debug(f"Controller: Updating event {id} with {payload}")
#     return await events_service.update_event(id, payload)

