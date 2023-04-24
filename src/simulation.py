
from tag import BaseTag
from reader import BinaryTagReader
import time
import settings
from settings import logger

def run_simulation(num_tags=10, reader_cls=BinaryTagReader, tag_cls=BaseTag):
    # Create a collection of tags
    tags = [tag_cls() for _ in range(num_tags)]
    tag_reader = reader_cls()

    #Current epoch time
    min_time = int(time.time())
    max_time=min_time + settings.SIMULATED_DURATION

    for t in tags:
        t.generate_time(min_time, max_time)
        logger.debug(f"TIME: {t.transmit_time}, tag: {t.id}")

    transmission_map = {}
    for t in tags:
        if not transmission_map.get(t.transmit_time):
            transmission_map[t.transmit_time] = [t]
        else:
            transmission_map[t.transmit_time].append(t)

    slots = 0
    for t, tags in transmission_map.items():
        if len(tags) <= 1:
            continue

        logger.debug(f"[NEW COLLISION] De-colliding: {tags} at time: {t}")
        slots += tag_reader.manage_collision(tags)
    
    logger.debug(f"Tags: {num_tags}\t Total Slots: {slots}")
    return num_tags, slots


