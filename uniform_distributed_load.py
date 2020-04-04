import numpy as np
from load import Load


class UniformDistributedLoad(Load):
    _length: np.float64
    _force: np.float64

    def load(self, position: np.float64):
        if position > 0 && position < self._length:
            return self._force
        else:
            return 0

    def __init__(self, length: np.float64, force: np.float64):
        _length = length
        _force = force
