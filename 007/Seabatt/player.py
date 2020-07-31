# -*- coding: utf-8 -*-
from boom import Shut




class Player (Shut):
    def __init__(self, name, mystep):
        self.name=name
        self.mystep=mystep
        super().__init__()
        
