from abc import abstractmethod

import scipy.integrate as spi
import numpy as np


class Load:

    @property
    @abstractmethod
    def load(self, position):
        pass

    def shear_stress(self, position):
        result = np.zeros_like(position)
        for i, value in enumerate(position):
            y, err = spi.quad(lambda x: self.load(x), 0, value)
            result[i] = y
        return result

