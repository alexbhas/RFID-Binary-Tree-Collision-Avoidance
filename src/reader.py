from abc import ABC, abstractmethod
from settings import logger
class BaseTagReader(ABC):
    ''' define a common interface for Readers implementing collision detection protocols'''
    def __init__(self):
        pass

    @abstractmethod
    def manage_collision(self, tags):
        pass


class GenOneTagReader(BaseTagReader):

    def __init__(self):
        super().__init__()
        self.PREFIX_ARR = ['000', '001', '010', '011', '100', '101', '110', '111']
        self.MAX_PREFIX = len(self.PREFIX_ARR)

    def manage_collision(self, tags):
        super().manage_collision(tags)
        return self._binary_search(tags)

    def _get_bit_string(self, i):
        if i > (self.MAX_PREFIX-1):
            return
        else:
            return self.PREFIX_ARR[i]
    
    def _binary_search(self, tags, id=''):

        # 1 slot for this evaluation and then add on the recusive chain
        num_slots = 1
        
        if id != '':
            # Then find matching tags
            matching_tags = [t for t in tags if t.id.startswith(id)]
        else:
            matching_tags = tags
        
        # logger.debug(f"TAGS MATCHING PREFIX {id}: {matching_tags}")

        '''Transmit an ID with three numbers. If collision then manage_collision with subset'''
        if len(matching_tags) <= 1:
            logger.debug(f'de-collided: {matching_tags}')
            # return 1 here as we are still querying on that id.
            return 1
        
        # Need all permuations of three bits 000 001 010 011 100 101 110 111
        if len(matching_tags) > 1:
            for i in range(self.MAX_PREFIX):
                tmp_id=f'{id}{self._get_bit_string(i)}'

                logger.debug(f"de-colliding: {matching_tags} using prefix: {tmp_id}")
                num_slots += self._binary_search(matching_tags,tmp_id)
        
        # No tags matched this id.
        return num_slots


class BinaryTagReader(GenOneTagReader):

    def __init__(self):
        super().__init__()
        self.PREFIX_ARR = ['0', '1']
        self.MAX_PREFIX = len(self.PREFIX_ARR)




        
        




