from abc import abstractmethod

import numpy as np


class Load:

    @property
    @abstractmethod
    def load(self, position: np.float64):
        pass
