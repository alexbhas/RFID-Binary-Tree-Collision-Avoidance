import random

class BaseTag():


    def __init__(self):
        self.transmit_time=None
        self.id = self._generate_uid()

    def generate_time(self, min_t=None, max_t=None):
        '''
        Generate the time at which the sensor transmits to the reader
        
            Parameters:
                max (int): the max time. Default=None
                min (int): the min time. Default=None
            
            Returns:
                time (int): the time at which the sensor transmits
        '''

        if min_t is None:
            min_t=0
        
        if max_t is None:
            max_t=min_t+10
        
        self.transmit_time = random.randrange(min_t, max_t)

        return self.transmit_time
        
        
    def _generate_uid(self, length=64):
        return "".join([str(random.randint(0, 1)) for _ in range(length)])
    
    def __str__(self) -> str:
        return self.id
    
    def __repr__(self) -> str:
        return self.__str__()